"""Image-processing kernels for teaching convolution concepts.

Provides a catalog of classic 2-D kernels (edge detection, blur, sharpen,
emboss …) together with helper functions to apply them to images and
visualise the results — all built on top of ``torch.nn.functional.conv2d``
so students can see the direct connection to CNN layers.

Quick start
-----------
>>> from ml.kernels import list_kernels, show_applied, show_all_kernels
>>> list_kernels()
>>> show_applied("photo.jpg", "sobel_v")
>>> show_all_kernels("photo.jpg")
"""

from __future__ import annotations

import math
from pathlib import Path
from typing import Union

import matplotlib.pyplot as plt
import numpy as np
import torch
import torch.nn.functional as F
from PIL import Image

# ---------------------------------------------------------------------------
# Kernel definitions
# ---------------------------------------------------------------------------
# Each entry: name -> (2-D float tensor, short description)
# Tensors are plain (H, W); functions reshape them for conv2d as needed.

_EDGE_KERNELS: list[str] = []  # names flagged for abs() display


def _edge(name: str, tensor: torch.Tensor, desc: str):
    """Register a kernel and mark it as an edge-type kernel."""
    _EDGE_KERNELS.append(name)
    return (tensor, desc)


KERNELS: dict[str, tuple[torch.Tensor, str]] = {
    # -- Edge detection -----------------------------------------------------
    "sobel_h": _edge(
        "sobel_h",
        torch.tensor([[-1., -2., -1.],
                       [ 0.,  0.,  0.],
                       [ 1.,  2.,  1.]]),
        "Sobel — horizontal edges",
    ),
    "sobel_v": _edge(
        "sobel_v",
        torch.tensor([[-1., 0., 1.],
                       [-2., 0., 2.],
                       [-1., 0., 1.]]),
        "Sobel — vertical edges",
    ),
    "prewitt_h": _edge(
        "prewitt_h",
        torch.tensor([[-1., -1., -1.],
                       [ 0.,  0.,  0.],
                       [ 1.,  1.,  1.]]),
        "Prewitt — horizontal edges (simpler weights)",
    ),
    "prewitt_v": _edge(
        "prewitt_v",
        torch.tensor([[-1., 0., 1.],
                       [-1., 0., 1.],
                       [-1., 0., 1.]]),
        "Prewitt — vertical edges (simpler weights)",
    ),
    "laplacian": _edge(
        "laplacian",
        torch.tensor([[ 0., -1.,  0.],
                       [-1.,  4., -1.],
                       [ 0., -1.,  0.]]),
        "Laplacian — edges in all directions",
    ),
    "scharr_h": _edge(
        "scharr_h",
        torch.tensor([[ -3., -10.,  -3.],
                       [  0.,   0.,   0.],
                       [  3.,  10.,   3.]]),
        "Scharr — horizontal edges (more accurate)",
    ),
    "scharr_v": _edge(
        "scharr_v",
        torch.tensor([[ -3., 0.,  3.],
                       [-10., 0., 10.],
                       [ -3., 0.,  3.]]),
        "Scharr — vertical edges (more accurate)",
    ),
    # -- Blurring -----------------------------------------------------------
    "box_blur": (
        torch.ones(3, 3) / 9.0,
        "Box blur 3×3 — simple average",
    ),
    "gaussian_blur_3": (
        torch.tensor([[1., 2., 1.],
                       [2., 4., 2.],
                       [1., 2., 1.]]) / 16.0,
        "Gaussian blur 3×3 (σ ≈ 1)",
    ),
    "gaussian_blur_5": (
        torch.tensor([[1.,  4.,  6.,  4., 1.],
                       [4., 16., 24., 16., 4.],
                       [6., 24., 36., 24., 6.],
                       [4., 16., 24., 16., 4.],
                       [1.,  4.,  6.,  4., 1.]]) / 256.0,
        "Gaussian blur 5×5 (σ ≈ 1.4)",
    ),
    # -- Sharpening ---------------------------------------------------------
    "sharpen": (
        torch.tensor([[ 0., -1.,  0.],
                       [-1.,  5., -1.],
                       [ 0., -1.,  0.]]),
        "Sharpen — enhances local contrast",
    ),
    # -- Other effects ------------------------------------------------------
    "emboss": (
        torch.tensor([[-2., -1., 0.],
                       [-1.,  1., 1.],
                       [ 0.,  1., 2.]]),
        "Emboss — 3-D relief effect",
    ),
    "ridge": _edge(
        "ridge",
        torch.tensor([[-1., -1., -1.],
                       [-1.,  8., -1.],
                       [-1., -1., -1.]]),
        "Ridge / outline detection",
    ),
}


# ---------------------------------------------------------------------------
# Public helpers
# ---------------------------------------------------------------------------

def list_kernels() -> None:
    """Print a formatted table of every available kernel."""
    print(f"{'Name':<20} {'Size':<8} {'Description'}")
    print("-" * 60)
    for name, (tensor, desc) in KERNELS.items():
        h, w = tensor.shape
        print(f"{name:<20} {h}×{w:<5} {desc}")


def get_kernel(name: str) -> torch.Tensor:
    """Return the raw 2-D kernel tensor for *name*."""
    if name not in KERNELS:
        raise KeyError(f"Unknown kernel '{name}'. Use list_kernels() to see options.")
    return KERNELS[name][0]


# ---------------------------------------------------------------------------
# Image loading
# ---------------------------------------------------------------------------

def load_image(source: Union[str, Path, Image.Image, torch.Tensor]) -> torch.Tensor:
    """Load an image and return a float tensor (C, H, W) in [0, 1].

    *source* can be a file path, a PIL Image, or an existing torch tensor
    (in which case it is returned as-is after ensuring float and 3-D shape).
    """
    if isinstance(source, torch.Tensor):
        t = source.float()
        if t.ndim == 2:
            t = t.unsqueeze(0)
        if t.max() > 1.0:
            t = t / 255.0
        return t

    if isinstance(source, (str, Path)):
        source = Image.open(source)

    # PIL Image → tensor
    arr = np.array(source).astype(np.float32) / 255.0
    t = torch.from_numpy(arr)
    if t.ndim == 2:
        # grayscale → (1, H, W)
        t = t.unsqueeze(0)
    else:
        # (H, W, C) → (C, H, W)
        t = t.permute(2, 0, 1)
    return t


# ---------------------------------------------------------------------------
# Applying kernels
# ---------------------------------------------------------------------------

def apply_kernel(image: Union[str, Path, Image.Image, torch.Tensor],
                 kernel_name: str) -> torch.Tensor:
    """Apply the named kernel to *image* and return the result (C, H, W).

    The convolution is done independently per channel using
    ``torch.nn.functional.conv2d`` with padding that preserves the spatial
    size of the input.
    """
    img = load_image(image)                   # (C, H, W)
    k = get_kernel(kernel_name)               # (kH, kW)
    kh, kw = k.shape
    # conv2d expects (N, C, H, W) input and (out_C, in_C, kH, kW) weight.
    # We convolve each channel independently using groups=C.
    C = img.shape[0]
    weight = k.unsqueeze(0).unsqueeze(0).expand(C, 1, kh, kw)  # (C, 1, kH, kW)
    x = img.unsqueeze(0)                                        # (1, C, H, W)
    pad_h, pad_w = kh // 2, kw // 2
    out = F.conv2d(x, weight, bias=None, stride=1,
                   padding=(pad_h, pad_w), groups=C)
    return out.squeeze(0)                                        # (C, H, W)


def _prepare_for_display(tensor: torch.Tensor, kernel_name: str) -> np.ndarray:
    """Convert a (C, H, W) result tensor to a numpy array ready for imshow."""
    if kernel_name in _EDGE_KERNELS:
        tensor = tensor.abs()
    tensor = tensor.clamp(0, 1)
    arr = tensor.detach().numpy()
    if arr.shape[0] == 1:
        return arr[0]          # grayscale → (H, W)
    return np.transpose(arr, (1, 2, 0))  # (C, H, W) → (H, W, C)


# ---------------------------------------------------------------------------
# Visualisation
# ---------------------------------------------------------------------------

def show_kernel(name: str) -> None:
    """Display a heatmap of the kernel matrix with annotated values."""
    k = get_kernel(name)
    desc = KERNELS[name][1]
    arr = k.numpy()
    fig, ax = plt.subplots(figsize=(3, 3))
    im = ax.imshow(arr, cmap="RdBu_r", vmin=-arr.max(), vmax=arr.max())
    # Annotate each cell with its value
    for i in range(arr.shape[0]):
        for j in range(arr.shape[1]):
            ax.text(j, i, f"{arr[i, j]:.3g}", ha="center", va="center",
                    fontsize=10, color="black")
    ax.set_title(f"{name}\n{desc}", fontsize=10)
    ax.set_xticks([])
    ax.set_yticks([])
    plt.colorbar(im, ax=ax, fraction=0.046, pad=0.04)
    plt.tight_layout()
    plt.show()


def show_applied(image: Union[str, Path, Image.Image, torch.Tensor],
                 kernel_name: str, cmap: str = "gray") -> None:
    """Show the original and filtered image side by side."""
    img = load_image(image)
    result = apply_kernel(img, kernel_name)

    orig_np = _prepare_for_display(img, "")          # never abs original
    filt_np = _prepare_for_display(result, kernel_name)

    fig, axes = plt.subplots(1, 2, figsize=(8, 4))
    axes[0].imshow(orig_np, cmap=cmap)
    axes[0].set_title("Original")
    axes[0].axis("off")
    axes[1].imshow(filt_np, cmap=cmap)
    axes[1].set_title(kernel_name)
    axes[1].axis("off")
    plt.tight_layout()
    plt.show()


def show_all_kernels(image: Union[str, Path, Image.Image, torch.Tensor],
                     kernel_names: list[str] | None = None,
                     cols: int = 4) -> None:
    """Apply every kernel (or a subset) to *image* and display a grid."""
    img = load_image(image)
    names = kernel_names if kernel_names is not None else list(KERNELS.keys())
    n = len(names)
    rows = math.ceil(n / cols)

    fig, axes = plt.subplots(rows, cols, figsize=(4 * cols, 4 * rows))
    axes = np.asarray(axes).flatten()

    for idx, name in enumerate(names):
        result = apply_kernel(img, name)
        arr = _prepare_for_display(result, name)
        axes[idx].imshow(arr, cmap="gray")
        axes[idx].set_title(name, fontsize=10)
        axes[idx].axis("off")

    # Hide unused subplots
    for idx in range(n, len(axes)):
        axes[idx].axis("off")

    plt.tight_layout()
    plt.show()


# ---------------------------------------------------------------------------
# Main — demo with edge-detection kernels
# ---------------------------------------------------------------------------

_SAMPLE_IMAGE = Path(__file__).resolve().parent.parent.parent / "images" / "field_for_kernels"

_EDGE_DETECTION_KERNELS = [
    "sobel_h", "sobel_v",
    "prewitt_h", "prewitt_v",
    "laplacian",
    "scharr_h", "scharr_v",
    "ridge",
]


def main() -> None:
    image_path = _SAMPLE_IMAGE
    print(f"Sample image: {image_path}")

    print("\nAvailable kernels:")
    list_kernels()

    print("\nShowing edge-detection kernels on sample image...")
    show_all_kernels(image_path, kernel_names=_EDGE_DETECTION_KERNELS, cols=4)


if __name__ == "__main__":
    main()

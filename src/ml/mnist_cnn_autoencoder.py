import torch
import torch.nn as nn
from torch.utils.data import DataLoader
import matplotlib.pyplot as plt
import argparse
import json
import os
from typing import Tuple, Dict, Any

# Default configuration
DEFAULT_CONFIG = {
    "learning_rate": 1e-3,
    "epochs": 10,
    "batch_size": 128,
    "latent_dim": 128,
    "num_workers": 2,
    "checkpoint_path": "mnist_cnn_autoencoder.pt",
    "device": "cuda" if torch.cuda.is_available() else "cpu",
}


class CNNAutoencoder(nn.Module):
    """
    CNN-based autoencoder for MNIST digit reconstruction.

    Architecture:
    - Encoder: Conv2d layers with MaxPool2d for spatial downsampling (28x28 -> 7x7)
    - Latent: Bottleneck representation (default 128-d)
    - Decoder: ConvTranspose2d layers for spatial upsampling (7x7 -> 28x28)
    """

    def __init__(self, latent_dim: int = 128):
        super().__init__()
        self.latent_dim = latent_dim

        # Encoder: progressively downsample spatial dimensions
        self.encoder = nn.Sequential(
            nn.Conv2d(1, 16, kernel_size=3, stride=1, padding=1),  # 1x28x28 -> 16x28x28
            nn.ReLU(),
            nn.MaxPool2d(2),  # 16x28x28 -> 16x14x14

            nn.Conv2d(16, 32, kernel_size=3, stride=1, padding=1),  # 16x14x14 -> 32x14x14
            nn.ReLU(),
            nn.MaxPool2d(2),  # 32x14x14 -> 32x7x7

            nn.Conv2d(32, 64, kernel_size=3, stride=1, padding=1),  # 32x7x7 -> 64x7x7
            nn.ReLU(),
        )

        # Latent space
        self.fc_encode = nn.Linear(64 * 7 * 7, latent_dim)
        self.fc_decode = nn.Linear(latent_dim, 64 * 7 * 7)

        # Decoder: progressively upsample spatial dimensions
        self.decoder = nn.Sequential(
            nn.ConvTranspose2d(64, 32, kernel_size=4, stride=2, padding=1),  # 64x7x7 -> 32x14x14
            nn.ReLU(),

            nn.ConvTranspose2d(32, 16, kernel_size=4, stride=2, padding=1),  # 32x14x14 -> 16x28x28
            nn.ReLU(),

            nn.Conv2d(16, 1, kernel_size=3, stride=1, padding=1),  # 16x28x28 -> 1x28x28
            nn.Sigmoid(),  # Ensure output in [0, 1] range
        )

    def encode(self, x: torch.Tensor) -> torch.Tensor:
        """Encode input to latent representation."""
        h = self.encoder(x)
        h = h.view(h.size(0), -1)  # Flatten
        z = self.fc_encode(h)
        return z

    def decode(self, z: torch.Tensor) -> torch.Tensor:
        """Decode latent representation to image."""
        h = self.fc_decode(z)
        h = h.view(-1, 64, 7, 7)  # Reshape to feature maps
        xhat = self.decoder(h)
        return xhat

    def forward(self, x: torch.Tensor) -> Tuple[torch.Tensor, torch.Tensor]:
        """Full forward pass: encode then decode."""
        z = self.encode(x)
        xhat = self.decode(z)
        return xhat, z


def load_mnist_data(batch_size: int = 128, num_workers: int = 2) -> Tuple[DataLoader, DataLoader]:
    """
    Load MNIST dataset for autoencoder training.

    Args:
        batch_size: Batch size for DataLoader
        num_workers: Number of worker processes for data loading

    Returns:
        train_loader: DataLoader for training set
        test_loader: DataLoader for test set
    """
    try:
        from torchvision import datasets, transforms
    except Exception as e:
        raise RuntimeError(
            f"Could not import torchvision. Please install torchvision.\nError: {e}"
        )

    transform = transforms.Compose([transforms.ToTensor()])

    train_ds = datasets.MNIST(
        root="./data",
        train=True,
        download=True,
        transform=transform
    )
    test_ds = datasets.MNIST(
        root="./data",
        train=False,
        download=True,
        transform=transform
    )

    train_loader = DataLoader(
        train_ds,
        batch_size=batch_size,
        shuffle=True,
        num_workers=num_workers
    )
    test_loader = DataLoader(
        test_ds,
        batch_size=batch_size,
        shuffle=False,
        num_workers=num_workers
    )

    return train_loader, test_loader


def train_epoch(model: nn.Module, loader: DataLoader, optimizer: torch.optim.Optimizer,
                criterion: nn.Module, device: str) -> float:
    """
    Train for one epoch.

    Args:
        model: The autoencoder model
        loader: Training data loader
        optimizer: Optimizer
        criterion: Loss function
        device: Device to use ('cuda' or 'cpu')

    Returns:
        Average loss for the epoch
    """
    model.train()
    total_loss = 0.0
    n_samples = 0

    for x, _ in loader:  # Ignore labels (unsupervised learning)
        x = x.to(device)

        optimizer.zero_grad()
        xhat, z = model(x)
        loss = criterion(xhat, x)
        loss.backward()
        optimizer.step()

        total_loss += loss.item() * x.size(0)
        n_samples += x.size(0)

    return total_loss / n_samples


@torch.no_grad()
def eval_epoch(model: nn.Module, loader: DataLoader, criterion: nn.Module,
               device: str) -> float:
    """
    Evaluate on validation/test set.

    Args:
        model: The autoencoder model
        loader: Test data loader
        criterion: Loss function
        device: Device to use ('cuda' or 'cpu')

    Returns:
        Average loss for the epoch
    """
    model.eval()
    total_loss = 0.0
    n_samples = 0

    for x, _ in loader:  # Ignore labels
        x = x.to(device)
        xhat, z = model(x)
        loss = criterion(xhat, x)

        total_loss += loss.item() * x.size(0)
        n_samples += x.size(0)

    return total_loss / n_samples


def train_model(model: nn.Module, train_loader: DataLoader, test_loader: DataLoader,
                config: Dict[str, Any]) -> Tuple[list, list]:
    """
    Complete training loop.

    Args:
        model: The autoencoder model
        train_loader: Training data loader
        test_loader: Test data loader
        config: Configuration dictionary

    Returns:
        train_losses: List of training losses per epoch
        test_losses: List of test losses per epoch
    """
    device = config["device"]
    model = model.to(device)

    criterion = nn.MSELoss()
    optimizer = torch.optim.Adam(
        model.parameters(),
        lr=config["learning_rate"]
    )

    train_losses = []
    test_losses = []

    print(f"Starting training for {config['epochs']} epochs...")
    print(f"Device: {device}")
    print(f"Model parameters: {sum(p.numel() for p in model.parameters()):,}")

    for epoch in range(1, config["epochs"] + 1):
        train_loss = train_epoch(model, train_loader, optimizer, criterion, device)
        test_loss = eval_epoch(model, test_loader, criterion, device)

        train_losses.append(train_loss)
        test_losses.append(test_loss)

        print(f"Epoch {epoch:02d}/{config['epochs']} | "
              f"train_loss={train_loss:.4f} | test_loss={test_loss:.4f}")

    return train_losses, test_losses


def save_checkpoint(model: nn.Module, config: Dict[str, Any], checkpoint_path: str) -> None:
    """
    Save model checkpoint with metadata.

    Args:
        model: The trained model
        config: Configuration dictionary
        checkpoint_path: Path to save the checkpoint
    """
    os.makedirs(os.path.dirname(checkpoint_path) or ".", exist_ok=True)

    payload = {
        "model_state_dict": model.state_dict(),
        "model_class": "CNNAutoencoder",
        "config": {
            "latent_dim": config["latent_dim"],
            "learning_rate": config["learning_rate"],
            "epochs": config["epochs"],
            "batch_size": config["batch_size"],
        },
        "input_shape": (1, 28, 28),
        "output_shape": (1, 28, 28),
    }

    torch.save(payload, checkpoint_path)
    print(f"Saved checkpoint to: {checkpoint_path}")


def load_checkpoint(checkpoint_path: str, device: str = "cpu") -> Tuple[nn.Module, Dict[str, Any]]:
    """
    Load model from checkpoint.

    Args:
        checkpoint_path: Path to the checkpoint file
        device: Device to load the model to

    Returns:
        model: Loaded model in eval mode
        ckpt: Checkpoint dictionary with metadata
    """
    ckpt = torch.load(checkpoint_path, map_location=device)

    latent_dim = ckpt["config"]["latent_dim"]
    model = CNNAutoencoder(latent_dim=latent_dim)
    model.load_state_dict(ckpt["model_state_dict"])
    model = model.to(device)
    model.eval()

    return model, ckpt


def visualize_reconstructions(model: nn.Module, loader: DataLoader, device: str,
                             n_samples: int = 10) -> None:
    """
    Visualize original vs reconstructed images.

    Args:
        model: The autoencoder model
        loader: Data loader
        device: Device to use
        n_samples: Number of samples to visualize
    """
    model.eval()

    # Get a batch
    x, _ = next(iter(loader))
    x = x[:n_samples].to(device)

    with torch.no_grad():
        xhat, z = model(x)

    # Move to CPU for plotting
    x = x.cpu()
    xhat = xhat.cpu()

    fig, axes = plt.subplots(2, n_samples, figsize=(n_samples * 1.5, 3))
    for i in range(n_samples):
        axes[0, i].imshow(x[i, 0], cmap="gray")
        axes[0, i].axis("off")
        axes[1, i].imshow(xhat[i, 0], cmap="gray")
        axes[1, i].axis("off")

    axes[0, 0].set_ylabel("Original", fontsize=12)
    axes[1, 0].set_ylabel("Reconstructed", fontsize=12)
    plt.suptitle("CNN Autoencoder: Input vs Reconstruction", fontsize=14)
    plt.tight_layout()
    plt.show()


def visualize_latent_space(model: nn.Module, loader: DataLoader, device: str) -> None:
    """
    Visualize 2D latent space (only works if latent_dim==2).

    Args:
        model: The autoencoder model
        loader: Data loader
        device: Device to use
    """
    model.eval()

    zs = []
    ys = []

    with torch.no_grad():
        for x, y in loader:
            x = x.to(device)
            _, z = model(x)
            zs.append(z.cpu())
            ys.append(y)

    Z = torch.cat(zs, dim=0).numpy()
    Y = torch.cat(ys, dim=0).numpy()

    if Z.shape[1] != 2:
        print(f"Latent space visualization only available for 2D "
              f"(current: {Z.shape[1]}D)")
        return

    plt.figure(figsize=(8, 8))
    scatter = plt.scatter(Z[:, 0], Z[:, 1], c=Y, s=3, cmap="tab10")
    plt.colorbar(scatter)
    plt.title("CNN Autoencoder: Latent Space (colored by digit)")
    plt.xlabel("z1")
    plt.ylabel("z2")
    plt.grid(True, alpha=0.3)
    plt.tight_layout()
    plt.show()


def plot_training_curves(train_losses: list, test_losses: list) -> None:
    """
    Plot training and test loss curves.

    Args:
        train_losses: List of training losses
        test_losses: List of test losses
    """
    epochs = len(train_losses)

    plt.figure(figsize=(10, 5))
    plt.plot(range(1, epochs + 1), train_losses, label="Train Loss", marker='o')
    plt.plot(range(1, epochs + 1), test_losses, label="Test Loss", marker='s')
    plt.xlabel("Epoch")
    plt.ylabel("Reconstruction Loss (MSE)")
    plt.title("CNN Autoencoder Training")
    plt.legend()
    plt.grid(True, alpha=0.3)
    plt.tight_layout()
    plt.show()


def main():
    parser = argparse.ArgumentParser(
        description="CNN Autoencoder for MNIST"
    )
    parser.add_argument(
        "--config",
        type=str,
        help="Path to configuration JSON file"
    )
    parser.add_argument(
        "--mode",
        type=str,
        choices=["train", "visualize"],
        default="train",
        help="Mode: train model or visualize from checkpoint"
    )
    parser.add_argument(
        "--checkpoint",
        type=str,
        default=None,
        help="Path to model checkpoint (.pt)"
    )
    parser.add_argument(
        "--latent-dim",
        type=int,
        default=None,
        help="Latent space dimension"
    )
    parser.add_argument(
        "--epochs",
        type=int,
        default=None,
        help="Number of training epochs"
    )
    parser.add_argument(
        "--batch-size",
        type=int,
        default=None,
        help="Batch size for training"
    )

    args = parser.parse_args()

    # Load config
    config = DEFAULT_CONFIG.copy()
    if args.config and os.path.exists(args.config):
        with open(args.config, "r") as f:
            user_config = json.load(f)
        config.update(user_config)
        print(f"Loaded config from {args.config}")

    # Override with CLI args if provided
    if args.latent_dim is not None:
        config["latent_dim"] = args.latent_dim
    if args.epochs is not None:
        config["epochs"] = args.epochs
    if args.batch_size is not None:
        config["batch_size"] = args.batch_size
    if args.checkpoint is not None:
        config["checkpoint_path"] = args.checkpoint

    device = config["device"]
    print(f"Using device: {device}")

    if args.mode == "train":
        # Load data
        print("Loading MNIST dataset...")
        train_loader, test_loader = load_mnist_data(
            batch_size=config["batch_size"],
            num_workers=config["num_workers"]
        )

        # Create model
        model = CNNAutoencoder(latent_dim=config["latent_dim"])
        print(f"Created CNNAutoencoder with latent_dim={config['latent_dim']}")

        # Train
        train_losses, test_losses = train_model(
            model, train_loader, test_loader, config
        )

        # Save checkpoint
        save_checkpoint(model, config, config["checkpoint_path"])

        # Plot results
        print("\nDisplaying training curves...")
        plot_training_curves(train_losses, test_losses)

        # Visualize reconstructions
        print("Displaying reconstructions...")
        visualize_reconstructions(model, test_loader, device)

        # Visualize latent space if 2D
        if config["latent_dim"] == 2:
            print("Displaying latent space...")
            visualize_latent_space(model, test_loader, device)

    elif args.mode == "visualize":
        # Load checkpoint
        checkpoint_path = config["checkpoint_path"]
        if not os.path.exists(checkpoint_path):
            raise FileNotFoundError(f"Checkpoint not found: {checkpoint_path}")

        print(f"Loading model from: {checkpoint_path}")
        model, ckpt = load_checkpoint(checkpoint_path, device)
        print(f"Latent dimension: {ckpt['config']['latent_dim']}")
        print(f"Model parameters: {sum(p.numel() for p in model.parameters()):,}")

        # Load data
        print("Loading MNIST dataset...")
        _, test_loader = load_mnist_data(
            batch_size=config["batch_size"],
            num_workers=config["num_workers"]
        )

        # Visualize
        print("Displaying reconstructions...")
        visualize_reconstructions(model, test_loader, device)

        if ckpt["config"]["latent_dim"] == 2:
            print("Displaying latent space...")
            visualize_latent_space(model, test_loader, device)


if __name__ == "__main__":
    main()

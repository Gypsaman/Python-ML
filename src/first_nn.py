from __future__ import annotations

import importlib.util
import sys
import subprocess
from dataclasses import dataclass
from typing import Tuple

import numpy as np


import torch
import torch.nn as nn
from torch.utils.data import TensorDataset, DataLoader


@dataclass
class Config:
    seed: int = 0
    n_samples: int = 400
    batch_size: int = 32
    lr: float = 1e-2
    epochs: int = 30
    log_every: int = 5


def set_seed(torch, seed: int) -> None:
    torch.manual_seed(seed)


def make_blobs_dataset(torch, n_samples: int) -> Tuple["torch.Tensor", "torch.Tensor"]:
    """
    Synthetic 2D dataset:
    - Class 0 centered near (-2, 0)
    - Class 1 centered near ( 2, 0)
    """
    x0 = torch.randn(n_samples // 2, 2) + torch.tensor([-2.0, 0.0])
    x1 = torch.randn(n_samples // 2, 2) + torch.tensor([2.0, 0.0])

    X = torch.cat([x0, x1], dim=0)
    y = torch.cat([torch.zeros(n_samples // 2), torch.ones(n_samples // 2)]).long()
    return X, y


def make_dataloader(TensorDataset, DataLoader, X, y, batch_size: int):
    ds = TensorDataset(X, y)
    return DataLoader(ds, batch_size=batch_size, shuffle=True)


def build_model(nn):
    class MLP(nn.Module):
        def __init__(self):
            super().__init__()
            self.net = nn.Sequential(
                nn.Linear(2, 16),
                nn.ReLU(),
                nn.Linear(16, 2),
            )

        def forward(self, x):
            return self.net(x)

    return MLP()


def make_training_objects(torch, nn, model, lr: float):
    criterion = nn.CrossEntropyLoss()
    optimizer = torch.optim.Adam(model.parameters(), lr=lr)
    return criterion, optimizer


def train(torch, model, train_loader, criterion, optimizer, epochs: int, log_every: int, X, y) -> None:

    for epoch in range(epochs):
        model.train()
        total_loss = 0.0

        for xb, yb in train_loader:
            optimizer.zero_grad()
            logits = model(xb)          # forward
            loss = criterion(logits, yb)
            loss.backward()             # backward
            optimizer.step()            # update
            total_loss += loss.item()

        if (epoch + 1) % log_every == 0:
                avg_loss = total_loss / len(train_loader)
                acc = evaluate_accuracy(torch, model, X, y)

                print(
                    f"época {epoch+1:02d} | "
                    f"pérdida {avg_loss:.4f} | "
                    f"accuracy {acc}"
                )


def evaluate_accuracy(torch, model, X, y) -> float:
    model.eval()
    with torch.no_grad():
        logits = model(X)
        pred = logits.argmax(dim=1)
        acc = (pred == y).float().mean().item()
    return acc




def main() -> None:

    print("versión de torch:", torch.__version__)

    cfg = Config()
    set_seed(torch, cfg.seed)

    #  Data
    X, y = make_blobs_dataset(torch, cfg.n_samples)
    train_loader = make_dataloader(TensorDataset, DataLoader, X, y, cfg.batch_size)
    print("X.shape:", tuple(X.shape), "| y.shape:", tuple(y.shape))

    # Model + training objects
    model = build_model(nn)
    criterion, optimizer = make_training_objects(torch, nn, model, cfg.lr)

    #  Train
    train(torch, model, train_loader, criterion, optimizer, cfg.epochs, cfg.log_every,X,y)

    # 6) Evaluate
    acc = evaluate_accuracy(torch, model, X, y)
    print("Accuracy (on full dataset):", acc)


if __name__ == "__main__":
    main()

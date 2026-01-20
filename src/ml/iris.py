import torch
import torch.nn as nn
import torch.optim as optim
from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from torch.utils.data import DataLoader, TensorDataset
import numpy as np
import matplotlib.pyplot as plt
import argparse
import json
import os
import pickle
from typing import Tuple, Dict, Any, Optional, List

# Default configuration
DEFAULT_CONFIG = {
    "learning_rate": 0.01,
    "epochs": 200,
    "batch_size": 32,
    "optimizer": "SGD",
    "optimizer_params": {},
    # New: checkpoint outputs
    "checkpoint_path": "iris_model.pt",
    "scaler_path": "iris_scaler.pkl",
}

CLASS_NAMES = ["setosa", "versicolor", "virginica"]


class Net(nn.Module):
    def __init__(self):
        super(Net, self).__init__()
        self.fc1 = nn.Linear(4, 16)
        self.fc2 = nn.Linear(16, 16)
        self.fc3 = nn.Linear(16, 3)

    def forward(self, x):
        x = torch.relu(self.fc1(x))
        x = torch.relu(self.fc2(x))
        x = self.fc3(x)  # logits
        return x


def load_data(batch_size: Optional[int] = None, random_state: int = 42):
    """
    Loads Iris dataset, preprocesses it, and returns:
      - train_loader, test_loader
      - fitted scaler (IMPORTANT for inference)
      - raw X_test, y_test (tensors)
    """
    iris = load_iris()
    X = iris.data
    y = iris.target

    # Split FIRST, then fit scaler ONLY on train to avoid data leakage.
    X_train_np, X_test_np, y_train_np, y_test_np = train_test_split(
        X, y, test_size=0.2, random_state=random_state, stratify=y
    )

    scaler = StandardScaler()
    X_train_np = scaler.fit_transform(X_train_np)
    X_test_np = scaler.transform(X_test_np)

    # Convert to tensors
    X_train = torch.from_numpy(X_train_np).float()
    y_train = torch.from_numpy(y_train_np).long()
    X_test = torch.from_numpy(X_test_np).float()
    y_test = torch.from_numpy(y_test_np).long()

    if batch_size:
        train_dataset = TensorDataset(X_train, y_train)
        test_dataset = TensorDataset(X_test, y_test)
        train_loader = DataLoader(train_dataset, batch_size=batch_size, shuffle=True)
        test_loader = DataLoader(test_dataset, batch_size=batch_size, shuffle=False)
        return train_loader, test_loader, scaler, X_test, y_test

    # Not used in your current flow, but kept for completeness
    return X_train, X_test, y_train, y_test, scaler


def get_optimizer(model, config):
    """
    Factory function to get the optimizer based on config.
    """
    opt_name = config.get("optimizer", "SGD").upper()
    lr = config.get("learning_rate", 0.01)
    params = config.get("optimizer_params", {})

    if opt_name == "SGD":
        return optim.SGD(model.parameters(), lr=lr, **params)
    elif opt_name == "RMSPROP":
        return optim.RMSprop(model.parameters(), lr=lr, **params)
    elif opt_name == "ADAM":
        return optim.Adam(model.parameters(), lr=lr, **params)
    else:
        raise ValueError(f"Unsupported optimizer: {opt_name}. Valid: SGD, RMSPROP, ADAM")


def evaluate_model(model, test_loader, print_acc=True):
    model.eval()
    correct = 0
    total = 0
    with torch.no_grad():
        for inputs, labels in test_loader:
            outputs = model(inputs)
            _, predicted = torch.max(outputs.data, 1)
            total += labels.size(0)
            correct += (predicted == labels).sum().item()

    acc = 100 * correct / total
    if print_acc:
        print(f"\nTest Accuracy: {acc:.2f}%")
    return acc


def train_model(model, train_loader, test_loader, criterion, optimizer, epochs):
    """
    Training loop.
    """
    train_losses = []
    train_accuracies = []
    test_accuracies = []

    model.train()
    for epoch in range(epochs):
        running_loss = 0.0
        correct = 0
        total = 0

        for inputs, labels in train_loader:
            optimizer.zero_grad()
            outputs = model(inputs)
            loss = criterion(outputs, labels)
            loss.backward()
            optimizer.step()

            running_loss += loss.item()
            _, predicted = torch.max(outputs.data, 1)
            total += labels.size(0)
            correct += (predicted == labels).sum().item()

        epoch_loss = running_loss / max(1, len(train_loader))
        epoch_acc = 100 * correct / max(1, total)

        train_losses.append(epoch_loss)
        train_accuracies.append(epoch_acc)

        test_acc = evaluate_model(model, test_loader, print_acc=False)
        test_accuracies.append(test_acc)
        model.train()

        if (epoch + 1) % 50 == 0:
            print(
                f"Epoch [{epoch+1}/{epochs}], "
                f"Loss: {epoch_loss:.4f}, Train Acc: {epoch_acc:.2f}%, Test Acc: {test_acc:.2f}%"
            )

    return train_losses, train_accuracies, test_accuracies


def plot_results(train_losses, train_accuracies, test_accuracies):
    epochs = len(train_losses)
    plt.figure(figsize=(15, 5))
    plt.subplot(1, 2, 1)
    plt.plot(range(1, epochs + 1), train_losses, label="Training Loss")
    plt.xlabel("Epochs")
    plt.ylabel("Loss")
    plt.title("Training Loss over Epochs")
    plt.legend()

    plt.subplot(1, 2, 2)
    plt.plot(range(1, epochs + 1), train_accuracies, label="Training Accuracy")
    plt.plot(range(1, epochs + 1), test_accuracies, label="Test Accuracy")
    plt.xlabel("Epochs")
    plt.ylabel("Accuracy (%)")
    plt.title("Training and Test Accuracy over Epochs")
    plt.legend()

    plt.tight_layout()
    plt.show()


# -------------------------
# NEW: persistence utilities
# -------------------------

def save_scaler(scaler: StandardScaler, path: str) -> None:
    os.makedirs(os.path.dirname(path) or ".", exist_ok=True)
    with open(path, "wb") as f:
        pickle.dump(scaler, f)


def load_scaler(path: str) -> StandardScaler:
    with open(path, "rb") as f:
        return pickle.load(f)


def save_checkpoint(
    model: nn.Module,
    config: Dict[str, Any],
    checkpoint_path: str,
) -> None:
    os.makedirs(os.path.dirname(checkpoint_path) or ".", exist_ok=True)
    payload = {
        "model_state_dict": model.state_dict(),
        "model_class": "Net",
        "config": {
            "learning_rate": config.get("learning_rate"),
            "epochs": config.get("epochs"),
            "batch_size": config.get("batch_size"),
            "optimizer": config.get("optimizer"),
            "optimizer_params": config.get("optimizer_params", {}),
        },
        "class_names": CLASS_NAMES,
        "input_dim": 4,
        "output_dim": 3,
    }
    torch.save(payload, checkpoint_path)


def load_model_from_checkpoint(checkpoint_path: str, device: Optional[str] = None) -> Tuple[nn.Module, Dict[str, Any]]:
    if device is None:
        device = "cpu"
    ckpt = torch.load(checkpoint_path, map_location=device)

    # In this simple case we know it's Net(), but we keep ckpt metadata anyway.
    model = Net().to(device)
    model.load_state_dict(ckpt["model_state_dict"])
    model.eval()
    return model, ckpt


# -------------------------
# NEW: prediction module
# -------------------------

def parse_features(features_str: str) -> np.ndarray:
    """
    Accepts:
      --features "5.1,3.5,1.4,0.2"
    Returns shape (1,4).
    """
    parts = [p.strip() for p in features_str.split(",")]
    if len(parts) != 4:
        raise ValueError("Expected exactly 4 comma-separated values: sepal_len,sepal_wid,petal_len,petal_wid")
    vals = np.array([float(x) for x in parts], dtype=np.float32).reshape(1, 4)
    return vals


@torch.no_grad()
def predict_one(
    checkpoint_path: str,
    scaler_path: str,
    features: np.ndarray,
    device: str = "cpu",
) -> Dict[str, Any]:
    """
    Predict a single example.
    features: numpy array shape (1,4) in RAW input units (not standardized).
    """
    model, ckpt = load_model_from_checkpoint(checkpoint_path, device=device)
    scaler = load_scaler(scaler_path)

    x_std = scaler.transform(features)  # shape (1,4)
    x_tensor = torch.from_numpy(x_std).float().to(device)

    logits = model(x_tensor)  # shape (1,3)
    probs = torch.softmax(logits, dim=1).cpu().numpy().flatten()
    pred_idx = int(np.argmax(probs))
    class_names = ckpt.get("class_names", CLASS_NAMES)

    return {
        "predicted_index": pred_idx,
        "predicted_label": class_names[pred_idx],
        "probabilities": {class_names[i]: float(probs[i]) for i in range(len(class_names))},
    }


def main():
    parser = argparse.ArgumentParser(description="Iris Neural Network (train/predict)")
    parser.add_argument("--config", type=str, help="Path to configuration JSON file")

    # NEW: mode selection
    parser.add_argument("--mode", type=str, choices=["train", "predict"], default="train",
                        help="train: train and save weights; predict: load weights and predict one sample")

    # NEW: predict-time args
    parser.add_argument("--checkpoint", type=str, default=None, help="Path to model checkpoint (.pt)")
    parser.add_argument("--scaler", type=str, default=None, help="Path to saved scaler (.pkl)")
    parser.add_argument("--features", type=str, default=None,
                        help='Comma-separated 4 features: "sepal_len,sepal_wid,petal_len,petal_wid"')
    parser.add_argument("--device", type=str, default="cpu", help='Device: "cpu" or "cuda" (if available)')

    args = parser.parse_args()

    config = DEFAULT_CONFIG.copy()
    if args.config:
        if os.path.exists(args.config):
            with open(args.config, "r") as f:
                user_config = json.load(f)
            config.update(user_config)
            print(f"Loaded config from {args.config}")
        else:
            print(f"Config file {args.config} not found, using defaults.")
    else:
        print("No config provided, using defaults.")

    checkpoint_path = args.checkpoint or config.get("checkpoint_path", "iris_model.pt")
    scaler_path = args.scaler or config.get("scaler_path", "iris_scaler.pkl")

    if args.mode == "train":
        batch_size = int(config.get("batch_size", 32))
        epochs = int(config.get("epochs", 200))

        # Load Data (and scaler)
        train_loader, test_loader, scaler, _, _ = load_data(batch_size=batch_size)

        # Initialize
        model = Net().to(args.device)
        criterion = nn.CrossEntropyLoss()
        optimizer = get_optimizer(model, config)

        # Train
        train_losses, train_accuracies, test_accuracies = train_model(
            model, train_loader, test_loader, criterion, optimizer, epochs
        )

        # Evaluate (Final)
        evaluate_model(model, test_loader)

        # Save artifacts
        save_checkpoint(model, config, checkpoint_path)
        save_scaler(scaler, scaler_path)
        print(f"Saved checkpoint to: {checkpoint_path}")
        print(f"Saved scaler to:     {scaler_path}")

        # Plot
        plot_results(train_losses, train_accuracies, test_accuracies)

    elif args.mode == "predict":
        if not args.features:
            raise ValueError('For --mode predict you must provide --features "5.1,3.5,1.4,0.2"')

        features = parse_features(args.features)
        result = predict_one(
            checkpoint_path=checkpoint_path,
            scaler_path=scaler_path,
            features=features,
            device=args.device,
        )
        print(json.dumps(result, indent=2))


if __name__ == "__main__":
    main()

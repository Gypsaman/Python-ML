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

# Default configuration
DEFAULT_CONFIG = {
    "learning_rate": 0.01,
    "epochs": 200,
    "batch_size": 32,
    "optimizer": "SGD",
    "optimizer_params": {}
}

class Net(nn.Module):
    def __init__(self):
        super(Net, self).__init__()
        self.fc1 = nn.Linear(4, 16)
        self.fc2 = nn.Linear(16, 16)
        self.fc3 = nn.Linear(16, 3)

    def forward(self, x):
        x = torch.relu(self.fc1(x))
        x = torch.relu(self.fc2(x))
        x = self.fc3(x)
        return x

def load_data(batch_size=None):
    """
    Loads Iris dataset, preprocesses it, and returns data loaders (or tensors if batch_size is None).
    """
    iris = load_iris()
    X = iris.data
    y = iris.target

    # Standardize
    scaler = StandardScaler()
    X = scaler.fit_transform(X)

    # Split
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

    # Convert to tensors
    X_train = torch.from_numpy(X_train).float()
    y_train = torch.from_numpy(y_train).long()
    X_test = torch.from_numpy(X_test).float()
    y_test = torch.from_numpy(y_test).long()

    if batch_size:
        train_dataset = TensorDataset(X_train, y_train)
        test_dataset = TensorDataset(X_test, y_test)
        train_loader = DataLoader(train_dataset, batch_size=batch_size, shuffle=True)
        test_loader = DataLoader(test_dataset, batch_size=batch_size, shuffle=False)
        return train_loader, test_loader, X_test, y_test # Returning raw test data too for simple eval if needed
    
    return X_train, X_test, y_train, y_test

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
        raise ValueError(f"Unsupported optimizer: {opt_name}. Valid SGD RMSPROP, ADAM")

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
        
        # Handle both DataLoader and raw tensors (if user didn't request batching, but we implemented it)
        # Using DataLoader loop here
        for i, (inputs, labels) in enumerate(train_loader):
            optimizer.zero_grad()
            outputs = model(inputs)
            loss = criterion(outputs, labels)
            loss.backward()
            optimizer.step()
            
            running_loss += loss.item()
            _, predicted = torch.max(outputs.data, 1)
            total += labels.size(0)
            correct += (predicted == labels).sum().item()
            
        epoch_loss = running_loss / len(train_loader)
        epoch_acc = 100 * correct / total
        
        train_losses.append(epoch_loss)
        train_accuracies.append(epoch_acc)

        # Track test accuracy
        test_acc = evaluate_model(model, test_loader, print_acc=False)
        test_accuracies.append(test_acc)
        model.train() # Switch back to train mode
        
        if (epoch + 1) % 50 == 0:
            print(f'Epoch [{epoch+1}/{epochs}], Loss: {epoch_loss:.4f}, Train Accuracy: {epoch_acc:.2f}%, Test Accuracy: {test_acc:.2f}%')
            
    return train_losses, train_accuracies, test_accuracies

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
        print(f'\nTest Accuracy: {acc:.2f}%')
    return acc

def plot_results(train_losses, train_accuracies, test_accuracies):
    epochs = len(train_losses)
    plt.figure(figsize=(15, 5))
    plt.subplot(1, 2, 1)
    plt.plot(range(1, epochs + 1), train_losses, label='Training Loss')
    plt.xlabel('Epochs')
    plt.ylabel('Loss')
    plt.title('Training Loss over Epochs')
    plt.legend()

    plt.subplot(1, 2, 2)
    plt.plot(range(1, epochs + 1), train_accuracies, label='Training Accuracy', color='orange')
    plt.plot(range(1, epochs + 1), test_accuracies, label='Test Accuracy', color='green')
    plt.xlabel('Epochs')
    plt.ylabel('Accuracy (%)')
    plt.title('Training and Test Accuracy over Epochs')
    plt.legend()

    plt.tight_layout()
    plt.show()

def main():
    parser = argparse.ArgumentParser(description='Iris Neural Network')
    parser.add_argument('--config', type=str, help='Path to configuration JSON file')
    args = parser.parse_args()

    config = DEFAULT_CONFIG.copy()
    if args.config:
        if os.path.exists(args.config):
            with open(args.config, 'r') as f:
                user_config = json.load(f)
                config.update(user_config)
            print(f"Loaded config from {args.config}")
        else:
            print(f"Config file {args.config} not found, using defaults.")
    else:
        print("No config provided, using defaults.")

    # Hyperparameters from config
    batch_size = config.get("batch_size", 16)
    epochs = config.get("epochs", 200)
    
    # Load Data
    train_loader, test_loader, _, _ = load_data(batch_size=batch_size)

    # Initialize
    model = Net()
    criterion = nn.CrossEntropyLoss()
    optimizer = get_optimizer(model, config)

    # Train
    train_losses, train_accuracies, test_accuracies = train_model(model, train_loader, test_loader, criterion, optimizer, epochs)

    # Evaluate (Final)
    evaluate_model(model, test_loader)

    # Plot
    plot_results(train_losses, train_accuracies, test_accuracies)

if __name__ == "__main__":
    main()
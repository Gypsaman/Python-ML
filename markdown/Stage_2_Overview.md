# Stage 2 — Neural Networks & Deep Learning Foundations

This stage focuses on **how neural networks are built, trained, and extended into modern deep learning architectures**. Students move from fundamental training mechanics into convolutional, generative, and attention-based models used in real-world systems.

---

## Session 1 — Neural Network Architectures Overview

### Goal

Introduce the landscape of neural network architectures and where each is used.

### Topics

* What is a neural network?
* Perceptrons vs multilayer networks
* Feedforward networks
* Convolutional Neural Networks (CNNs)
* Autoencoders
* Recurrent Networks (high-level only)
* Transformers (high-level intuition)

### Hands-On

* Visualize a simple feedforward network
* Forward pass with fixed weights
* Architecture comparison discussion

---

## Session 2 — Backpropagation and Autograd

### Goal

Understand how neural networks learn using gradients.

### Topics

* Computational graphs
* Chain rule intuition
* Gradients and partial derivatives
* Backpropagation
* PyTorch autograd system

### Hands-On

* Manual gradient calculation (1D example)
* PyTorch autograd inspection
* Visualizing gradient flow

---

## Session 3 — Loss Functions and Optimization Intuition

### Goal

Explain how error is quantified and minimized.

### Topics

* Regression vs classification loss
* Mean Squared Error
* Cross-Entropy Loss
* Loss surfaces
* Local vs global minima

### Hands-On

* Plot loss curves
* Compare losses on simple datasets
* Observe training instability

---

## Session 4 — Training Loops and Model Evaluation

### Goal

Teach the mechanics of training neural networks.

### Topics

* Epochs, batches, iterations
* Training vs inference
* Validation sets
* Overfitting vs underfitting

### Hands-On

* Write a full PyTorch training loop
* Track training/validation loss
* Introduce accuracy metrics

---

## Session 5 — Gradient Descent Variants

### Goal

Understand how optimizers affect learning dynamics.

### Topics

* Batch vs stochastic gradient descent
* Momentum
* RMSProp
* Adam optimizer
* Learning rate scheduling

### Hands-On

* Compare optimizers on same dataset
* Visualize convergence speed
* Learning rate experiments

---

## Session 6 — Weight Initialization and Activation Functions

### Goal

Explain stability and signal propagation in deep networks.

### Topics

* Vanishing/exploding gradients
* Xavier and He initialization
* Sigmoid, Tanh, ReLU, Leaky ReLU
* Dead neurons

### Hands-On

* Activation comparisons
* Gradient flow visualization
* Training instability experiments

---

## Session 7 — Regularization Techniques

### Goal

Prevent overfitting and improve generalization.

### Topics

* L1 and L2 regularization
* Dropout
* Early stopping
* Data augmentation (conceptual)

### Hands-On

* Overfit a model intentionally
* Apply regularization techniques
* Compare generalization performance

---

## Session 8 — Generalization and Representation Learning

### Goal

Build intuition about feature learning and abstraction.

### Topics

* Learned representations
* Bias–variance tradeoff
* Model capacity
* Latent spaces (intuition only)

### Hands-On

* Visualize learned feature spaces
* Compare shallow vs deep models
* Prepare groundwork for autoencoders

---

## Session 9 — Autoencoders and Variational Autoencoders

### Goal

Introduce latent variable models and generative learning.

### Topics

* Autoencoder architecture
* Encoder vs decoder
* Latent space representations
* Reconstruction loss
* Variational Autoencoders (VAE)
* KL divergence intuition
* Reparameterization trick

### Hands-On

* Train a basic autoencoder on MNIST
* Visualize latent space embeddings
* Train a VAE and sample new data
* Latent space interpolation

---

## Session 10 — Convolutional Neural Networks (CNNs)

### Goal

Teach spatial feature extraction for images.

### Topics

* Why dense layers fail for images
* Convolution operation
* Filters and feature maps
* Pooling layers
* CNN architectures
* Translation invariance

### Hands-On

* Build a CNN for MNIST or CIFAR-10
* Visualize learned filters
* Compare CNN vs fully connected models

---

## Session 11 — Transformers I: Sequences and Attention

### Goal

Introduce sequence modeling and attention mechanisms.

### Topics

* What is a sequence?
* Tokens and embeddings
* Positional encoding intuition
* Attention as weighted information routing
* Query, Key, Value concept
* Self-attention mechanism

### Hands-On

* Visualize attention weights
* Implement scaled dot-product attention
* Simple transformer block walkthrough

---

## Session 12 — Transformers II: Architecture and Applications

### Goal

Understand full Transformer architectures and modern use cases.

### Topics

* Multi-head attention
* Encoder vs decoder stacks
* Transformer training overview
* Vision Transformers (ViT)
* Large Language Models (conceptual)
* Why Transformers replaced RNNs

### Hands-On

* Build a minimal Transformer in PyTorch
* Token-level prediction task
* Inspect attention maps
* Discuss scaling and real-world deployment

---

## Summary of Stage 2

By the end of Stage 2, students will:

* Understand how neural networks learn and generalize
* Implement deep networks in PyTorch
* Build CNNs, VAEs, and Transformers
* Develop strong intuition for modern deep learning systems

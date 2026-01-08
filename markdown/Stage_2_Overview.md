# Stage 2 — Neural Networks & Deep Learning Foundations (15 Sessions)

This stage focuses on **how neural networks are built, trained, and extended into modern deep learning architectures**. Students move from training fundamentals into convolutional, generative, and attention-based models, with additional conceptual depth where abstraction increases.

---

## Session 1 — Neural Network Architectures Overview

### Goal

Introduce the landscape of neural network architectures and where each is used.

### Topics

* What is a neural network?
* Perceptrons vs multilayer networks
* Feedforward networks
* CNNs (high-level motivation only)
* Autoencoders (high-level motivation only)
* Transformers (conceptual overview)

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
* PyTorch autograd mechanics

### Hands-On

* Manual gradient calculation (1D example)
* Autograd graph inspection
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
* Observe unstable training

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

* Full PyTorch training loop
* Track training/validation loss
* Accuracy vs loss discussion

---

## Session 5 — Gradient Descent Variants

### Goal

Understand how optimizers affect learning dynamics.

### Topics

* Batch vs stochastic gradient descent
* Momentum
* RMSProp
* Adam
* Learning rate schedules

### Hands-On

* Optimizer comparison
* Convergence visualization
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
* Gradient magnitude tracking
* Failure mode demonstrations

---

## Session 7 — Regularization Techniques

### Goal

Prevent overfitting and improve generalization.

### Topics

* L1 vs L2 regularization
* Dropout
* Early stopping
* Data augmentation (conceptual)

### Hands-On

* Intentional overfitting
* Apply regularization
* Compare validation performance

---

## Session 8 — Representation Learning & Latent Spaces

### Goal

Prepare students conceptually for autoencoders and VAEs.

### Topics

* What is a representation?
* Feature compression vs information loss
* Bottleneck layers
* Geometry of learned spaces
* Latent variables (intuitive, non-probabilistic)

### Hands-On

* Visualize embeddings
* Compare shallow vs deep representations
* Dimensionality reduction intuition

---

## Session 9 — Autoencoders: Deterministic Representation Learning

### Goal

Understand how autoencoders learn compact representations.

### Topics

* Encoder–decoder structure
* Reconstruction loss
* Undercomplete vs overcomplete autoencoders
* Failure cases (identity learning)

### Hands-On

* Train autoencoder on MNIST
* Visualize reconstructions
* Inspect latent embeddings

---

## Session 10 — Variational Autoencoders (VAEs)

### Goal

Introduce probabilistic generative modeling.

### Topics

* Why deterministic autoencoders fail as generators
* Latent distributions
* KL divergence (intuitive)
* Reparameterization trick
* ELBO intuition

### Hands-On

* Train a VAE
* Sample from latent space
* Latent interpolation

---

## Session 11 — CNN Fundamentals: Convolutions & Feature Maps

### Goal

Build intuition for spatial feature extraction before full CNNs.

### Topics

* Why dense layers fail on images
* Local connectivity
* Convolution operation
* Filters and feature maps
* Stride and padding

### Hands-On

* Manual convolution visualization
* Apply custom filters
* Feature map inspection

---

## Session 12 — Convolutional Neural Networks (CNNs)

### Goal

Assemble full CNN architectures and understand invariance.

### Topics

* Pooling layers
* Hierarchical feature learning
* Translation invariance
* Classic CNN architectures

### Hands-On

* CNN for MNIST or CIFAR-10
* Visualize learned filters
* CNN vs MLP comparison

---

## Session 13 — Transformers I: Sequences and Attention

### Goal

Introduce sequence modeling and attention mechanisms.

### Topics

* Tokens and embeddings
* Positional encoding intuition
* Attention as information routing
* Query, Key, Value

### Hands-On

* Attention weight visualization
* Scaled dot-product attention
* Transformer block walkthrough

---

## Session 14 — Transformers II: Architecture and Scaling

### Goal

Understand full Transformer architectures.

### Topics

* Multi-head attention
* Encoder vs decoder stacks
* Training transformers
* Why transformers replaced RNNs

### Hands-On

* Minimal Transformer implementation
* Token-level prediction
* Attention map inspection

---

## Session 15 — Modern Deep Learning Systems & Integration

### Goal

Tie architectures together and discuss real-world systems.

### Topics

* CNNs vs Transformers
* VAEs vs diffusion models (conceptual)
* Model scaling laws
* Deployment considerations

### Hands-On

* Architecture comparison discussion
* Capstone-style model selection exercise

---

## Summary of Stage 2

By the end of Stage 2, students will:

* Understand how and why deep networks learn representations
* Build CNNs, VAEs, and Transformers in PyTorch
* Develop strong intuition for latent spaces, attention, and spatial structure
* Be prepared for advanced topics such as diffusion models, LLMs, and multimodal systems

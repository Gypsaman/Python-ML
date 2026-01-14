import torch

x = torch.randn(32,2)
w = torch.randn(2, 16)

y = x @ w
print(y.shape)
y1 = w.T @ x.T
print(y1.shape)
print(y==y1.T)
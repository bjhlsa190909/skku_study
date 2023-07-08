import numpy as np

class Sigmoid:
  def __init__(self):
    self.params = []

  def forward(self, x):
    return 1 / (1 + np.exp(-x))

class Affine:
  def __init__(self, W, b):
    self.params = [W, b]

  def forward(self, x):
    W, b = self.params
    out = np.matmul(x, W) + b
    return out

class TwoLayerNet:
  def __init__(self, input_size, hidden_size, output_size):
    I, H, O = input_size, hidden_size, output_size

    #가중치와 편향 초기화
    W1 = np.random.randn(I, H)
    b1 = np.random.randn(H)
    W2 = np.random.randn(H, O)
    b1 = np.random.randn(O)

    #계층 생성
    self.layers = [
      

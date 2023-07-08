class MatMul:
  def __init__(self):
    self.params = [W]
    self.grads = [np.zeros_like(W)]
    self.x = None

  def forward(self, x):
    W, = self.params
    out = np.matmul(x, W)
    self.x = x
    return out

  def backward(self, out):
    W, = self.params
    dx = np.matmul(dout, W.T)
    dW = np.matmul(self.x.T, dout)
    self.grads[0][...] = dW
    return dx

class Affine:
  def __init__(self, W, b):
    self.params = [W, b]
    self.grads = [np.zeros_like(W), np.zeros_like(b)]
    self.x = None

  def forward(self, x):
    W, b = self.params
    out = np.matmul(x, W) + b
    self.x = x
    return out

  def backward(self, dout):
    W, b = self.params
    dx = np.matmul(dout, W.T)
    dW = mp.matmul(self.x.T, dout)
    db = np.sum(dout, axis = 0)

    self.grads[0][...] = dW
    self.grads[0][...] = db
    return dx

def AND(x1, x2):
  x = np.array([x1, x2])
  w = np.array([0.5, 0.5])
  b = -0.7
  tmp = np.sum(x*w) + b
  if tmp <= theta:
    return 0
  elif tmp > theta:
    return 1

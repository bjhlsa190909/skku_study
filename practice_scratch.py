# class Man:
#     def __init__(self, name):
#         self.name = name
#         print("Initialized")

#     def hello(self):
#         print("Hello"+self.name+"!")

#     def goodbye(self):
#         print("Good-bye"+self.name+"!")

# m = Man("David")
# m.hello()
# m.goodbye()


import numpy as np

# x = np.array([1.0, 2.0, 3.0])

# print(x)

X = np.array([[51,55], [14, 19], [0, 4]])
# print(X[0])
X = X.flatten()
print(X)
print(X[X > 15])
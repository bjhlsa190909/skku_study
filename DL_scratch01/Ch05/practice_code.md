코드 구현하기(계층 구현)

1. 단순 곱셈 및 덧셈 계층

```python

class MulLayer:
    def __init__(self):
        self.x = None
        self.y = None

    def forward(self, x, y):
        self.x = x
        self.y = y
        out = x * y

        return out
    
    def backward(self, dout):
        dx = dout * self.y
        dy = dout * self.x

        return dx, dy
    
class AddLayer:
    def __init__(self):
        pass          #

    def forward(self, x, y):
        out =  x + y

        return out
    
    def backward(self, x, y):
        dx = dout * 1
        dy = dout * 1

        return dx, dy
    
   



코드 구현하기(계층 구현)
------------------------

1. 단순 곱셈 및 덧셈 계층

```python

class MulLayer:
    def __init__(self):
        self.x = None    # forward 메서드에서 입력으로 받은 x와 y를 저장해 둔 다음 backward에서 사용.
        self.y = None    # 즉, 이전에 저장된 값을 다음 계산에서 사용하기 위해 클래스 속성으로 선언됨.

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
        pass          #backward에 있어 특별히 기억될 내용 없기 때문에 pass사용

    def forward(self, x, y):
        out =  x + y

        return out
    
    def backward(self, x, y):
        dx = dout * 1
        dy = dout * 1

        return dx, dy
```
2. 계층 활용(사과와 오렌지 구입 예시)

```python

apple = 100
apple_num = 2
orange = 150
orange_num = 3
tax = 1.1

# 위에서 구현한 곱셈과 덧셈에 대한 클래스의 인스턴스 값을 만듦.

mul_apple_layer = MulLayer()
mul_orange_layer = MulLayer()
add_apple_orange_layer = AddLayer()
mul_tax_layer = MulLayer()

#forward
apple_price = mul_apple_layer.forward(apple, apple_num)
orange_price = mul_orange_layer.forward(orange, orange_num)
all_price = add_apple_orange_layer.forward(apple_price, orange_price)

#backward(역전파_MulLayer에 대한 backward는 해당 클래스의 메소드에 나오듯이, 각자 변수에 대한 편미분 값을 구하는 것이기에 dout에 곱하는 값을 서로 바꿔줌)
dprice = 1
dall_price, dtax = mul_tax_layer.backward(dprice)
dapple_price, dorange_price = add_apple_orange_layer.backward(dall_price)
dorange, dorange_num = mul_orange_layer.backward(dorange_price)
dapple, dapple_num = mul_apple_layer.backward(dapple_price)

print("price:", int(price))
print("dApple:", dapple)
print("dApple_num:", int(dapple_num))
print("dOrange:", dorange)
print("dOrange_num:", int(dorange_num))
print("dTax:", dtax)

```
3. 활성화 함수 구현(Relu, Sigmoid)

```python

class Relu:
    def __init__(self):
        self.mask = None
        
    def forward(self, x):
        self.mask = (x <= 0)    # mask라는 인스턴스 변수를 설정. x값이 0이하는 False, 0이상은 True를 유지함. 
        out = x.copy()          # x배열 자체를 직접 조작하지 않고, 복사된 배열을 이용& 중간 계산 결과를 저장하기 위해서임. 
        out[self.mask] = 0
        
        return out
    
    def backward(self, dout):
        dout[self.mask] = 0
        dx = dout
        
        return dx

class Sigmoid:
    def __init__(self):
        self.out = None
    
    def forward(self, x):
        out = 1 / (1 + np.exp(-x))
        self.out = out
        
        return out
        
    def backward(self, dout):
        dx = dout * (1.0 - self.out) * self.out    # 하기 5-22에서 나오는 것을 구현한 것임.
        
        return dx
```

<img width="291" alt="fig 5-22" src="https://user-images.githubusercontent.com/125746059/232256326-714b480f-1289-4751-aa0c-a8ca2157fa1e.png">

4. Affine/Softmax 계층 구현

기본적인 신경망 순전파의 흐름이 가중치 신호의 총합(Y=np.dot(X, W) + B)을 활성화함수(sigmoid, relu 등)로 변환하여 다음 층으로 전파하는 것이고, 여기서 수행되는 행렬의 곱이 어파인의 기본적인 concept임. 

```python

class Affine:
    def __init__(self, W, b):
        self.W = W
        slef.b = b
        self.x = x
        self.dW = None
        self.db = None
        
    def forward(self, x):
        self.x = x    # 중간 연산 결과 값들을 그때마다 기억하는 과정
        out = np.dot(x, self.W) + self.b
        
        return out
        
    def backward(self, dout):
        dx = np.dot(dout, self.W.T)    # T는 주어진 행렬을 전치행렬로 바꾸는 역할.
        self.dW = np.dot(self.x.T, dout)
        self.db = np.sum(dout, axit = 0)
        
        return dx

class SoftmaxWithLoss:
    def __init__(self):
        self.loss = None
        self.y = None    # softmax 출력값
        self.t = None    # 정답 레이블(t)(원-핫 벡터)
        
    def forward(self, x, t):
        self.t = t
        self.y = softmax(x)    
        self.t = cross_entropy_error(self.y, self.t)
        return self.loss
        
    def backward(self, dout=1):
        batch_size = self.t.shape[0]    
        dx = (self.y - self.t) / batch_size
        
        return dx
        
```




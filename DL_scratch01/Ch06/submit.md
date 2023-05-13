6장 학습 관련 기술들
--------------------

6.1 매개변수 갱신
- 신경망 학습의 목적은 손실 함수의 값을 가능한 낮추는 매개변수 찾는 것임(매개변수의 최적값을 찾는 문제_ 최적화)
- 앞서 학습한 방법론은 확률적 경사 하강법(SGD)였음(매개변수의 기울기를 구해 기울어진 방향으로 값을 갱신하는 일을 반복해서 최적값을 찾는 방법)

<img width="190" alt="e 6 1" src="https://user-images.githubusercontent.com/125746059/236435769-7e07f523-08b7-49ea-bbcc-5735763a565a.png">

<코드 구현>

```python

class SGD:
    def __init__(self, lr = 0.01):
        self.lr = lr
    def update(self, params, grads):
        params[key] = -= self.lr * grads[key]
        
    # params, grads는 가중치 매개변수와 기울기를 저장하고 있는 딕셔너리 변수임.
```

- SGD는 단순하고 구현도 쉽지만, 문제에 따라서는 비효율적인 경우가 있음.특히, 비등방성(anisotropy) 함수에서는 탐색경로가 비효율적임. 

<img width="400" alt="fig 6-3" src="https://user-images.githubusercontent.com/125746059/236436904-1a20580b-507b-43e4-b44a-74fa4943b2d3.png">

- 이러한 SGD의 문제를 개선해주는 세 방법(모멘텀, AdaGrad, Adam) 등이 있음. 

1) 모멘텀

<img width="161" alt="e 6 3" src="https://user-images.githubusercontent.com/125746059/236437478-4f5a52e0-12f2-46fd-93a0-b6c61147b718.png">

나머지 변수는 SGD와 동일하나 v라는 변수가 추가됨. 여기서 av항은 매개변수의 조정치가 급격히 변하는 것을 막아주는 역할을 함. 

<img width="400" alt="fig 6-5" src="https://user-images.githubusercontent.com/125746059/236438810-8c95aac4-1d03-4b84-a3a8-b2092ed291af.png">

모멘텀의 갱신 경로는 공이 그릇 바닥을 구르듯 움직이며, 이는 SGD와 비교하면 지그재그 정도가 덜 한 것을 확인할 수 있음. 

<코드 구현>

```python

class Momentum:
    def __init__(self, lr = 0.01, momentum = 0.9):
        self.lr = lr
        self.momentum = momentum
        self.v = None
        
    def update(self, params, grads):
        if self.v is None:
            self.v = {}
            for key, val in params.items():
                self.v[key] = np.zeros_like(val)
        for key in params.keys():
            self.v[key] = self.momentum * self.v[key] - self.lr * grads[key]
            params[key] += self.v[key]
            
```

2) AdaGrad

신경망 학습에서는 학습률 값이 중요한데, 이 값이 너무 작으면 학습 시간이 길어지고 너무 크면 발산하여 학습이 제대로 이뤄지지 않음. 

학습률 감소(learning rate decay)라는 방법은 처음에는 크게 학습하다가 조금씩 작게 학습하는 방법으로 학습 진행에 따라 학습률을 점차 줄여가는 방법임. 

<img width="189" alt="e 6 5" src="https://user-images.githubusercontent.com/125746059/236440444-87927c99-3757-4295-abb9-4d66bc6213fb.png">

<img width="198" alt="e 6 6" src="https://user-images.githubusercontent.com/125746059/236440452-07c6fb3d-fb33-46ca-8e6c-34a1db14e15d.png">

상기 식에서는 h라는 변수가 나오는데, 이는 기존 기울기 값을 제곱하여 계속 더해주고, 매개변수를 갱신할 때 h의 제곱근을 -1승 하여 학습률을 조정함. 이는 매개변수 원소 중 많이 갱신된 원소는 학습률이 낮아진다는 뜻으로, 학습률 감소가 매개변수의 원소마다 다르게 적용됨을 의미함. 

<코드 구현> 

```python
class AdaGrad:
    def __init__(self, lr = 0.01):
        self.lr = lr
        self.h = None
        
    def update(self, params, grads):
        if self.h is None:
            self.h = {}
            for key, val in params.items():
                self.h[key] = np.zeros_like(val)
                
        for key in params.keys():
            self.h[key] += grads[key] * grads[key]
            params[key] -= self.lr * grads[key] / (np.sqrt(self.h[key] + 1e-7)
            
```
<img width="400" alt="fig 6-6" src="https://user-images.githubusercontent.com/125746059/236441910-2c015d46-5a42-42c5-ab9b-db3545266753.png">

3)Adam

모멘텀과 AdaGrad 두 기법을 융합하여 적용한 방법임. 

4) MNIST 데이터셋으로 본 갱신 방법 비교

<img width="400" alt="fig 6-9" src="https://user-images.githubusercontent.com/125746059/236442505-4286b2b5-becc-474c-ab52-0bf5feceae3f.png">

상기 결과를 보면 SGD의 학습 진도가 가장 느리고 나머지 세 기법의 진도는 비슷함. 일반적으로 SGD보다 다른 세 기법이 빠르게 학습하고, 떄로는 최종 정확도도 높게 나타남. 

6.2 가중치의 초기값

hidden layer(은닉층)의 분포를 관찰하여 가중치의 초기값에 따라 활성화 값이 어떻게 변화하는지 살펴보면 하기와 같이 구현됨.

```python

import numpy as np
import matplotlib.pyplot as plt

def sigmoid(x):
    return 1 / (1 + np.exp(-x))  # 은닉층의 활성화함수로 시그모이드 사용
    
x = np.random.randn(1000, 100) # 1000 x 100 의 입력데이터(난수_정규분포) 생성
node_num = 100
hidden_layer_size = 5
activations = {}

for i in range(hidden_layer_size):
    if i != 0:
        x = activations[i-1]
        
    w = np.random.randn(node_num, node_num) * 1 # 표준편차가 1인 경우 상정
        
    a = np.dot(x, w)
    z = sigmoid(a)
    activations[i] = z

for i, a in activations.items():
    plt.subplot(1, len(activations), i+1)
    plt.title(str(i+1) + "-layer")
    plt.hist(a.flatten(), 30, range=(0,1))

```
![image](https://github.com/bjhlsa190909/skku_study/assets/125746059/59dc9266-18b3-4f02-bd14-018200192d82)

각 층의 활성화 값들이 0와 1에 치우쳐 분포되는 모양새를 보임(시그모이드 함수의 출력값이 0에 가까워지자 그 미분은 0에 다가감_기울기 소실문제)

위에서 구현한 값 중에 가중치에 곱해진 표준편차를 0.01로 수정하여 그래프를 표현하면 아래와 같음.

![image](https://github.com/bjhlsa190909/skku_study/assets/125746059/1bf47e96-187c-4c25-b50a-3dfb08ad066d)

0.5 부근에 집중된 값의 분포를 보여 기울기 소실 문제가 발생하지 않았으나 표현력 관점에서 문제가 있음(뉴런을 여러개로 둔 의미가 없어짐)

Xavier초기값 사용(일반적인 딥러닝 프레임워크에서 표준적으로 이용하고 있음)
>> 이 초기값을 표현한 논문에서는 각 층의 활성화 값들을 광범위하게 분포시킬 목적으로 가중치의 적절한 분포를 찾고자 하였으며, 앞 계층의 노드가 n개라면 표준편차가 1 / np.sqrt(n) 이라는 결론을 이끌어 냄. 

![image](https://github.com/bjhlsa190909/skku_study/assets/125746059/f9704f85-ce99-4d00-8760-8a0495dd5d4a)

<img width="400" alt="fig 6-12" src="https://github.com/bjhlsa190909/skku_study/assets/125746059/d5127a40-e257-4d45-807d-12013ff2ea14">

Relu를 활성화 함수로 사용할 떄의 초기값은 주로 He 초기값을 이용함. He초기값은 앞 계층의 노드 개수가 n개 일때, 표준편차가 2 / np.sqrt(n) 을 사용하는데, 이는 Relu함수가 음의 영역에서 0이라 더 넓게 분포시키기 위해 2배의 계수를 사용하는 것으로 해석될 수 있음. 

6.2.4 MNIST 데이터셋으로 본 가중치 초기값 비교

<img width="400" alt="fig 6-15" src="https://github.com/bjhlsa190909/skku_study/assets/125746059/7fcfaa3e-3afb-4265-aaec-528654db9fcf">

std가 0.01인 경우에는 학습이 거의 이뤄지지 않았고, Xavier나 He 초기값은 학습이 순조롭게 이뤄짐.

6.3 배치 정규화

기본적인 아이디어는 각 층에서의 활성화 값이 적당히 분포되도록 조정하는 것에 있음. 

장점
학습 속도 개선, 초기 값에 크게 의존하지 않음, 오버피팅 억제(드롭아웃 필요성 감소) 

<img width="647" alt="fig 6-16" src="https://github.com/bjhlsa190909/skku_study/assets/125746059/232f0ee9-845a-4e85-96db-47cf05f77dbb">

결과적으로 각 미니배치의 입력 데이터를 평균 0, 분산 1인 데이터로 변환하는 작업을 수행하여 데이터 분포가 덜 치우치도록 함(이 처리를 활성화 함수의 앞 또는 뒤 중 어디에 넣을지에 대한 논의와 실험 진행중)

<img width="300" alt="e 6 7" src="https://github.com/bjhlsa190909/skku_study/assets/125746059/6296da4c-7270-404f-b2ea-98bf346d9f37">

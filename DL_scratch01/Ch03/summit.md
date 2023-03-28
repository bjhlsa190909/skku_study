3.1 신경망
---------  
  3.1.1 신경망의 예
  
<img width="300" height="300" alt="fig 3-1" src="https://user-images.githubusercontent.com/125746059/224335385-5d487187-9877-4872-b431-790fbbb04505.png">
 
여기에서 왼쪽 줄을 입력층, 중간 줄을 은닉층, 맨 오른쪽 줄을 출력층으로 부름. 
 
  3.1.2 퍼셉트론 복습
 
<img width="300" height="300" alt="fig 3-3" src="https://user-images.githubusercontent.com/125746059/224335973-93a69933-9968-493b-bd91-e5b4f8348e22.png">

 뉴런이 얼마나 쉽게 활성화 되느냐를 제어하는 편향 b를 포함시킨 퍼셉트론 수식은 아래와 같음. 
 
 <img width="295" alt="e 3 1" src="https://user-images.githubusercontent.com/125746059/224336959-0a30a1d4-2fae-48fb-a765-569f1ad4011f.png">

 상기의 식에서 드러나는 퍼셉트론 동작법은 x1, x2, 1이라는 3개의 신호가 뉴런에 입력되어 각 신호에 가중치를 곱한 후 다음 뉴런에 전달되고, 다음 뉴런에서는 이 신호들의 값을 더하여 합이 0을 넘으면 1을 출력함. 
 
 3.1.3 활성화 함수 등장
 
 활성화 함수란 입력 신호의 총합이 활성화를 일으키는지를 정하는 역할을 수행함. 
 
 <img width="300" height="300" alt="fig 3-4" src="https://user-images.githubusercontent.com/125746059/224338110-77097171-1fd0-49d9-a62b-384f010b6868.png">
 
 위 그림은 가중치 신호를 조합한 결과가 a라는 노드가 되고, 활성화 함수 h()를 통과하여 y라는 노드로 변환되는 과정을 보여줌. 
 
 3.2 활성화 함수
 --------------
 3.2.1 시그모이드 함수
 
 <img width="198" alt="e 3 6" src="https://user-images.githubusercontent.com/125746059/224338699-307912b7-feb8-4413-84cf-1147af19f3b9.png">

 신경망에서 자주 이용하는 활성화 함수로서 exp(-x)는 자연상수 e에 대한 지수함수를 의미함. 
 
 또한 활성화 함수로 시그모이드 함수를 이용하여 신호를 변환하고, 그 변환된 신호를 다음 뉴런에 전달함. 
 
 3.2.2 계단 함수 구현하기 
 
 3.2.3 계단 함수의 그래프 
 
 <img width="300" height="300" alt="fig 3-6" src="https://user-images.githubusercontent.com/125746059/224339799-b89566ba-0a25-4a18-aeab-8531c6f9c10a.png">

3.2.4 시그모이드 함수 구현하기 

 <img width="300" height="300" alt="fig 3-7" src="https://user-images.githubusercontent.com/125746059/224340247-6d7a1e99-b6db-4603-bb33-9b806e1cc916.png">

 3.2.5 시그모이드 함수와 계단함수 비교
 
 <img width="300" height="300" alt="fig 3-8" src="https://user-images.githubusercontent.com/125746059/224340697-c186a0e9-6e62-453b-af4d-c6b27bd85e67.png">
 
 공통점 : 입력이 작을 때의 출력은 0에 가깝고, 입력이 커지면 출력이 1에 가까워지는 구조임(즉, 두 함수는 입력이 중요하면 큰 값을 출력하고 그렇지 않으면 작은 값을 출력함)
 차이점 : 그래프의 매끄러움, 출력값의 형태가 다름(계단 함수는 0과 1을 출력하는 반면, 시그모이드 함수는 연속적인 실수가 흐름)
 
 3.2.6 비선형 함수
 
 신경망에서는 층을 깊게 해야하므로 활성화 함수로 비선형 함수를 사용해야 함. (계단 함수도 비선형 함수임)
 
 3.2.7 RELU 함수
 
 RELU(Rectified Linear Unit)함수는 입력이 0 이하이면 0을 출력하고 0을 넘으면 그 입력을 그대로 출력함. 
 
 <img width="300" alt="fig 3-9" src="https://user-images.githubusercontent.com/125746059/224449100-a35e16ee-e527-4ee6-882c-385371728ca9.png">

 <img width="200" alt="e 3 7" src="https://user-images.githubusercontent.com/125746059/224449157-d977e728-aac1-47bd-b75b-dc4b720c2edb.png">

 3.3 다차원 배열의 계산
 ---------------------
 3.3.1 다차원 배열
 
 한 줄로 늘어선 것, 직사각형, 3차원으로 늘어놓은 것 등 N차원으로 나열하는 것 통틀어 다차원 배열이라 함. 
 (특히 2차원 배열은 행렬matrix라고 부름)
 
 3.3.2 행렬의 곱
 
 <img width="300" alt="fig 3-12" src="https://user-images.githubusercontent.com/125746059/224451123-fbd5bffe-6483-4aa7-af1e-64661f1b0bed.png">

 행렬의 곱에서는 대응하는 차원의 원소 수를 일치시켜야 함. 
 
 <img width="300" alt="fig 3-13" src="https://user-images.githubusercontent.com/125746059/224451213-e238d8c1-b74f-4bf9-8218-96700a516474.png">

 상기에서 A가 2차원 행렬, B가 1차원 배열일 때에도 대응하는 차원의 원소 수를 일치시켜야함. 
 
 3.3.3 신경망에서의 행렬 곱
 
 <img width="400" alt="fig 3-14" src="https://user-images.githubusercontent.com/125746059/224462928-5f0f0ad6-cc80-43f8-85ec-f02c4cfbc7dd.png">

 3.4 3층 신경망 구현하기
 -----------------------
 <img width="300" alt="fig 3-15" src="https://user-images.githubusercontent.com/125746059/224462960-9c719b42-adec-4ebe-a69c-101ae47f172c.png">

 3.4.1 표기법 설명
 
 <img width="300" alt="fig 3-16" src="https://user-images.githubusercontent.com/125746059/224463033-fca22040-e22f-4891-97ab-09fad440b5ea.png">

 
3.4.2 각 층의 신호 전달 구현하기 

<img width="400" alt="fig 3-17" src="https://user-images.githubusercontent.com/125746059/224463120-7e31bd12-f260-4376-9d57-b4a3d8a6a8af.png">

<img width="300" alt="e 3 8" src="https://user-images.githubusercontent.com/125746059/224463176-13e90a44-3b54-4d63-8163-c26134b8ca86.png">

<img width="300" alt="e 3 9" src="https://user-images.githubusercontent.com/125746059/224463183-65517481-e7c5-4faa-a401-59f25d369b69.png">

 첫번째 식은 입력을 받아 가중치를 곱한 a1 노드 의 값을 의미하며, 1층의 가중치 부분을 두번째 식과 같이 간소화 할 수 있음. 
 
 <img width="300" alt="fig 3-18" src="https://user-images.githubusercontent.com/125746059/224463360-4f0bcccf-50d5-4416-829c-33ab4539bd28.png">
 
 위 그림은 입력층에서 1층으로의 신호 전달을 표현하고 있으며, 하단의 그림은 1층에서 2층으로의 신호전달을 나타내고 있음.(활성화 함수로 시그모이드 함수 이용) 
 
 <img width="300" alt="fig 3-19" src="https://user-images.githubusercontent.com/125746059/224463397-34b19e17-577f-4ade-ba5a-f18737f23e91.png">

<img width="300" alt="fig 3-20" src="https://user-images.githubusercontent.com/125746059/224463473-1784cc54-eb4c-425e-8ff1-3aab0a794535.png">

 2층에서 출력층으로의 신호 전달을 위 그림은 표현하고 있고, 기존 층들에서 이뤄졌던 것과의 유일한 차이점은 활성화 함수가 다르다는 것임.
 (출력층의 활성화 함수는 문제의 성질에 따라 다르게 정함. 예를 들어, 회귀에서는 항등함수를, 2클래스 분류에는 시그모이드 함수를, 다중 클래스 분류에는 소프트맥스 함수를 사용하는 것이 일반적임)
 
 3.4.3 구현 정리 
 
 3.5 출력층 설계하기
 -------------------
 신경망은 분류와 회귀 모두에 이용될 수 있으며, 일반적으로 회귀에는 항등함수, 분류에는 소프트맥스 함수를 사용함. 
 
 3.5.1 항등 함수와 소프트맥스 함수 구현하기 
 
 <img width="300" alt="fig 3-21" src="https://user-images.githubusercontent.com/125746059/224464198-13ef0f7b-b9e0-4b13-9946-00e5271bdea7.png">

 소프트맥스 함수 식
 
 <img width="300" alt="e 3 10" src="https://user-images.githubusercontent.com/125746059/224464230-a3a88278-6fdc-4000-8a25-6ee77d3431c5.png">

 exp(x)는 자연상수 e의 지수함수를, n은 출력층의 노드의 수, yk는 그 중 k번쨰 출력임을 의미함. 즉, 소프트맥스 함수의 분자는 입력 신호 ak의 지수 함수, 분모는 모든 입력 신호의 지수 함수의 합으로 구성됨. 
 
 <img width="300" alt="fig 3-22" src="https://user-images.githubusercontent.com/125746059/224464315-6c5ed0c7-4dd9-4ca3-af85-c734f22034f6.png">

 3.5.2 소프트맥스 함수 구현시 주의점
 
 앞서 구현한 softmax() 함수 코드는 지수함수를 사용하기에 컴퓨터로 계산시 오버플로 문제가 발생하여 수치가 불안정해지는 문제가 발생함. 
 
 이 문제를 해결하도록 소프트맥스 함수 구현을 개선해보고자 함. 
 
 <img width="300" alt="e 3 11" src="https://user-images.githubusercontent.com/125746059/224464649-4bcc7642-9e6f-4202-a71b-fbd1cf3481f6.png">
 
 3.5.3 소프트맥스 함수의 특징
 
 소프트맥스 함수의 출력은 0에서 1.0 사이의 실수이고, 출력의 총합은 1임. (소프트맥스 함수의 중요한 성질)
 
 즉, 입력 값에 대응되는 출력값에 대해 확률적인 결론을 낼 수 있으므로 문제에 따라 통계적 대응이 가능하게 됨. 
 (단, 소프트맥스 함수를 적용해도 지수함수의 단조증가함수로서의 특성상 각 원소의 대소 관계는 변하지 않음)
 
 3.5.4 출력층의 뉴런 수 정하기 
 
 출력층의 뉴런 수는 풀려는 문제에 맞게 정해야하고, 분류에서는 분류하고 싶은 클래스 수로 설정하는 것이 일반적임. 
 
 
3.6 손글씨 숫자 인식
--------------------
기계학습과 마찬가지로 신경망도 두 단계를 거쳐 문제를 해결하는데, 특히 추론 과정을 신경망의 순전파(forward propagation)이라고 함. 

3.6.1 MNIST 데이터셋
<img width="300" alt="fig 3-24" src="https://user-images.githubusercontent.com/125746059/224465480-9e44a49f-78f9-4646-8ee6-db9f063ff15c.png">


 

 
 

 
 

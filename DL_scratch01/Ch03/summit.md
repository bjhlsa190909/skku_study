<details>
<summary>3장 신경망</summary>
 
3.1 신경망
---------  
  3.1.1 신경망의 예
  
<img width="60%" height="300" alt="fig 3-1" src="https://user-images.githubusercontent.com/125746059/224335385-5d487187-9877-4872-b431-790fbbb04505.png">
 
여기에서 왼쪽 줄을 입력층, 중간 줄을 은닉층, 맨 오른쪽 줄을 출력층으로 부름. 
 
  3.1.2 퍼셉트론 복습
 
<img width="60%" height="300" alt="fig 3-3" src="https://user-images.githubusercontent.com/125746059/224335973-93a69933-9968-493b-bd91-e5b4f8348e22.png">

 뉴런이 얼마나 쉽게 활성화 되느냐를 제어하는 편향 b를 포함시킨 퍼셉트론 수식은 아래와 같음. 
 
 <img width="295" alt="e 3 1" src="https://user-images.githubusercontent.com/125746059/224336959-0a30a1d4-2fae-48fb-a765-569f1ad4011f.png">

 상기의 식에서 드러나는 퍼셉트론 동작법은 x1, x2, 1이라는 3개의 신호가 뉴런에 입력되어 각 신호에 가중치를 곱한 후 다음 뉴런에 전달되고, 다음 뉴런에서는 이 신호들의 값을 더하여 합이 0을 넘으면 1을 출력함. 
 
 3.1.3 활성화 함수 등장
 
 활성화 함수란 입력 신호의 총합이 활성화를 일으키는지를 정하는 역할을 수행함. 
 
 <img width="60%" height="300" alt="fig 3-4" src="https://user-images.githubusercontent.com/125746059/224338110-77097171-1fd0-49d9-a62b-384f010b6868.png">
 
 위 그림은 가중치 신호를 조합한 결과가 a라는 노드가 되고, 활성화 함수 h()를 통과하여 y라는 노드로 변환되는 과정을 보여줌. 
 
 3.2 활성화 함수
 --------------
 3.2.1 시그모이드 함수
 
 <img width="198" alt="e 3 6" src="https://user-images.githubusercontent.com/125746059/224338699-307912b7-feb8-4413-84cf-1147af19f3b9.png">

 신경망에서 자주 이용하는 활성화 함수로서 exp(-x)는 자연상수 e에 대한 지수함수를 의미함. 
 
 또한 활성화 함수로 시그모이드 함수를 이용하여 신호를 변환하고, 그 변환된 신호를 다음 뉴런에 전달함. 
 
 3.2.2 계단 함수 구현하기 
 
 3.2.3 계단 함수의 그래프 
 
 <img width="60%" height="300" alt="fig 3-6" src="https://user-images.githubusercontent.com/125746059/224339799-b89566ba-0a25-4a18-aeab-8531c6f9c10a.png">

3.2.4 시그모이드 함수 구현하기 

 <img width="60%" height="300" alt="fig 3-7" src="https://user-images.githubusercontent.com/125746059/224340247-6d7a1e99-b6db-4603-bb33-9b806e1cc916.png">

 3.2.5 시그모이드 함수와 계단함수 비교
 
 <img width="60%" height="300" alt="fig 3-8" src="https://user-images.githubusercontent.com/125746059/224340697-c186a0e9-6e62-453b-af4d-c6b27bd85e67.png">

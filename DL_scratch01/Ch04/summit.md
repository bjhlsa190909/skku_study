4. 신경망 학습
--------------

4.1.1 데이터 주도 학습

<img width="400" height = '300' alt="fig 4-2" src="https://user-images.githubusercontent.com/125746059/229109804-2d041d40-0acb-49ec-bedb-d6db604c55cf.png">

기계학습의 경우 주어진 데이터에서 feature값을 추출하고 그 특징의 패턴을 기계가 학습하는 방법을 취하나, 신경망의 경우 데이터를 '있는 그대로' 학습하여 문제의 패턴을 찾아내려고 함. 

4.1.2 훈련 데이터와 시험 데이터

기계학습의 문제는 training data 와 test data로 나누어 학습과 실험을 수행하는게 일반적임(범용 능력을 제대로 평가하기 위함)

* 용어 설명 > 오버 피팅(overfitting) : 한 데이터 셋에만 지나치게 최적화되어 다른 데이터 셋에 대한 학습과 예측에는 신뢰도가 낮은 상태

4.2 손실 함수

손실함수는 신경망 성능의 '나쁨'을 나타내는 지표로, 현재의 신경망이 훈련 데이터를 얼마나 잘 처리하지 못하느냐를 나타냄. 

4.2.1 오차제곱합

<img width="175" alt="e 4 1" src="https://user-images.githubusercontent.com/125746059/229112975-2e455697-7c38-4306-83cd-b3515d6ccaa2.png">

(yk는 신경망이 추정한 값, tk는 정답레이블, k는 데이터의 차원 수)

4.2.2 교차 엔트로피 오차

<img width="169" alt="e 4 2" src="https://user-images.githubusercontent.com/125746059/229115249-3c305647-15ab-477e-bfca-0fa1489a8ddc.png">

<img width="400" height='300 alt="fig 4-3" src="https://user-images.githubusercontent.com/125746059/229115824-ef7b69a6-d6d1-4fd3-99fa-089bf028e32c.png">
                         
교차 엔트로피 오차 또한 정답일 때의 출력(yk)이 전체 값을 결정하게 되고, 정답에 해당하는 yk값이 작을수록 오차는 커지게 됨. 
                         
                         







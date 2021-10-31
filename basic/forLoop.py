#반복문 - for
#for 문은 반복 횟수 또는 범위를 지정해 명령어를 반복 수행합니다.
#for문은 다음과 같은 구조로 사용됩니다.

#for 변수 in 반복횟수/범위 :
#    수행할 명령

#반복 횟수 지정하기 - range()
#range() 함수를 이용해 반복 횟수를 정할 수 있습니다.
#이 때, 특수한 변수를 사용할 수 있는데, 이 변수는 해당 명령어가 몇번째로 수행되고 있는지
#수로 저장되는 변수입니다. 이때, 순서는 0부터 세는 것에 주의하세요
for i in range(10) : # i라는 이름으로 특수한 변수를 만듭니다.
    print(i) #변수 i는 명령어가 몇번쨰로 수행되고 있는지를 수로 저장합니다.

for a in range(10) : #변수 이름은 자유롭게 정할 수 있습니다.
    print(a) 

#range(시작, 끝)의 형식으로 수를 두 개 넣으면 처음에 시작되는 수를 정할 수 있습니다.
#이 때 순서는 시작 에서부터 끝-1 까지 저장됩니다.
for i in range(3, 6) :
    print(i) #3부터 5까지가 출력됩니다.

#문제
#1. 1부터 10까지 for를 이용해 출력하세요

#2. 10부터 20까지 for를 이용해 출력하세요

#for와 리스트
#for문에 range() 대신 리스트를 넣어서 작동시킬 수 있습니다.
#이 때도 range()와 마찬가지로 특수한 변수를 사용할 수 있는데, 
# 이때는 순서가 아닌 리스트의 값을 차례대로 하나씩 가져옵니다.
for i in [2,4,6,8] :
    print(i) #리스트 안의 값을 차례대로 출력합니다.


#문제
#1. 다음 리스트에 저장되어 있는 값을 차례대로 출력하세요
ls = [1,2,3,4,5,6,7]

#2. @@@라고 써진 부분을 수정해 1 2 4 8 16이 차례대로 출력되도록 하세요
for i in @@@ :
    print(i)
tinkerefftt
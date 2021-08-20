# 81) 소수의 개수
# 2에서 1백만 사이의 수중 소수는 모두 몇 개일까요?

# 우리가 전에 풀었던 에라토스테네스의 체를 이용하면 쉽게 구할 수
# 있을 것입니다.

#1백만까지의 수를 저장하기 위한 코드
numbers = [0,0]
for i in range(2, 1000001) :
    numbers.append(i)

#여기에 문제를 해결할 코드를 짜 주세요
count= 0
for i in range(2, 1000001) :
    if(numbers[i] != 0) :
        count += 1
        idx = i
        numbers[i] = 0
        while idx <= 1000000 :
            numbers[idx] = 0
            idx += i
print(count)
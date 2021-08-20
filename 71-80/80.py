# 80) 제곱의 개수
# 2 <= a <= 100 이고
# 2 <= b <= 100 인 두 수 a, b에 대하여
# 가능한 a**b의 개수는 모두 몇 개일까요?
# 중복은 제외하여야 합니다.

#여기에 문제를 해결하고 결과를 출력하는 코드를 입력해 주세요
ls=[]
for i in range(2,101):
    for x in range(2,101):
        if i**x not in ls:
            ls.append(i**x)
print(len(ls))
        


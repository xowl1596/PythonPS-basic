# 47을 뒤집으면 74가 나오고 이를 원래 수에 더하면
# 47 + 74 = 121로 대칭수가 나옵니다.
# (대칭수 : 거꾸로 수를 읽어도 원래 수와 똑같은 수)

# 대부분의 수는 위 과정을 여러 번 거쳐야 대칭수가 나오는데,
# 예를 들어 349의 경우
# 349 + 943 = 1292
# 1292 + 2921 = 4213
# 4213 + 3124 = 7337
# 위와 같이 3번의 과정을 거쳐야 대칭수가 나옵니다.

# 하지만 196과 같이 위 과정을 몇번을 거치든 대칭수가 나오지
# 않을 것이라고 추측되는 수가 있는데, 이러한 수를
# 라이크렐 수라고 합니다.
# 아직은 증명되지 않았지만, 이 문제에서는 라이크렐 수가
# 존재한다고 가정하겠습니다.

# 또, 1에서 10000까지의 수는 50번 미만의 과정을 통해 대칭수가
# 나오는지 라이크렐 수인지 판단할 수 있다고 합니다.

# 1에서 10000까지의 수중 라이크렐 수는 몇 개입니까?

#문제풀이를 위한 힌트입니다.
def isPalindrome(a) : #수 a가 대칭수인지 확인하는 함수.
    s = str(a)
    idx = 0
    check = True

    while idx <= int(len(s)/2): 
        if s[idx] != s[len(s)-(1+idx)] :
            check = False
            break
        idx += 1

    return check

#여기에 문제를 해결하는 코드를 입력하세요
count = 0

for i in range(1, 10001) :
    num = str(i)

    check = True

    for i in range(49) :
        reversedNum = num[::-1]

        num = int(num) + int(reversedNum)

        if isPalindrome(num) :
            check = False
            break
    
    if check :
        count += 1

print(count)


    
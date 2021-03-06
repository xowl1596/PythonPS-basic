#문자 다루기

#문자 데이터에서 특정 글자 가져오기
#변수[i] 를 이용해 문자의 i번째 글자만 가져올 수 있습니다.
#이 때, 문자의 순서는 0부터 시작함에 주의하세요
a = "abcdefg"
print(a[0]) #> a
print(a[3]) #> d

#변수[i:j]를 이용하면 문자의 i번째부터 j-1번째 글자까지 가져옵니다.
print(a[2:5]) #>cde

#문제 
#1. 다음 변수에서 3번째(저)와 6번째(공백) 글자만 출력하세요
a = "오늘 저녁은 치킨이다"

#2. 위 a변수에서 치킨만 출력하세요

#replace 함수를 이용하면 특정 문자들을 다른 문자로 바꿀 수 있습니다.
a = "12333456"
a = a.replace("3", "1") #a에 저장된 문자에서 모든 3을 1로 바꿉니다.
a = a.replace("1", "") #a에 저장된 문자에서 모든 1을 없앱니다.
print(a) #> 2456

#문제
#1. 아래 변수에서 -을 공백으로 바꾸고 출력하세요
a = "010-1234-1234"

#2. 아래 변수에서 /을 없애고 출력하세요
a = "2021/10/31"

#split함수를 이용하면 특정 문자를 기준으로 문자를 쪼개고 리스트로 만듭니다.
a = "a,b,c,d"
a = a.split(",")
print(a) #> [a,b,c,d]

#문제
#1. 다음 문자열에서 split을 이용해 com만 출력하세요
url = "http://www.naver.com"

#문자열을 +를 이용해 합칠 수 있습니다.
a = "He"
b = "llo"
c = a + b
print(c) #> Hello

#문제
#1. 다음 변수를 이용해 24를 출력하세요
a = "2"
b = "4"

#문자열에 정수를 곱해 반복시킬 수 있습니다.
a = "abc"
b = a * 3
print(b) #> abcabcabc

#문제
#1. 다음 변수를 이용해 Hi를 3번 출력하세요
a = "Hi"

#2. -을 80개 출력하세요

#3. 두 변수를 이용해 아래 문장을 출력하세요
#HelloPythonHelloPythonHelloPython
a = "Hello"
b = "Python"

#4. 다음 변수에서 ,을 모두 제거하고 출력하세요
a = "1,234,567,890"

#upper 또는 lower 함수를 이용하면 문자를 대문자 또는 소문자로 바꾸어 출력할 수 있습니다.
a = "100abc"
print(a.upper()) #> 100ABC
b = "100ABC"
print(b.lower()) #> 100abc

#문제
#1. 다음 변수에서 Hello World를 출력하세요
a = "Hello_World"

#2. 다음 변수에서 2021년 10월 31을 출력하세요
b = "2021/10/31"

#3. 다음 변수를 이용해 아래 문장을 출력하세요
# 오늘은 피자먹는 날
a = "피자먹는"
b = "오늘"
c = "날"

#4. 다음 변수에서 /을 모두 공백으로 바꾸세요
a = "2021/10/31" #"2021 10 31"로 변경
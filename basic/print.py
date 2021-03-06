#print() 함수 기초
#Hello, World를 출력하세요

#문자열 안에서 ' 또는 "를 표현하기 위해서는 \'과 \"을 이용해야합니다. 
# (예 : Mary's Backpack을 출력 => Mary\'s Backpack으로 표현)
# 이와 같이 앞에 \를 붙여서 표현하는 문자들을 이스케이프 문자라고 합니다.

#문제
# 1. 아래 문장을 출력하세요 
# 신씨가 소리질렀다 "도둑이야!"

#print()함수에서 줄바꿈은 \n을 이용해야 합니다.
#탭을 표현할 때는 \t를 이용합니다.

#문제
#1. 다음 코드를 실행해보고 \n과 \t의 차이를 알아보세요
print("Hello\nNice\t\tMeet You") 

#2. 아래 문장을 print() 하나만 이용해 출력하세요
#안녕하세요
#만나서
#만갑습니다

#print() - 여러개의 데이터를 출력하기
#,를 이용하면 여러개의 데이터를 출력할 수 있습니다.
#다음 코드를 실행해 봅시다.
print("오늘", "뭐먹지") #> 오늘 뭐먹지
#,를 이용해 데이터를 출력하면 공백으로 각각의 데이터가 구분되어 출력됩니다.
#sep 인자를 이용해 구분 문자를 바꿀 수 있습니다.
#다음 코드를 실행해 봅시다.
print("오늘", "뭐먹지", sep="/") #> 오늘/뭐먹지

#또, print() 사용시 자동으로 마지막에 \n이 붙어서 print() 한번에 한줄이 출력될 것입니다.
#end 인자를 이용하면 마지막에 붙는 문자를 바꿀 수 있습니다.
#다음 코드를 실행해 봅시다.
print("오늘", end="")
print("뭐먹지") #> 오늘뭐먹지

#문제
#1. 아래 코드를 수정해 "a/b/c/d"를 출력하도록 하세요
print("a","b","c","d")

#2. 아래 코드를 수정해 "abcd"를 출력하도록 하세요
print("a")
print("b")
print("c")
print("d")

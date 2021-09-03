import random

def getCards() : #카드들을 생성한다.
    cards = []
    for i in range(4) :
        #수식 카드 만들기
        num1 = random.randint(1,9)
        num2 = random.randint(1,9)
        op = random.randint(1,2)

        content = ""
        correctContent = ""
        if op == 1 :
            content = str(num1) + "+" + str(num2)
            correctContent = str(num1 + num2)
        elif op == 2 :
            content = str(num1) + "-" + str(num2)
            correctContent = str(num1 - num2)
        
        cards.append(content)
        cards.append(correctContent)
    print(cards)

getCards()
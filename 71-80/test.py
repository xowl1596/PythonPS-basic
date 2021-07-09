# def isOverNum(a) :
#     sum = 0
#     for i in range(1, int(a/2)+1) :
#         if a % i == 0 :
#             sum += i
#     if sum > a :
#         return True
#     else :
#         return False

# overNums = []
# numbers = set([i for i in range(1,28124)])
# temp = []
# for i in range(1, 28124) :
#     if isOverNum(i) :
#         overNums.append(i)
# print("과잉수 구하기 완료. 과잉수 갯수 : ", len(overNums))

# for i in range(1, 28124) :
#     found = False
#     for a in overNums :
#         if found :
#             break
#         if a >= i : 
#             break
#         for b in overNums :
#             if b >= i :
#                 break
#             if a + b == i :
#                 print(i, a, b)
#                 temp.append(i)
#                 found = True
#                 break
# temp = set(temp)

# numbers = list(numbers.difference(temp))
# print(sum(numbers))

#프로젝트 오일러 28번문제
# sum = 1


# pivot = 3
# diff = 2
# for i in range(500) :
#     partSum = 0
#     for i in range(4) :
#         partSum += (pivot**2) - (diff*i)
#     sum += partSum
#     pivot += 2
#     diff += 2
# print(sum)
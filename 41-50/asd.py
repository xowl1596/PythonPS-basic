# map = [[3,6,2,8],
#        [7,3,4,2],
#        [8,6,7,3],
#        [5,3,2,9]]
map = [[2,1,2,1],
       [1,2,1,1],
       [2,1,1,1],
       [1,1,1,1]]
def checkDangerZone(x, y) : 
    global map 
    result = False
    
    current = map[x][y]
    #가로 지형 판단.    
    if x == 0 or x == 3 : 
        if x == 0 and current >= map[x+1][y]  : #x좌표가 0 => 오른쪽만 판단.
            return False
        elif x == 3 and current >= map[x-1][y] : #x좌표가 0 => 왼쪽만 판단.
            return False
    elif current >= map[x+1][y] or current >= map[x-1][y] : 
        return False#그 외 : 양쪽 모두 판단.

    #세로 지형 판단.
    if y == 0 or y == 3 : 
        if y == 0 and current >= map[x][y-1]  : #y좌표가 0 => 아래쪽만 판단.
            return False
        elif y == 3 and current >= map[x][y-1] : #y좌표가 3 => 위쪽만 판단.
            return False
    elif current >= map[x][y-1] or current >= map[x][y+1] : #그 외 : 양쪽 모두 판단.
        return False

    return True

count = 0
for x in range(4) :
    for y in range(4) :
        if checkDangerZone(x, y) :
            count += 1

print(count)
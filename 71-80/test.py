for a in (1, 1001) :
    print(a)
    for b in (a+1, 1001) :
        for c in (b+1, 1001) :
            print(a**2 + b**2 == c**2)
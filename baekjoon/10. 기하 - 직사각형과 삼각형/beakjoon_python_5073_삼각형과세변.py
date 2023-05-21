while 1:
    a, b, c = map(int, input().split())
    if a == 0 and b == 0 and c == 0:
        break
    
    list = sorted([a, b, c], reverse=True)
    if list[0] < list[1] + list[2]:
        if a == b == c:
            print("Equilateral")
        elif a == b or b == c or a == c:
            print("Isosceles")
        else:
            print("Scalene")
    else:
        print("Invalid")
while True:
    a, b = map(int,input().split())
    
    if 0 < a < 10 and 0 < b < 10:
        print(a+b)
    elif 0 == a and 0 == b:
        break

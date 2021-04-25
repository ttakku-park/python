count = int(input())

if 1 <= count <= 9:
    for i in range(1,10):
        result = count * i
        print(count,'*',i,'=',result)

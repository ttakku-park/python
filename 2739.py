a = int(input("1부터 9까지의 숫자를 입력하세요"))
while (True):
    if (1 <= a <= 9):
        for i in range(1,a+1):
            print(a,'X',i,'=',a*i)
        
    else:
        print("다시입력하세요")  #while 사용해서 input으로 돌아가고싶었는데 구현을 못했습니다
        a = int(input("1부터 9까지의 숫자를 입력하세요")) #####방금추가
 
 
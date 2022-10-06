A, B = map(int, input("").split(" ")) 

if A > B:
    print(">")
elif A < B:
    print("<")
elif A == B:
    print("==")


# map 함수 1) 함수 하나(int)와 리스트 하나를 입력받는다. 
#          2) 리스트의 요소 하나하나에 함수를 적용한다.            

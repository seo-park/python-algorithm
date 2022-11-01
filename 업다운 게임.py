#업다운게임

#1. 정답 정하기 -> random 라이브러리 사용
#1-1. 정답은 1 ~ 100 사이의 숫자
import random
key = random.randint(1,100)

#2. 기회 5번 주기
for i in range(5) :
    #3. 사용자한테 대답을 입력 받기
    ans = int(input())
    if ans < key : #4. 사용자가 말한 대답보다 정답이 크다면 up 출력
        print("UP")
    elif ans > key : #5. 사용자가 말한 대답보다 정답이 작다면 down 출력
        print("DOWN")
    else :
        print("정답!") #6. 사용자가 정답 맞추면 정답! 출력하고 즉시 종료
        break
    

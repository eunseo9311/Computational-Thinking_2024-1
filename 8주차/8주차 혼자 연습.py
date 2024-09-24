
'''
money = 2500
while money >= 0:
    money -= 700
    print("아이스크림을 구매합니다.\n맛있다.")
else:
    print("돈이 없다 ㅠㅠ")
'''



#1부터 1000까지 모두 더한 값을 프린트하기
'''
n = 1
sum = 0
while n <= 1000:
    sum += n
    n += 1
print(sum)
'''



#구구단 3단 출력하기
'''
print("구구단 3단")
n = 1
while n <= 9:
    print("3 x %d = %d" % (n, 3*n))
    n += 1
'''



#입력받은 n단 출력하기
'''
n = int(input("구구단 n단을 출력하시겠습니까? : "))
print("구구단 %d단" % (n)) 
i = 1
while i <=  9:
    print("%d x %d = %d" % (n, i, n*i))
    i += 1
'''




#2의 배수 구하기
#30부터 70까지의 정수 중에서 2의 배수의 합을 구하기
'''
import time
sum = 0
n = 30
while n<= 70:
    n += 1
    if n % 2 == 0:
        sum += n
        time.sleep(0.1)
print("결과 값: ",sum)
'''




#1부터 10까지 숫자 출력하기
'''
import time
i = 1
while i <= 10:
    print(i)
    i += 1
    time.sleep(0.5)
'''



#4의 배수는 건너뛰기
'''
import time
i = 0
while i <= 50:
    i += 1
    if i  % 4 == 0:
        continue
    print(i)
'''

'''
import time
i = 0
while i <= 50:
    if i % 4 != 0:
        i += 1
    print(i)
    time.sleep(0.5)
'''
# 이거 정답 맞는거 같은데 뭔가 이상하네
'''
import time
i = 1
while i <= 50:
    if i % 4 != 0:
        print(i)
        time.sleep(0.5)
    i += 1
'''



#369 게임 3의 배수에 박수
'''
import time
i = 0
while i < 20:
    i += 1
    if i % 3 == 0:
        print("clap")
        time.sleep(0.5)
    else:
        print(i)
        time.sleep(0.5)
'''
    


#10에서 20까지 더해서 총합 출력하기
'''
sum = 0
i = 10
while i <= 20
    sum += i
    i += 1
print(sum)
'''


#6주차 복습

'''
rain = int(input("오늘 비 올 확률은? "))
if rain >= 60:
    print("우산을 챙겨 가세요.")
else:
    print("화창한 날씨 입니다.")
print("오늘도 행복한 하루 되세요.")


temp = int(input("현재 기온은 몇 도?"))
hTemp = int(input("최고 기온은 몇 도?"))
lTemp = int(input("최저 기온은 몇 도?"))
if temp >= 20:
    print("반팔 옷을 입으세요.")
if temp <= 10:
    print("날씨가 쌀쌀하니 겉옷을 챙기세요.")
if hTemp - lTemp >= 10:
    print("일교차가 심하니 감기에 주의하세요.")
    

성적 = 95
결석 = 2
if 성적 >= 90 and 결석 <= 1:
    print("Pass")
else:
    print("Fail")
print("열심히 공부하는 하루를 보냅시다.")


score = 90
if score >= 80:
    print("장학금 대상자 입니다.")
else:
    print("다음 학기에 장학금을 노려보세요.")
print("수고하셨습니다.")


score = int(input("점수를 입력하세요: "))
if score >= 90:
    print("장학금 대상자입니다.")
print("수고하셨습니다.")


#6시간 전의 시간을 알려주는 프로그램
현재시간 = int(input("지금 몇시 인가요? "))
print("%d시" % 현재시간)
if 현재시간 > 6:
    이전시간 = 현재시간 - 6
if 현재시간 <= 6:
    이전시간 = 현재시간 + 6
print("%d시" % 이전시간)


score = int(input("시험점수를 입력하세요: "))
if score >= 90:
    print("시험을 아주 잘 봤군요. 축하해요❤️‍")
elif score >= 80:
    print("시험을 괜찮게 봤군요. 수고했어요😊")
elif score >= 70:
    print("시험을 좀 못 봤군요. 다음에는 잘 해봐요🥹")
else:
    print("완전히 망했군요. 공부 좀 하세요😥")
    

import time
for i in range (1,10,1):
    print(i)
    time.sleep(0.5)


for n in range(1,10,1):
    print("Hello\nPython")
    
    

import time
n = int(input("정수 n을 입력하세요: "))
for n in range(1,n,1):   # n까지 하면 n-1까지만 나온다. 범위가 미만이라서 그렇게 된다.
    print(n)
    time.sleep(0.5)
print("종료합니다.")



import time
n = int(input("정수 n을 입력하세요: "))
for n in range(1,n+1,1):   # n까지 하면 n-1까지만 나온다. 범위가 미만이라서 그렇게 된다.
    print(n)
    time.sleep(0.5)
print("종료합니다.")



money = 2500
while money >= 0:
    money -= 700
    print("아이스크림을 구매합니다.\n맛있다.")
print("돈이 없다 😭")



money = 2500
i = 0
while money >= 0:
    money -= 700
    i += 1
    print("아이스크림을 %d개째 구매합니다.\n남은 돈은 %d원입니다." % (i, money))
    if i % 2 == 0:  # if 들여쓰기를 하나 더 해서 틀린거였음. print랑 같은 줄이다.
            print("맛있다.나는 자두 바가 좋아")
    else:
            print("맛있다. 오늘은 모히또 바를 먹을래")


a = list(range(10,101,10)) # 100이라고 쓰면 미만이라서 100이 출력이 안 된다
print(a)
b = list(range(10,51,5)) #50이라고 쓰면 미만이라서 50이 출력이 안 된다
print(b)


'''





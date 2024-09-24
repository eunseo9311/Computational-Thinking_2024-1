import time 
import winsound as ws 

def bb() :
    time.sleep(0.3) 
    ws.Beep(1000, 200)
    ws.Beep(1000, 200)
    time.sleep(0.5) 
    return 0 

print('[ 챗봇 프로그램 ] ')
print('컴퓨터와 대화하는 프로그램입니다.\n')
bb() 

while True :
    talk = input('User : ')
    print('Comp : ', end='') 
    if talk == '안녕' :
        bb()
        print('안녕~ 반가워')
    elif talk == '놀자' :
        bb() 
        print('좋아~ 재밌게 놀자')
    elif talk == '뭐해' :
        bb() 
        print('너랑 얘기하는 중이야')
    elif talk == '잘가' :
        bb() 
        print('다음에 또 만나자.') 
        break 
    else :
        bb() 
        print('뭐라고?')

print('\nComp : 제가 아직은 많이 멍청합니다.') ; bb()
print('프로그램을 종료합니다.') 



 




        

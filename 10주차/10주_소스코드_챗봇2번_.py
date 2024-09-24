import time 
import winsound as ws 

def bb() :
    time.sleep(0.3) 
    ws.Beep(1000, 200)
    ws.Beep(1000, 200)
    time.sleep(0.4) 
    return 0 

bb() 
print('챗봇 프로그램')
print('코딩 언어에 대해 무엇이든 물어보세요\n') 

while True :
    query = input('질문 : ')
    query = query.upper() 
    print('답변 : ', end='') 

    if 'C' in query :
        bb() 
        print('C언어는 대표적인 코딩 언어입니다.')
    elif '자바' in query or 'JAVA' in query :
        bb() 
        print('자바는 안드로이드 앱 개발에 많이 활용됩니다.')
    elif '파이썬' in query or 'PYTHON' in query :
        bb() 
        print('파이썬은 최근 1위의 언어입니다.')
    elif '안녕' in query :
        bb() 
        print('코딩 언어에 대해 질문하세요.')
    
    else :
        bb() 
        print('뭐라고?')
    print() 




        

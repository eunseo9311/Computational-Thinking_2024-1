import tkinter as tk
from functools import partial
import webbrowser
import os
import random


# 노래 링크를 여는 함수들
def card_click_stress(card_number, emoji):
    links = {
        "🤪": "https://www.youtube.com/watch?v=iIPH8LFYFRk",
        "🍷": "https://www.youtube.com/watch?v=MBNQgq56egk",
        "🥇": "https://www.youtube.com/watch?v=3fp9effzCTE",
        "🩷": "https://www.youtube.com/watch?v=KeMbLY7ztDw",
        "🌊": "https://www.youtube.com/watch?v=VJfGfB4-vP0",
        "🍭": "https://www.youtube.com/watch?v=8WfFGy4NT-M",
        "🦋": "https://www.youtube.com/watch?v=iFoqGyWhMws",
        "🤕": "https://www.youtube.com/watch?v=JaIMSzE5yLA",
        "🔋": "https://www.youtube.com/watch?v=pkcJEvMcnEg",
    }
    if emoji in links:
        webbrowser.open(links[emoji])

def card_click_angry(card_number, emoji):
    links = {
        "🔗": "https://m.youtube.com/watch?v=qsUA0w6uYEE&pp=ygUM7Jew6rKw6rOg66as",
        "😠": "https://m.youtube.com/watch?v=r4krir0ymF8&pp=ygUKRG9udCB0b3VjaA%3D%3D ",
        "🏎": "https://youtu.be/medo8dj_-28?si=9HluttQqRRkdwqWk",
        "⚽": "https://youtu.be/xkgNsE9Uhzc?si=Ep-yDuNM9Rbyjm7_",
        "🙏": "https://youtu.be/Kbj2Zss-5GY?si=eE3lWDB8Mm9OlG4B",
        "🦖": "https://youtu.be/r_0JjYUe5jo?si=ysqbTb19sn6Qsj9T",
        "🎱": " https://youtu.be/_XhLIXjUtFg?si=4PJ4MA9IvBLRrDeg",
        "👠": "https://youtu.be/1HOyIJ084lk?si=dxUa9dlco2GqQxrD",
        "💫": "https://youtu.be/8x-M7AkTvrQ?si=ahFmpKN7q8_uctHj",
    }
    if emoji in links:
        webbrowser.open(links[emoji])

def card_click_sad(card_number, emoji):
    links = {
        "🤫": "https://www.youtube.com/watch?v=SL3KEvmAgoY",
        "☂️": "https://www.youtube.com/watch?v=V47v-AXQBSw",
        "🚚": "https://www.youtube.com/watch?v=1FIhcdocT-k",
        "😢": "https://www.youtube.com/watch?v=RgKAFK5djSk",
        "🎀": "https://www.youtube.com/watch?v=iasIUYRT_fE",
        "🌸": "https://www.youtube.com/watch?v=hWOB5QYcmh0",
        "🌹": "https://www.youtube.com/watch?v=hx4TOIy902E",
        "💦": "https://www.youtube.com/watch?v=pgN-vvVVxMA&rco=1",
        "🐦": "https://www.youtube.com/watch?v=2ZEdEoEZ1zQ",
    }
    if emoji in links:
        webbrowser.open(links[emoji])

def card_click_fun(card_number, emoji):
    links = {
        "⭐": "https://youtu.be/HYsz1hP0BFo?si=5RUdGjx51vhWz0Ma",
        "🏃‍♀": "https://youtu.be/EGd2H11qKPI?si=lxgjDy6bb8nKeSxx",
        "🌑": "https://youtu.be/vNx1pg7PLzw?si=0_3CDO7-s9kMZ2Tz ",
        "🦙": "https://youtu.be/xcKl3QDh6b0?si=P6XqV6JcMJJr1xBW",
        "🤔": "https://youtu.be/kkVD6ZDqNdA?si=0w4uR71Sctv7pdjX",
        "🛩": "https://youtu.be/0_LtCBHRNZM?si=vSetVmKSxHV7pYYw",
        "😝": "https://youtu.be/5Wiio4KoGe8?si=Fi9gPW01savxf6yg",
        "💍": "https://youtu.be/6q0JnftlH-I?si=_KuC5QQDa9vc9NrL",
        "🐬": "https://youtu.be/kRj4toENrnA?si=cd619kLqhyH8n46Z",
    }
    if emoji in links:
        webbrowser.open(links[emoji])

def card_click_love(card_number, emoji):
    links = {
        "🎙": "https://m.youtube.com/watch?v=BUzI-awsi1s&pp=ygUP64W4656Y67Cp7JeQ7ISc",
        "🌼": "https://m.youtube.com/watch?v=sRmbrE6eHpU&pp=ygUQ6rCA7Iq07J20IOubtOuLpA%3D%3D",
        "💝": "https://m.youtube.com/watch?v=O0RcKP1YzGM&pp=ygUQ6rOg67CxIOyepeuylOykgA%3D%3D",
        "⭐": "https://m.youtube.com/watch?v=9U8uA702xrE&pp=ygUQ7Jqw7KO866W8IOykhOqyjA%3D%3D",
        "🌿": "https://m.youtube.com/watch?v=AE005nZeF-A&pp=ygUPRnJhbmsgb2NlYW4gbHZ5",
        "💕": "https://m.youtube.com/watch?v=aKHbqm-D62Y&pp=ygUHTG92ZSB5YQ%3D%3D",
        "💙": "https://m.youtube.com/watch?v=D1PvIWdJ8xo&pp=ygUIQmx1ZW1pbmc%3D",
        "🫧": "https://m.youtube.com/watch?v=kffacxfA7G4&pp=ygUFQmFieSA%3D",
        "💊": "https://m.youtube.com/watch?v=dTwj7PhpY9M&pp=ygUKUGFpbmtpbGxlcg%3D%3D",
    }
    if emoji in links:
        webbrowser.open(links[emoji])

# 카드 게임을 시작하는 함수
def card_game(card_click_function, emojis):
    card_window = tk.Toplevel()
    card_window.title("Card Game")

    # 카드 프레임 생성
    card_frame = tk.Frame(card_window)
    card_frame.pack(pady=20, padx=20)

    random.shuffle(emojis)

    # 9개의 카드 버튼 생성
    cards = []
    for i in range(9):
        card_button = tk.Button(card_frame, text=emojis[i], width=6, height=3,
                                command=partial(card_click_function, i+1, emojis[i]),font=("Helvetica", 36))
        card_button.grid(row=i//3, column=i%3, padx=5, pady=5)
        cards.append(card_button)

    return card_window

# 대화 함수
def start_conversation(emoticon):
    global current_card_window
    if current_card_window is not None and current_card_window.winfo_exists():
        current_card_window.destroy()
    
    if emoticon == "🤯":
        emojis = ["🤪","🍷","🥇","🩷","🌊","🍭","🦋","🤕","🔋"]
        current_card_window = card_game(card_click_stress, emojis)
    elif emoticon == "😡":
        emojis = ["🔗","😠","🏎","⚽","🙏","🦖","🎱","👠","💫"]
        current_card_window = card_game(card_click_angry, emojis)
    elif emoticon == "😭":
        emojis = ["🤫","☂️","🚚","😢","🎀","🌸","🌹","💦","🐦"]
        current_card_window = card_game(card_click_sad, emojis)
    elif emoticon == "🤣":
        emojis = ["⭐","🏃‍♀","🌑","🦙","🤔","🛩","😝","💍","🐬"]
        current_card_window = card_game(card_click_fun, emojis)
    elif emoticon == "😍":
        emojis = ["🎙","🌼","💝","⭐","🌿","💕","💙","🫧","💊"]
        current_card_window = card_game(card_click_love, emojis)

# 버튼을 클릭할 때 호출되는 함수
def select_emoticon(emoticon):
    root.user_emoticon = emoticon  # 사용자가 선택한 이모티콘을 저장합니다.
    start_conversation(emoticon)

# Tkinter 윈도우 생성
root = tk.Tk()
root.title("오늘의 기분")

# 현재 스크립트 파일의 디렉토리 확인
script_dir = os.path.dirname(os.path.abspath(__file__))

# 배경 이미지 파일 경로 설정
background_image_path = os.path.join(script_dir, "background.png")

# 배경 이미지 로드
background_photo = tk.PhotoImage(file=background_image_path)

# 배경 이미지를 담을 캔버스 생성
canvas = tk.Canvas(root, width=background_photo.width(), height=background_photo.height())
canvas.pack(fill="both", expand=True)

# 캔버스에 배경 이미지 표시
canvas.create_image(0, 0, image=background_photo, anchor="nw")

button_font = ("Helvetica", 24)

# 현재 카드 창을 저장할 변수
current_card_window = None

# 버튼 생성
stress_button = tk.Button(root, text="🤯", font=button_font, command=lambda: select_emoticon("🤯"))
angry_button = tk.Button(root, text="😡", font=button_font, command=lambda: select_emoticon("😡"))
sad_button = tk.Button(root, text="😭", font=button_font, command=lambda: select_emoticon("😭"))
fun_button = tk.Button(root, text="🤣", font=button_font, command=lambda: select_emoticon("🤣"))
love_button = tk.Button(root, text="😍", font=button_font, command=lambda: select_emoticon("😍"))

# 버튼을 캔버스에 배치
canvas.create_window(background_photo.width()//2 - 200, background_photo.height()//2+150, window=stress_button)
canvas.create_window(background_photo.width()//2 - 100, background_photo.height()//2+150, window=angry_button)
canvas.create_window(background_photo.width()//2, background_photo.height()//2+150, window=sad_button)
canvas.create_window(background_photo.width()//2 + 100, background_photo.height()//2+150, window=fun_button)
canvas.create_window(background_photo.width()//2 + 200, background_photo.height()//2+150, window=love_button)

root.user_emoticon = None

# 윈도우 실행
root.mainloop()

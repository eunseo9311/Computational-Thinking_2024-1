n = int(input(ㅈ"몇 각형을 그려줄까요?"))


import turtle
t = turtle.Turtle()
t.width(3)

for i in range(n):
    t. forward(100)
    t.right(360/n)

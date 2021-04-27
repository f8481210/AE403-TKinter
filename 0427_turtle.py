import turtle
tur = turtle.Turtle()

#設置畫面大小
turtle.setup(500,500)

#定義畫矩形&著色函式
def rectangle():
    tur.begin_fill()
    for i in range(2):
        tur.forward(200)
        tur.right(90)
        tur.forward(50)
        tur.right(90)
    tur.end_fill()

def Goto(x,y):
    tur.penup()
    tur.goto(x,y)
    tur.pendown()

#上面黑色部分
Goto(-100,100)
tur.fillcolor(0,0,0)
rectangle()

#中間紅色部分
Goto(-100,50)
tur.fillcolor(1,0,0)
rectangle()

#下面黃色部分
Goto(-100,0)
tur.fillcolor(1,1,0)
rectangle()

#完成程式
turtle.done()
turtle.exitonclick()


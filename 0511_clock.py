#載入模組
import turtle
import time
import datetime

#創建turtle
tur = turtle.Turtle()
tur.seth(90)
tur.speed(10)

#step1 時鐘刻度
def writenum(num):
    tur.penup()
    tur.forward(200)
    tur.write(num)
    tur.back(200)

for i in range(1,13):
    tur.right(30)
    writenum(i)    

#step2 時針、分針、秒針
update = True
updateSecond = True

while True:

    now = datetime.datetime.now()
    h = now.hour % 12
    m = now.minute
    s = now.second

    if update: #時針，分針
        htur = turtle.Turtle()
        htur.seth(90)
        htur.right(h*30+m/60*30)
        htur.forward(100)
        
        mtur = turtle.Turtle()
        mtur.seth(90)
        mtur.right(m*6)
        mtur.forward(140)
        update = False
        
    if updateSecond: #秒針
        stur = turtle.Turtle()
        stur.seth(90)
        stur.right(s*6)
        stur.forward(175)
        updateSecond = False
        

#step3 讓秒針一直轉，指針會依據現在時間移動到正確位置
    time.sleep(1)
    new = datetime.datetime.now()
    mNew = new.minute
    
    updateSecond = True
    stur.clear()
    stur.reset()
    
    if mNew != m:
        update = True
        htur.clear() #清除
        htur.reset() #重畫
        
        mtur.clear() #清除
        mtur.reset() #重畫    

    
turtle.done()
turtle.exitonclick()
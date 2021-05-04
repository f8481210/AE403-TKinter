#載入模組
import turtle
import time
import datetime
#創建turtle
tur = turtle.Turtle()

#step1 時鐘刻度
def writeNumber(num):
    tur.penup()
    tur.forward(200)
    tur.write(num)
    tur.back(200)
    tur.pendown()
    
tur.seth(90)    

for i in range(1,13):
    tur.right(30)
    writeNumber(i)
   
#step2 時針、分針、秒針

update = True #是否要更新時間(時針/分針)
updateSecond = True #是否要更新時間(秒針)

while True:
    now = datetime.datetime.now()#取得時間時(12進制)/分/秒
    h = now.hour % 12
    m = now.minute
    s = now.second
    
    if update:
          hour = turtle.Turtle()#繪畫時針
          hour.seth(90) #將Turtle轉向北方
          #一圈12小時(30度/小時)
          #分鐘也會影響時針，每60分鐘影響30度(0.5度/分鐘)
          hour.right(h * 30 + m / 60 * 30)
          hour.forward(100)
          
          minute = turtle.Turtle()#繪畫分針
          minute.seth(90)#將Turtle轉向北方
          #6度/分鐘
          minute.right(m * 6)
          minute.forward(130)
          #由於繪畫完畢，update為False
          update = False



#step3 讓秒針一直轉，指針會依據現在時間移動到正確位置
    

turtle.done()
turtle.exitonclick()

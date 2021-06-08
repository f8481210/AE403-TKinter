# -*- coding: utf-8 -*-
"""
Created on Mon Sep 17 10:21:59 2018

@author: Eric
"""

#匯入tkinter模組
import tkinter as tk

"""創建基本視窗"""
window = tk.Tk()

window.title("單選按鈕")

window.geometry("300x200")

"""Menu"""
menuBar = tk.Menu(window)

#檔案->第二層視窗
fileMenu = tk.Menu(menuBar,tearoff=False)

fileMenu.add_command(label="開新遊戲")

fileMenu.add_command(label="作弊指令")
#分隔線
fileMenu.add_separator()

fileMenu.add_command(label="Exit")
#設定好檔案的第二層視窗後，再包進檔案目錄內
menuBar.add_cascade(label="檔案  ",menu=fileMenu)

#選項->第二層視窗
fileMenu2 = tk.Menu(menuBar,tearoff=False)

fileMenu2.add_command(label="遊戲設定")

fileMenu2.add_command(label="畫面設定")

#選項->進階設定->第三層視窗
subMenu = tk.Menu(menuBar,tearoff=False)

subMenu.add_command(label="遊戲優化Max")

subMenu.add_command(label="攻擊所有敵人")
#設定好選項->進階設定->第三層視窗後，再包進進階設定目錄內
fileMenu2.add_cascade(label="進階設定",menu=subMenu)

#設定好選項->第二層視窗後，再包進選項目路內
menuBar.add_cascade(label="選項  ",menu=fileMenu2)

window.config(menu=menuBar)

"""RadioButton"""

#設定String初始值
string = tk.StringVar()
string.set("Tkinter")

"""顯示所選擇的文字"""
def selection():
    label.config(text="我是" + gender.get() +
                 "生，我喜歡" + string.get())

#創建label元件
label = tk.Label(window, bg='#aaa', text='尚未選擇')
label.pack()

#創建Radiobutton元件
radio1 = tk.Radiobutton(window,
                    text='Minecraft Python',
                    variable=string, value='Minecraft Python',
                    command=selection)
radio1.pack()

#創建Radiobutton元件
radio2 = tk.Radiobutton(window,
                    text='Pygame',
                    variable=string, value='Pygame',
                    command=selection)
radio2.pack()

#創建Radiobutton元件
radio3 = tk.Radiobutton(window,
                    text='Tkinter',
                    variable=string, value='Tkinter',
                    command=selection)
radio3.pack()

#設定變數儲存所選擇的值
gender = tk.StringVar()
gender.set("男")

#創建Radiobutton元件
radio4 = tk.Radiobutton(window,
                    text='男',
                    variable=gender, value="男",
                    command=selection)
radio4.pack()

#創建Radiobutton元件
radio5 = tk.Radiobutton(window,
                    text='女',
                    variable=gender, value='女',
                    command=selection)
radio5.pack()

#視窗開始前，先跑一次函式，改變label文字
selection()

#開始跑視窗
window.mainloop()



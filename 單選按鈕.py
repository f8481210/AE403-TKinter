# -*- coding: utf-8 -*-
"""
Created on Mon Sep 17 10:21:59 2018

@author: Eric
"""
#匯入tkinter模組
import tkinter as tk
"""創建基本視窗"""
window = tk.Tk()
window.geometry('300x300')
window.title("單選按鈕")
#創建可變動的tk字串變數
string = tk.StringVar()

"""顯示所選擇的文字"""
def selection():
    label.config(text="我喜歡" + string.get())

#創建label元件
label = tk.Label(window, bg='#f00', text='尚未選擇')
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


#開始跑視窗
window.mainloop()



#檔名：0316_tkinter
#匯入
import tkinter as tk
import tkinter.messagebox

def clickme():
    tkinter.messagebox.showinfo(title='提示',message='好痛')
#創建
window = tk.Tk()
#標題
window.title("恩恩的第一個GUI程式")
#畫面大小
window.geometry("300x300")

label = tk.Label(window,text="恩恩",bg="#000",fg="#FFF")
label.pack()

entry = tk.Entry(window,width=50)
entry.pack()

button = tk.Button(window,text="按鈕",command = clickme)
button.pack()

#顯示
window.mainloop()


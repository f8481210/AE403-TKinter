import tkinter as tk
window = tk.Tk()
window.title("Menu")
window.geometry("500x500")

menubar = tk.Menu(window)

#檔案->第二層視窗
filemenu = tk.Menu(menubar,tearoff=False)

filemenu.add_command(label="開新遊戲")
filemenu.add_command(label="作弊指令")
filemenu.add_separator()
filemenu.add_command(label="EXIT")

menubar.add_cascade(label="File",menu=filemenu)

filemenu2 = tk.Menu(menubar,tearoff=False)
filemenu2.add_command(label="遊戲設定")
filemenu2.add_command(label="畫面設定")
menubar.add_cascade(label="設定",menu=filemenu2)
#選項->進階設定->第三層視窗
submenu = tk.Menu(menubar,tearoff=False)
submenu.add_command(label="遊戲優化Max")
submenu.add_command(label="攻擊所有敵人")
filemenu.add_cascade(label="第三層選單",menu=submenu)

window.config(menu=menubar)
window.mainloop()
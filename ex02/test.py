import tkinter as tk
import tkinter.messagebox as tkm

#def button_click():
#    tkm.showwarning("警告", "ボタンを押したらダメだって")
def button_click(event):
    btn = event.widget
    txt = btn["text"]#辞書で取得しているから文字列
    tkm.showinfo(txt, f"[{txt}]ボタンが押されました")
    
root = tk.Tk()#window作成
root.title("お試し")
root.geometry("500x200")

label = tk.Label(root,
                 text="ラベルを書いてみた",
                 font=("Ricty Diminished", 20)
                 )
label.pack()#配置

#button = tk.Button(root, text="押すな",bg="green",command=button_click)
button = tk.Button(root, text="押すな")
button.bind("<1>", button_click)
button.pack()

entry = tk.Entry(width=30)#width 文字数
entry.insert(tk.END, "fugapiyo")
entry.pack()

root.mainloop()
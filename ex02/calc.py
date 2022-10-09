import tkinter as tk
import tkinter.messagebox as tkm

def btn_click(event):
    btn=event.widget
    txt=int(btn["text"])
    tkm.showinfo("", f"[{txt}]のボタンがクリックされました")
    entry.insert(tk.END, txt)
    return "break"

root = tk.Tk()
root.title("tk")
root.geometry("300x500")

entry = tk.Entry(justify="right",width=10,font=("Times New Roman", 40))
#justify 右揃え
entry.grid(columnspan=30)

for i in range(10):
    btn = tk.Button(root, text=f"{i}", font=("Times New Roman", 30), width=4, height=2)
    btn.bind("<1>", btn_click)
    if i==0:
        r=4
        
    elif i<4:
        r=3
    elif i<7:
        r=2
    else:
        r=1
    c=3-(i-1)%3
    btn.grid(row=r, column=c)

root.mainloop()
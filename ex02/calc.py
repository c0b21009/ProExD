import tkinter as tk
import tkinter.messagebox as tkm

def btn_click(event):
    btn=event.widget
    txt=btn["text"]
    #tkm.showinfo(f"{txt}", f"[{txt}]のボタンがクリックされました")
    entry.insert(tk.END, txt)
    
    #0tk.ENDを0にすると2つ目の入力が十の位になる
def equal(event):
    eqn = entry.get()
    res = eval(eqn)
    entry.delete(0, tk.END)
    entry.insert(tk.END, res)
    
root = tk.Tk()
root.title("tk")
root.geometry("300x600")

entry = tk.Entry(root, justify="right",width=10,font=("Times New Roman", 40))
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
btn = tk.Button(root, text="+", font=("Times New Roman", 30), width=4, height=2)
btn.bind("<1>", btn_click)
btn.grid(row=4, column=2)

btn = tk.Button(root, text="=", font=("Times New Roman", 30), width=4, height=2)
btn.bind("<1>", equal)
btn.grid(row=4, column=3)
root.mainloop()
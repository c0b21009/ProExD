import tkinter as tk
import maze_maker as mm #8
def key_down(event):
    global key
    key = event.keysym#5
    print(key)
    
def key_up(event):
    global key
    key = ""#6

def main_proc():
    
    global cx, cy
    if key == "Up":
        cy -= 20
    if key =="Down":
        cy += 20
    if key == "Left":
        cx -= 20
    if key =="Right":
        cx += 20
    can.coords("tori", cx, cy)
    root.after(100, main_proc)#7
    
if __name__ == "__main__":
    root = tk.Tk()
    root.title("迷えるこうかとん")#1
    
    can = tk.Canvas(root, width=1500, height=900,bg="black")
    can.pack()#2
    
    tori = tk.PhotoImage(file="fig/1.png")
    cx, cy =300, 400
    can.create_image(cx, cy, image=tori, tag="tori")#3
    
    key = "" #4
    root.bind("<KeyPress>", key_down)#5
    root.bind("<KeyRelease", key_up)#6
    root.mainloop()
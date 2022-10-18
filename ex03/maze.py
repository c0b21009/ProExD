import tkinter as tk
import maze_maker as mm #8
import tkinter.messagebox as tkm
import time
import random

# 5
def key_down(event):
    global key
    key = event.keysym


# 6
def key_up(event):
    global key
    key = ""


# 7
def main_proc():
    global mx, my
    global cx, cy
    global lx, ly
    global tmr,tmr2
    global px, py
    tmr +=1
    tmr2 +=0.1
    
    if key == "Up":
        my -= 1
    if key == "Down":
        my += 1
    if key == "Left":
        mx -= 1
    if key == "Right":
        mx += 1
    if maze_lst[my][mx] == 0: 
        cx, cy = mx*100+50, my*100+50
    else: 
        if key == "Up":
            my += 1
        if key == "Down":
            my -= 1
        if key == "Left":
            mx += 1
        if key == "Right":
            mx -= 1
    if tmr>130:
        tmr=0
    lx=(tmr%15)*100+50
    ly=(tmr//15)*100+50
    px=random.randint(0, 1500)
    py=random.randint(0, 900)
    
    canv.coords("tori", cx, cy)
    canv.coords("lion", lx, ly)
    canv.coords("pen", px, py)
    
    if lx==cx and ly==cy:
        tkm.showwarning("危ない！", "食べられちゃったー"+str(tmr2)+"秒逃げたよ")
        tori = tk.PhotoImage(file="fig/5.png") 
        mx, my = 1, 1
        cx, cy = mx*100+50, my*100+50
        canv.create_image(cx, cy, image=tori, tag="tori")
        tmr=0
        tmr2=0.0
    
        
    root.after(100, main_proc)


if __name__ == "__main__":
    tmr=0
    tmr2=0.0
    root = tk.Tk()
    root.title("迷えるこうかとん") # 1

    # 2
    canv = tk.Canvas(root, width=1500, height=900, bg="black")
    canv.pack()

    # 9,10
    maze_lst = mm.make_maze(15, 9)

    mm.show_maze(canv, maze_lst) 

    # 3
    tori = tk.PhotoImage(file="fig/5.png") 
    mx, my = 1, 1
    cx, cy = mx*100+50, my*100+50
    canv.create_image(cx, cy, image=tori, tag="tori")
    
    lion = tk.PhotoImage(file="fig/3926.png") 
    lx, ly = 100-50, 100-50
    canv.create_image(lx, ly, image=lion, tag="lion")
    
    pen = tk.PhotoImage(file="fig/3926.png") 
    px, py =0,0
    canv.create_image(px, py, image=pen, tag="pen")

    # 4
    key = "" 

    # 5,6
    root.bind("<KeyPress>", key_down)
    root.bind("<KeyRelease>", key_up)    

    # 7
    main_proc()

    root.mainloop()
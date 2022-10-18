import tkinter as tk
import maze_maker as mm #8

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
    canv.coords("tori", cx, cy)
    root.after(100, main_proc)


if __name__ == "__main__":
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

    # 4
    key = "" 

    # 5,6
    root.bind("<KeyPress>", key_down)
    root.bind("<KeyRelease>", key_up)    

    # 7
    main_proc()

    root.mainloop()
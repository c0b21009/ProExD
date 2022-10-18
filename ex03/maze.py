import tkinter as tk

if __name__ == "__main__":
    root = tk.Tk()
    root.title("迷えるこうかとん")
    
    can = tk.Canvas(root, width=1500, height=900,bg="black")
    can.pack()
    
    tori = tk.PhotoImage(file="fig/1.png")
    cx, cy =300, 400
    can.create_image(cx, cy, image=tori, tag="tori")
    root.mainloop()
    
    
    
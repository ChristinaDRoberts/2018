#Christina Roberts
#How to Code 2.0

from tkinter import*
my_pen = "up"
my_x, my_y = None, None

def main():
    root = Tk()
    my_sketch = Canvas(root)
    my_sketch.pack()
    my_sketch.bind("<Motion>", motion)
    my_sketch.bind("<ButtonPress-1>", my_pen_down)
    my_sketch.bind("<ButtonRelease-1>", my_pen_up)
    root.mainloop()

def my_pen_down(event):
    global my_pen
    my_pen = "down"

def my_pen_up(event):
    global my_pen, my_x, my_y
    my_pen = "up"
    my_x = None
    my_y = None

def motion(event):
    global my_x, my_y
    if my_pen == "down":
        if my_x is not None and my_y is not None:
            event.widget.create_line(my_x, my_y, event.x, event.y, smooth = True)
        my_x = event.x
        my_y = event.y

print("Use cursor to draw in field provided please.")
    
main()


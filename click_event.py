#Christina Roberts
#How to Code 2.0


from tkinter import*

print("Please left click anywhere on the canvas. Thank you.")


def main():
    root = Tk()
    my_window = Canvas(root, width = 300, height = 300)
    my_window.pack()
    my_window.bind("<Button>", test_click)
    root.mainloop()
def test_click(event):
    
    print("Clicked at: ", event.x, event.y)




main()

#Christina Robert
#How to Code 2.0

from tkinter import*
def new_skyscraper():
    win_w = scale_win_w.get()
    win_h = scale_win_h.get()
    w = scale_w.get()
    h = scale_h.get()
    gap = scale_gap.get()

    my_building.delete("all")

    my_building.create_rectangle(gap, gap, (win_w + 2) * gap + win_w * w,
                                 (win_h + 2) * gap + win_h * h,
                                 outline = "gray", fill = "gray")

    for i in range(win_w):
        for j in range(win_h):
            my_building.create_rectangle(((w + gap) * i + 2 * gap),
                                         ((h + gap) * j + 2 * gap),
                                         ((w + gap) * i + (2 * gap + w)),
                                         ((h + gap) * j + (2* gap + h)),
                                         outline = "black", fill = "white")

            my_building.pack(fill = BOTH, expand = 1)

root = Tk()
my_building = Canvas(root, width = 500, height = 500)
root.title("Skyscraper")
my_building.pack

scale_win_w = Scale(root, from_ = 5, to = 30, orient = HORIZONTAL, label = "Windows Wide")
scale_win_w.pack()


scale_win_h = Scale(root, from_ = 5, to = 30, orient = HORIZONTAL, label = "Windows High")
scale_win_h.pack()


scale_w = Scale(root, from_ = 5, to = 30, orient = HORIZONTAL, label = "Windows Width")
scale_w.pack()


scale_h = Scale(root, from_ = 5, to = 30, orient = HORIZONTAL, label = "Windows Height")
scale_h.pack()

scale_gap = Scale(root, from_ = 2, to = 20, orient = HORIZONTAL, label = "Windows Gap")
scale_gap.pack()

button = Button(root, text = "Draw Skyscraper", command = new_skyscraper)
button.pack()

root.mainloop()



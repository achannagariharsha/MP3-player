from tkinter import *
import random

root = Tk()
root.geometry("400x400")

l1 = Label(root, font=("Helvetica", 260))

def roll():
    dice = ['\u2680', '\u2681', '\u2682', '\u2683', '\u2684', '\u2685']
    result = f'{random.choice(dice)}{random.choice(dice)}'
    l1.config(text=result)
    l1.pack()
    if result[0] == result[1]:
        result_label.config(text="You Win!")

b1 = Button(root, text="Roll the Dice!", foreground='blue', command=roll)
b1.pack()

result_label = Label(root, text="", font=("Helvetica", 20))
result_label.pack()

root.mainloop()

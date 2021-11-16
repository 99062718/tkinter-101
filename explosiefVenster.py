import tkinter
import time

window = tkinter.Tk()
kleuren = ["black", "purple", "red", "orange", "yellow", "white"]
proportion = 50
proportionStr = str(proportion)
number = 6

def windowChange():
    global number
    if number == 0:
        print("BOOM!")
        window.destroy()
    else:
        global proportion
        global proportionStr
        window.configure(height=proportionStr, width=proportionStr, bg=kleuren[number - 1])
        print(number)
        number -=1
        proportion += 50
        proportionStr = str(proportion)
        window.after(2000, windowChange)

window.after(2000, windowChange)

window.mainloop()
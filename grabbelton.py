import tkinter
from tkinter import messagebox
import random
from tkinter.constants import COMMAND

mainWindow = tkinter.Tk()
mainWindow.title("De grabbelton")
grabbeltonItems = [
    "een Osu!sock", 
    "een League of legends usb", 
    "Saw op dvd", 
    "een Koelkastmagneet voor je harddrive", 
    "een Fietsband", 
    "een R toets keycap", 
    "een Bananenschil", 
    "Mijn hond Kai", 
    "Die 2 gozers van Daft punk", 
    "een Lege ijstheefles"
]

leftWindow = tkinter.Frame(
    mainWindow,
    bg="black"
)

leftWindow.pack(
    ipadx=30,
    ipady=300,
    side="left"
)

hoeveelheidGrabbels = tkinter.Label(
    leftWindow,
    text=len(grabbeltonItems)
)

hoeveelheidGrabbels.pack(
    side="bottom"
)

rightWindow = tkinter.Frame(
    mainWindow,
    bg="black"
)

rightWindow.pack(
    ipadx=30,
    ipady=300,
    side="right"
)

middleWindow = tkinter.Frame(
    mainWindow,
    bg="white"
)

middleWindow.pack(
    ipadx=240,
    expand=True,
    fill="y"
)

def grabbel():
    global grabbeltonItems
    randomNum = random.randint(0, len(grabbeltonItems) - 1)
    messagebox.showinfo(message="U heeft {} gegrabbeld!".format(grabbeltonItems[randomNum]))
    grabbeltonItems.remove(grabbeltonItems[randomNum])
    hoeveelheidGrabbels.configure(text=len(grabbeltonItems))

button = tkinter.Button(middleWindow)
button.configure(text="klik hier om te grabbelen", command=grabbel)
button.pack(
    padx=120,
    pady=150
)

mainWindow.mainloop()
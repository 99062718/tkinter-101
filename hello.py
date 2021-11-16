import tkinter

mainWindow = tkinter.Tk()

mainWindow.geometry("300x300")
mainWindow.title("Hello!")

blueWidget = tkinter.Label(
    mainWindow,
    text = "Hello Tkinter!",
    bg = "blue",
    fg = "white"  
)

redWidget = tkinter.Frame(
    mainWindow,
    bg = "red"
)

yellowWidget = tkinter.Frame(
    mainWindow,
    bg = "yellow"
)

blueWidget.pack(
    ipady = 70,
    fill = "x"
)

redWidget.pack(
    expand = True,
    fill = "both",
    side = "left"
)

yellowWidget.pack(
    expand = True,
    fill = "both",
    side = "right"
)

mainWindow.mainloop()
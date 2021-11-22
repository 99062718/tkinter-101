from datetime import datetime
import tkinter

mainWindow = tkinter.Tk()
mainWindow.title("De klok")
mainWindow.configure(width=500, height=200, bg="white")
currentText = tkinter.StringVar(value=0)

def setTime():
    currentTime = datetime.now()
    currentText.set(currentTime.strftime("%H:%M:%S"))
    mainWindow.after(500, setTime)

label = tkinter.Label(mainWindow)
label.configure(textvariable=currentText, font=("comic sans", 60))
label.pack(ipadx = 500, ipady = 200)

mainWindow.after(200, setTime)

mainWindow.mainloop()
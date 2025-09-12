# 1. Import Tkinter Module
# 2. Create the GUI application main Window
# 3. Add widgets
from tkinter import *

window = Tk()
window.title = ('Tkinter Sample Window')
window.geometry = ('300x300')

#Label
greeting = Label(text="Hello user", fg='black', bg='white')
#Button
button = Button(text="Click me", fg='white', bg='black')
#Entry
entry = Entry(fg='purple', bg='lightblue', width=100)

greeting.pack()
button.pack()
entry.pack()

frame = Frame(master=window, relief=RAISED, borderwidth=5)
frame.pack()
label = Label(master=frame, text="Sample Frame")
label.pack()

textbox = Text(fg='green', bg='white')
textbox.pack()

window.mainloop()
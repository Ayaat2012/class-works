import tkinter as tk

window = tk.Tk()

for i in range(3): #0,1,2
    for j in range(3): #0,1,2
        frame = tk.Frame(master=window, relief=tk.RAISED, borderwidth=15)
        frame.grid(row=i, column=j, padx=3, pady=3)
        label = tk.Label(master=frame, text=f"Row {i}\nColumn {j}")
        label.pack()

window.mainloop()
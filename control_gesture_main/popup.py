import tkinter as tk
from tkinter import messagebox

def popupmsg(msg):
    popup = tk.Tk()
    popup.wm_title("NOTIFICATION")
    label = tk.Label(popup, text=msg, height=10, width= 30)
    label.pack(side="top", fill="x", pady=10)

    B1 = tk.Button(popup, text="Okay", command=popup.destroy)
    B1.pack()
    popup.mainloop()

# Example usage
# popupmsg("YOUTUBE IS IN HANDS")

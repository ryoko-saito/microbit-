import tkinter as tk

def dispLabel():
    lbl.configure(text="こんにちは")

root = tk.Tk()
root.geometry("300x400")

lbl = tk.Label(text="LABEL")
btn = tk.Button(text="PUSH",command=dispLabel)

lbl.pack()
btn.pack()
tk.mainloop()

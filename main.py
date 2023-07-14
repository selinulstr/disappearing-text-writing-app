from tkinter import *
from tkinter import ttk
from tkinter.ttk import Style

ROOT_BG = "#FFB07F"
FRAME_BG = "#FFB07F"
TEXT_FG = "#FF52A2"
count = 0
current_text = None

root = Tk()
root.title("Disappearing Text Writing")
root.config(padx=30, pady=30, background=ROOT_BG)
root.geometry("690x400")
s = Style()
s.configure("My.TFrame", background=FRAME_BG)
frm = ttk.Frame(root, padding=10, style="My.TFrame")
frm.grid()


def check_text():
    global count, current_text
    text = entry.get()
    if len(text) > 0 and text == current_text:
        time_label.config(text=f"Deleting in: {count}")
        if count == 0:
            entry.delete(0, END)
            time_label.config(text="Start again...")
            check_text()
        else:
            root.after(1000, check_text)
            count -= 1
    else:
        current_text = entry.get()
        count = 5
        root.after(1000, check_text)


def start_again():
    global count, current_text
    current_text = None
    count = 0
    check_text()


app_label = ttk.Label(frm, text="Disappearing Text Writing", font=("Courier", 30, "bold"),
                      background=ROOT_BG, foreground="#F31559")
app_label.grid(column=0, row=0, columnspan=3, pady=30)
time_label = ttk.Label(frm, text="Start", font=("Courier", 30, "bold"),
                       background=ROOT_BG, foreground=TEXT_FG)
time_label.grid(column=0, row=1, columnspan=3, pady=30)
entry = ttk.Entry(frm, width=30, font=("Courier", 20, "bold"), foreground="#F31559")
entry.grid(column=0, row=2, columnspan=3, pady=30)
entry.focus()

check_text()
root.mainloop()
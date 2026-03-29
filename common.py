import tkinter as tk
import tkinter.font as tkFont

root = tk.Tk()
toonsoort_var = tk.StringVar(value="MAJEUR")
starttoon_entry = tk.Entry(root)
#dit is de layout van de akkoorden/trappen
normal_font = tkFont.Font(family="Arial", size=18, weight="bold")
output_label = tk.Label(root, text="", fg="green", font=normal_font)

#Dit opent een songwriting venster
def open_songwriting_venster():
    songwriting_venster = tk.Toplevel(root)
    songwriting_venster.title("Songwriting")
    songwriting_venster.geometry("400x400")

    tk.Label(songwriting_venster, text="Hier kunnen we songwriten!").pack(pady=10)
    tk.Button(songwriting_venster, text="Afsluiten", width=25, command=songwriting_venster.destroy).pack()
import tkinter as tk
import tkinter.font as tkFont

root = tk.Tk()
toonsoort_var = tk.StringVar(value="MAJEUR")
starttoon_entry = tk.Entry(root)
#dit is de layout van de akkoorden/trappen
normal_font = tkFont.Font(family="Arial", size=18, weight="bold")
output_label = tk.Label(root, text="", fg="green", font=normal_font)
output_drieklank = tk.Label(root, text="", fg="green", font=normal_font)
output_vierklank = tk.Label(root, text="", fg="green", font=normal_font)


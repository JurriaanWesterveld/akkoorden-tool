from alle_tonen import *
from toonladders import *
from septime import *
from common import *

from bereken_akkoorden import bereken_trappen



#Dit maakt het venster
root.title("Toonladder Generator")
root.geometry("600x300")

#Dit is de menu waar je kiest tussen verschillende toonsoorten
tk.Label(root, text="Werk je in mineur of majeur?").pack()
tk.OptionMenu(root, toonsoort_var, "MAJEUR", "MAJEUR 7", "MINEUR", "MINEUR 7").pack()

#Hier kies je de grondtoon en wordt dat doorgestuurd naar de "bereken_trappen" functie
tk.Label(root, text="Van welke toon wil je de akkoorden?").pack()
starttoon_entry.pack()
tk.Button(root, text="Bereken akkoorden", command=bereken_trappen).pack()
output_label.pack(pady=10)

#button voor afsluiten
tk.Button(root, text="Afsluiten", width=25, command=root.destroy).pack()





root.mainloop()
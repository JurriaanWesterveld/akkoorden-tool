from alle_tonen import *
from toonladders import *
from common import *
from bereken_akkoorden import bereken_trappen



#Dit maakt het venster
root.title("Toonladder Generator")
root.geometry("600x400")

#Dit is de menu waar je kiest tussen verschillende toonsoorten
tk.Label(root, text="Werk je in mineur of majeur?").pack()
tk.OptionMenu(root, toonsoort_var, "MAJEUR", "MINEUR").pack()

#Hier kies je de grondtoon en wordt dat doorgestuurd naar de "bereken_trappen" functie
tk.Label(root, text="Van welke toon wil je de akkoorden?").pack()
starttoon_entry.pack()
tk.Button(root, text="Bereken akkoorden", command=bereken_trappen).pack()
output_label.pack()


#button voor afsluiten
afsluiten_button = tk.Button(root, text="Afsluiten", width=25, activebackground="red", command=root.destroy)
afsluiten_button.place(relx=0.5, rely=0.9, anchor=CENTER)


root.mainloop()
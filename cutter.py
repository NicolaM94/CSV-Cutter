import csv
import tkinter as tk
from time import sleep

app = tk.Tk()
app.geometry("600x600")
app.resizable(False,False)
app.title("CSV Cutter by NicolaMoro")


tk.Label(app,text="Inserisci il percorso del file.\nIl file deve essere '.csv' per essere letto correttamente").pack()
path = tk.Entry(app, width=50)
path.pack()

tk.Label(app,text="Inserisci la chiave di partizione").pack()
part_key = tk.Entry(app,width=50)
part_key.pack()

def partitioner():
    with open(path.get()) as f:
        reader = csv.reader(f)
        for line in reader:
            for block in line:
                if part_key.get() in block:
                    with open("output.txt","a") as file:
                        file.write(str(line))
                        
    sublevel = tk.Toplevel()
    sublevel.title("CSV Cutter - Operazione Completa")
    sublevel.geometry("200x100")
    sublevel.resizable(False,False)
    tk.Label(sublevel,text="Operazione completata!").pack(pady=25)
    sublevel.mainloop()


tk.Button(app,text="Inizia",command = partitioner).pack(pady=10)

app.mainloop()


from tkinter import*
from tkinter import ttk


root = Tk()
root.title("Milhas para KM")


def calculate(*args):
    try:
        value = float(miles.get()) 
        result = int(1.6093 * value * 10000.0 + 0.5)/10000.0 
        kilometers.set(result) 
    except ValueError:
        pass 


mainframe = ttk.Frame(root, padding=" 3 3 12 12") 
mainframe.grid(column=0, row=0, sticky=(N,W,E,S)) 
root.columnconfigure(0, weight=1)
root.rowconfigure(0, weight=1)

miles = StringVar()
miles_entry = ttk.Entry(mainframe, width=7, textvariable=miles)
miles_entry.grid(column=2, row=1, sticky=(W,E))



kilometers = StringVar()
ttk.Label(mainframe, textvariable=kilometers).grid(column=2, row=2, sticky=(W,E))

ttk.Button(mainframe, text="Calcular", command=calculate).grid(column=3, row=3, sticky=W)


ttk.Label(mainframe, text="O valor em Milhas:").grid(column=1, row=1, sticky=W)
ttk.Label(mainframe, text="É equivalente a:").grid(column=1, row=2, sticky=E)
ttk.Label(mainframe, text="KM").grid(column=3, row=2, sticky=W)


for child in mainframe.winfo_children(): 
    child.grid_configure(padx=5, pady=5) 
miles_entry.focus() 
root.bind("<Return>", calculate) 

root.mainloop()

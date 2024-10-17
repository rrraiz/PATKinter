from tkinter import*
from tkinter import ttk

root = Tk()
root.title("Calculadora de IMC")

def calculate_bmi(*args): 
    try:
        weight = float(weight_entry.get())
        height = float(height_entry.get())
        bmi = weight / (height ** 2)
        result_label.config(text=f"{bmi:.2f}")
    except ValueError:
        pass
   
mainframe = ttk.Frame(root, padding=" 3 3 12 12") 
mainframe.grid(column=0, row=0, sticky=(N,W,E,S)) 
root.columnconfigure(0, weight=1)
root.rowconfigure(0, weight=1)

weight = StringVar()
weight_entry = ttk.Entry(mainframe, width=7, textvariable=weight)
weight_entry.grid(column=2, row=1, sticky=(W))

height = StringVar()
height_entry = ttk.Entry(mainframe,  width=7, textvariable=height)    
height_entry.grid(column=2, row=2, sticky=(W)) 

result_label = ttk.Label(mainframe)
result_label.grid(column=2, row=3, sticky=(W))

ttk.Button(mainframe, text="Calcular", command=calculate_bmi).grid(column=3, row=3, sticky=W)

ttk.Label(mainframe, text="Peso(kg):").grid(column=1, row=1, sticky=E)
ttk.Label(mainframe, text="Altura(m):").grid(column=1, row=2, sticky=E)
ttk.Label(mainframe, text="Seu IMC:").grid(column=1, row=3, sticky=E)

for child in mainframe.winfo_children(): 
      child.grid_configure(padx=5, pady=5)
      weight_entry.focus()
      root.bind("<Return>", calculate_bmi)

root.mainloop()



   

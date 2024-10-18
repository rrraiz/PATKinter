from tkinter import*
from tkinter import ttk
import random 

root = Tk()
root.title("Senha Aleatória")
root.minsize(300, 100)

def gerar_senha(tamanho=8):
    letra = 'aAbBcCdDeEfFgGhHiIjJkKlLmMnNoOpPqQrRsStTuUvVwWxXyYzZ'
    numero = "0123456789"
    caractere_especial = "!@#$%^&*()"
    senha_conjunto = letra + numero + caractere_especial

    senha = ""
    for i in range(8):
        caractere_aleatorio = random.choice(senha_conjunto)
        senha += caractere_aleatorio
    
    senha_var.set(senha)

mainframe = ttk.Frame(root, padding=" 3 3 12 12") 
mainframe.grid(column=0, row=0, sticky=(N,W,E,S)) 
root.columnconfigure(0, weight=1)
root.rowconfigure(0, weight=1)


senha_var = StringVar()
ttk.Label(mainframe, textvariable=senha_var).grid(column=2, row=2, sticky=(W,E))
ttk.Button(mainframe, text="Gerar senha", command=gerar_senha).grid(column=1, row=2, sticky=W)


for child in mainframe.winfo_children(): 
      child.grid_configure(padx=5, pady=5)
      root.bind("<Return>", gerar_senha)

root.mainloop()

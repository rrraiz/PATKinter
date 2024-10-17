#Aplicação gráfica simples em Python usando a biblioteca tkinter(usada para construir interfaces gráficas de usuário)
from tkinter import*
from tkinter import ttk

#Criando janela tk, que é a janela principal
root = Tk()
#Configuração título do App
root.title("Pés para Metros")

#Gerando loop para renderização iterminente. A função calculate converte o valor inserido de pés para metros.
def calculate(*args):
    try:
        value = float(feet.get()) #Entrada
        result = int(0.3048 * value * 10000.0 + 0.5)/10000.0 #P
        meters.set(result) #Saída
    except ValueError:
        pass #Ignora a função except, "passa" pela exceção sem tentar fazer a conversão ou atualizar o resultado. útil para manter a função robusta, sem interrupções na execução.

#Criando o nosso container <div></div>
mainframe = ttk.Frame(root, padding=" 3 3 12 12") #um frame é criado como um contêiner para outros widgets(botões, barras de rolagem, listas). 
mainframe.grid(column=0, row=0, sticky=(N,W,E,S)) #É posicionado na grade(grid) da janela principal, com espaço adicional (padding) em torno dele. 
root.columnconfigure(0, weight=1)
root.rowconfigure(0, weight=1)

feet = StringVar()#É usado para armazenar o valor do input e o resultado da conversão.
feet_entry = ttk.Entry(mainframe, width=7, textvariable=feet)#O campo 'Entry' é criado para que o usuário insira o valor em pés, sendo associado à variável feet. 
feet_entry.grid(column=2, row=1, sticky=(W,E))



meters = StringVar()
ttk.Label(mainframe, textvariable=meters).grid(column=2, row=2, sticky=(W,E))#Um label(um tipo de widget-exibe texto ou imagens em interfaces gráficas) exibe o resultado da conversão em metros, sendo vinculado à variável meters. Não permite interação direta (não é clicável ou editável)

ttk.Button(mainframe, text="Calcular", command=calculate).grid(column=3, row=3, sticky=W)#Criado para acionar a função calculate quando clicado. 

#Labels são adicionados em formato de texto para indicar as unidades e a relação entre pés e metros. 
ttk.Label(mainframe, text="Pés").grid(column=3, row=1, sticky=W)
#<p></p>
ttk.Label(mainframe, text="É equivalente a").grid(column=1, row=2, sticky=E)
#<p></p>
ttk.Label(mainframe, text="Metros").grid(column=3, row=2, sticky=W)

#Um loop é usado para adicionar espaçamento entre os widgets. A tecla 'Enter' também é vinculado para chamar a função de cálculo, possibilitando que o cálculo seja realizado. 
for child in mainframe.winfo_children(): #Retorna todos os widgets qie estão dentro do mainframe (widgets filhos)
    #O loop 'for' itera cada child que foi retornado por 'winfo_children()'. Para cada widget filho, o código aplica a congiguração de grade.
    child.grid_configure(padx=5, pady=5) #Utilizado para configurar propriedades de layout do widget(filho).
#'padx=5' e 'pady=5' adicionam um espaço de 5 pixels à esquerda e À direita. Ajuda a melhorar o espaçamento entre os widgets.
feet_entry.focus() #Define o foco no campo de entrada. Assim que a janela for aberta, o cursor ficará automaticamento dentro desse campo, permitindo que o usuário comce a digitar imediatamente. 
root.bind("<Return>", calculate) #Vincula a tecla 'Enter'(<Return>) à função calculate. Assim que o usário pressionar a tecla 'Enter' com a janela ativa, a função calculate será chamada. 

#O mainloop é chamado para iniciar a aplicação e permitir que ela res´ponsa a interações do usuário.
root.mainloop()

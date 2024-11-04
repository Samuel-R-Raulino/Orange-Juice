import tkinter as tk

janela = tk.Tk()

janela.columnconfigure(0, weight=3)
janela.columnconfigure(1, weight=3)
janela.columnconfigure(2, weight=3)

janela.title("Orange Juice")
janela.resizable(640,480)
imagem = tk.PhotoImage(file="Kratos_PS4.png")

logo = tk.Label(janela,image=imagem)
logo.grid(column=3,row=0,columnspan=2)

def _conta():
    print("conta")
def _navegacao():
    print("navegacao")
def _novidades():
    print("novidades")
def _biblioteca():
    print("biblioteca")

wid = 60
conta = tk.Button(janela,text="conta",width=wid,height = 2,command=_conta)
navegacao = tk.Button(janela,text="navegação",width=wid,height = 2,command=_navegacao)
novidades = tk.Button(janela,text="novidades",width=wid,height = 2,command=_novidades)
biblioteca = tk.Button(janela,text="biblioteca",width=wid,height = 2,command=_biblioteca)

conta.grid(column=2,row=1)
navegacao.grid(column=3,row=1)
novidades.grid(column=4,row=1)
biblioteca.grid(column=5,row=1)
janela.mainloop()
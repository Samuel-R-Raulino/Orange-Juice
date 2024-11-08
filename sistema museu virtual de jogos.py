import os
import tkinter as tk

def clear():
    os.system('cls')

clear()

janela = tk.Tk()


janela.title("Orange Juice")
janela.geometry("800x600")
janela.configure(bg="#C83436")


fonte_padrao = ("Arial", 10)

imagem_original = tk.PhotoImage(file="Pinto_de_Boi.jpg")

logo = tk.Label(janela, image=imagem_original, bg="#C83436")
logo.grid(column=0, row=0, columnspan=6, pady=10)

titulo = tk.Label(janela, text="Orange Juice Online Games", font=("Arial", 29, "bold"), bg="#C83436", fg="white", padx=5, pady=1)
titulo.grid(row=1, column=0, columnspan=6, sticky="we")



subtitulo = tk.Label(janela, text="Bem-vindo ao nosso sistema virtual de jogos online Orange Juice!", font=("Arial", 13, "bold"), bg="#C83436", fg="white", padx=5, pady=1)
subtitulo.grid(row=2, column=0, columnspan=6, sticky="we")
# Funções dos botões
def _conta():
    print("conta")

def _navegacao():
    print("navegação")

def _novidades():
    print("novidades")

def _biblioteca():
    print("biblioteca")


wid = 56
conta = tk.Button(janela, text="Conta", width=wid, height=2, command=_conta, font=fonte_padrao, bg="#FF914B", relief="solid", highlightcolor="white")
navegacao = tk.Button(janela, text="Navegação", width=wid, height=2, command=_navegacao, font=fonte_padrao, bg="#FF914B", relief="solid")
novidades = tk.Button(janela, text="Novidades", width=wid, height=2, command=_novidades, font=fonte_padrao, bg="#FF914B", relief="solid")
biblioteca = tk.Button(janela, text="Biblioteca", width=wid, height=2, command=_biblioteca, font=fonte_padrao, bg="#FF914B", relief="solid")

conta.grid(column=0, row=3, padx=10, pady=10)
navegacao.grid(column=1, row=3, padx=10, pady=10)
novidades.grid(column=2, row=3, padx=10, pady=10)
biblioteca.grid(column=3, row=3, padx=10, pady=10)

conteudo_frame = tk.Frame(janela, bg="white", bd=1, relief="solid")
conteudo_frame.grid(row=4, column=0, columnspan=6, sticky="NSEW", padx=10, pady=10)

conteudo = tk.Label(conteudo_frame, text="", font=fonte_padrao, bg="white", anchor="w", padx=10, pady=10)
conteudo.pack(fill="both", expand=True)

janela.grid_rowconfigure(4, weight=1)
janela.grid_columnconfigure(5, weight=1)


janela.mainloop()

import os
import tkinter as tk
from tkinter import messagebox
import sqlite3


def clear():
    os.system('cls')

clear()


def conectar_bd():
    conn = sqlite3.connect('usuarios.db') 
    return conn


def criar_tabela():
    conn = conectar_bd()
    cursor = conn.cursor()
    cursor.execute('''CREATE TABLE IF NOT EXISTS usuarios (
                        id INTEGER PRIMARY KEY AUTOINCREMENT,
                        usuario TEXT NOT NULL,
                        senha TEXT NOT NULL)''')
    conn.commit()
    conn.close()

criar_tabela()


def cadastrar_usuario():
    usuario = entrada_usuario.get()
    senha = entrada_senha.get()

    if usuario and senha:
        conn = conectar_bd()
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM usuarios WHERE usuario = ?", (usuario,))
        usuario_existe = cursor.fetchone()

        if usuario_existe:
            messagebox.showwarning("Aviso", "Este usuário já existe. Tente outro.")
        else:
            cursor.execute("INSERT INTO usuarios (usuario, senha) VALUES (?, ?)", (usuario, senha))
            conn.commit()
            messagebox.showinfo("Sucesso", "Usuário cadastrado com sucesso!")
            janela_cadastro.grid_forget() 
            janela_login.grid(row=0, column=0) 

        conn.close()
    else:
        messagebox.showwarning("Aviso", "Preencha todos os campos.")


def validar_login():
    usuario = entrada_usuario_login.get()
    senha = entrada_senha_login.get()

    if usuario and senha:
        conn = conectar_bd()
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM usuarios WHERE usuario = ? AND senha = ?", (usuario, senha))
        usuario_valido = cursor.fetchone()

        if usuario_valido:
            messagebox.showinfo("Sucesso", "Login bem-sucedido!")
            exibir_interface_principal()
        else:
            messagebox.showerror("Erro", "Usuário ou senha inválidos.")
        conn.close()
    else:
        messagebox.showwarning("Aviso", "Preencha todos os campos.")

def exibir_interface_principal():
  
    janela_login.grid_forget()

 
    titulo = tk.Label(janela, text="Orange Juice Online Games", font=("Arial", 29, "bold"), bg="#C83436", fg="white", padx=5, pady=1)
    titulo.grid(row=1, column=0, columnspan=6, sticky="we")

    subtitulo = tk.Label(janela, text="Bem-vindo ao nosso sistema virtual de jogos online Orange Juice!", font=("Arial", 13, "bold"), bg="#C83436", fg="white", padx=5, pady=1)
    subtitulo.grid(row=2, column=0, columnspan=6, sticky="we")

 
    wid = 56
    conta = tk.Button(janela, text="Conta", width=wid, height=2, command=lambda: print("conta"), font=("Arial", 10), bg="#FF914B", relief="solid", highlightcolor="white")
    navegacao = tk.Button(janela, text="Navegação", width=wid, height=2, command=lambda: print("navegacao"), font=("Arial", 10), bg="#FF914B", relief="solid")
    novidades = tk.Button(janela, text="Novidades", width=wid, height=2, command=lambda: print("novidades"), font=("Arial", 10), bg="#FF914B", relief="solid")
    biblioteca = tk.Button(janela, text="Biblioteca", width=wid, height=2, command=lambda: print("biblioteca"), font=("Arial", 10), bg="#FF914B", relief="solid")

    conta.grid(column=0, row=3, padx=10, pady=10)
    navegacao.grid(column=1, row=3, padx=10, pady=10)
    novidades.grid(column=2, row=3, padx=10, pady=10)
    biblioteca.grid(column=3, row=3, padx=10, pady=10)

    conteudo_frame = tk.Frame(janela, bg="white", bd=1, relief="solid")
    conteudo_frame.grid(row=4, column=0, columnspan=6, sticky="NSEW", padx=10, pady=10)

    conteudo = tk.Label(conteudo_frame, text="", font=("Arial", 10), bg="white", anchor="w", padx=10, pady=10)
    conteudo.pack(fill="both", expand=True)

    janela.grid_rowconfigure(4, weight=1)
    janela.grid_columnconfigure(5, weight=1)


janela = tk.Tk()
janela.title("Orange Juice")    
janela.geometry("800x600")
janela.configure(bg="#C83436")

janela_login = tk.Frame(janela, bg="#C83436")
janela_login.grid(row=0, column=0, columnspan=6, sticky="nsew", padx=10, pady=10)


usuario_label_login = tk.Label(janela_login, text="Usuário:", font=("Arial", 14), fg="white", bg="#C83436")
usuario_label_login.grid(row=0, column=0, padx=10, pady=10)
entrada_usuario_login = tk.Entry(janela_login, font=("Arial", 14), width=20)
entrada_usuario_login.grid(row=0, column=1, padx=10, pady=10)

senha_label_login = tk.Label(janela_login, text="Senha:", font=("Arial", 14), fg="white", bg="#C83436")
senha_label_login.grid(row=1, column=0, padx=10, pady=10)
entrada_senha_login = tk.Entry(janela_login, font=("Arial", 14), width=20, show="*")
entrada_senha_login.grid(row=1, column=1, padx=10, pady=10)


botao_login = tk.Button(janela_login, text="Entrar", font=("Arial", 14), bg="#FF914B", command=validar_login)
botao_login.grid(row=2, column=0, columnspan=2, pady=20)

botao_cadastro = tk.Button(janela_login, text="Cadastre-se", font=("Arial", 14), bg="#FF914B", command=lambda: janela_cadastro.grid(row=0, column=0))
botao_cadastro.grid(row=3, column=0, columnspan=2)

janela_cadastro = tk.Frame(janela, bg="#C83436")
janela_cadastro.grid(row=0, column=0, columnspan=6, sticky="nsew", padx=10, pady=10)

usuario_label_cadastro = tk.Label(janela_cadastro, text="Usuário:", font=("Arial", 14), fg="white", bg="#C83436")
usuario_label_cadastro.grid(row=0, column=0, padx=10, pady=10)
entrada_usuario = tk.Entry(janela_cadastro, font=("Arial", 14), width=20)
entrada_usuario.grid(row=0, column=1, padx=10, pady=10)

senha_label_cadastro = tk.Label(janela_cadastro, text="Senha:", font=("Arial", 14), fg="white", bg="#C83436")
senha_label_cadastro.grid(row=1, column=0, padx=10, pady=10)
entrada_senha = tk.Entry(janela_cadastro, font=("Arial", 14), width=20, show="*")
entrada_senha.grid(row=1, column=1, padx=10, pady=10)

botao_cadastrar = tk.Button(janela_cadastro, text="Cadastrar", font=("Arial", 14), bg="#FF914B", command=cadastrar_usuario)
botao_cadastrar.grid(row=2, column=0, columnspan=2, pady=20)

janela.mainloop()

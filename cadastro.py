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
            exibir_tela_login()

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


def exibir_tela_login():
    janela_cadastro.grid_forget()
    janela_login.grid(row=0, column=0, columnspan=6, sticky="nsew")


def exibir_tela_cadastro():
    janela_login.grid_forget()
    janela_cadastro.grid(row=0, column=0, columnspan=6, sticky="nsew")


def exibir_interface_principal():
    janela_login.grid_forget()
    janela_cadastro.grid_forget()

    titulo = tk.Label(janela, text="Orange Juice Online Games", font=("Arial", 29, "bold"), bg="#C83436", fg="white", padx=5, pady=1)
    titulo.grid(row=1, column=0, columnspan=6, sticky="we")

    subtitulo = tk.Label(janela, text="Bem-vindo ao nosso sistema virtual de jogos online Orange Juice!", font=("Arial", 13, "bold"), bg="#C83436", fg="white", padx=5, pady=1)
    subtitulo.grid(row=2, column=0, columnspan=6, sticky="we")


janela = tk.Tk()
janela.title("Orange Juice")
janela.geometry("800x600")
janela.configure(bg="#C83436")

# Tela de Login
janela_login = tk.Frame(janela, bg="#C83436")

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

botao_cadastro = tk.Button(janela_login, text="Cadastre-se", font=("Arial", 14), bg="#FF914B", command=exibir_tela_cadastro)
botao_cadastro.grid(row=3, column=0, columnspan=2)

# Tela de Cadastro
janela_cadastro = tk.Frame(janela, bg="#C83436")

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

botao_voltar = tk.Button(janela_cadastro, text="Voltar", font=("Arial", 14), bg="#FF914B", command=exibir_tela_login)
botao_voltar.grid(row=3, column=0, columnspan=2)

exibir_tela_login()
janela.mainloop()

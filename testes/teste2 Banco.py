import os
from tkinter import *
import sqlite3


def clear():
    os.system('cls')


def conectar_db():
    conn = sqlite3.connect('usuarios.db')
    return conn


def criar_tabela():
    conn = conectar_db()
    cursor = conn.cursor()
    cursor.execute('''CREATE TABLE IF NOT EXISTS tema(
                   id INTEGER PRIMARY KEY AUTOINCREMENT,
                   pref VARCHAR)''')
    conn.commit()
    conn.close()


def salvar_tema(tema):
    conn = conectar_db()
    cursor = conn.cursor()
    cursor.execute ("DELETE FROM tema")
    cursor.execute ("INSERT INTO tema (pref) VALUES (?)", (tema,))
    conn.commit()
    conn.close()


def carregar_tema():
    conn = conectar_db()
    cursor = conn.cursor()
    cursor.execute("SELECT pref FROM tema ORDER BY id DESC LIMIT 1")
    resultado = cursor.fetchone()
    conn.close()
    return resultado[0] if resultado else 'azul'


janela = Tk()
janela.resizable(False,False)
janela.title("titulo")
width = 640
height = 480
wheight = str(width)+"x"+str(height)
janela.geometry(wheight)


def mudarjanela(frame, tema):
    frame.tkraise()
    salvar_tema(tema)


azul = Frame(janela)
verde = Frame(janela)
rosa = Frame(janela)


for frame in (azul, verde, rosa):
    frame.grid(row=0, column=0, sticky="nsew")


cnv = Canvas(azul,width=width,height=height,bg="pink")
cnv.pack(expand=True)
retangulo = cnv.create_rectangle(10,10,width-10,height-10,fill="blue",outline="black",width=2)
bot = Button(azul,text="ficar verde",command=lambda:mudarjanela(verde, 'verde')).place(x=0,y=30)
bot = Button(azul,text="ficar rosa",command=lambda:mudarjanela(rosa, 'rosa')).place(x=90,y=30)
bot = Button(azul,text = "ficar azul",command=lambda:mudarjanela(azul, 'azul')).place(x=180,y=30)


cnv = Canvas(verde,width=width,height=height,bg="blue")
cnv.pack(expand=True)
retangulo = cnv.create_rectangle(10,10,width-10,height-10,fill="green",outline="black",width=2)
bot = Button(verde,text="ficar verde",command=lambda:mudarjanela(verde, 'verde')).place(x=0,y=30)
bot = Button(verde,text="ficar rosa",command=lambda:mudarjanela(rosa, 'rosa')).place(x=90,y=30)
bot = Button(verde,text = "ficar azul",command=lambda:mudarjanela(azul, 'azul')).place(x=180,y=30)


cnv = Canvas(rosa,width=width,height=height,bg="green")
cnv.pack(expand=True)
retangulo = cnv.create_rectangle(10,10,width-10,height-10,fill="pink",outline="black",width=2)
bot = Button(rosa,text="ficar verde",command=lambda:mudarjanela(verde, 'verde')).place(x=0,y=30)
bot = Button(rosa,text="ficar rosa",command=lambda:mudarjanela(rosa, 'rosa')).place(x=90,y=30)
bot = Button(rosa,text = "ficar azul",command=lambda:mudarjanela(azul, 'azul')).place(x=180,y=30)


criar_tabela()
tema_inicial = carregar_tema()
if tema_inicial == 'verde':
    mudarjanela(verde, 'verde')

elif tema_inicial == 'rosa':
    mudarjanela(rosa, 'rosa')

else:
    mudarjanela(azul, 'azul')


janela.mainloop()
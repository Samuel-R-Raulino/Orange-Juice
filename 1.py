from tkinter import *

def mostrarframe(frame):
    frame.tkraise()

janela = Tk()
janela.title("titulo")
janela.geometry("640x480")

frame1 = Frame(janela)
frame2 = Frame(janela)
frame3 = Frame(janela)

for frame in (frame1, frame2, frame3):
    frame.grid(row=0, column=0, sticky="nsew")
#classe 
#
texto = Label(frame1,text="texto")
texto.pack()
texto = Label(frame1,text="texto")
texto.pack()
texto = Label(frame1,text="texto")
texto.pack()
texto = Label(frame1,text="texto")
texto.pack()
botao = Button(frame1,text="botao",command=lambda:mostrarframe(frame2))
botao.pack()

canvas = Canvas(frame,width=300,height=200,bg="white")
canvas.pack()
retangulo = canvas.create_rectangle(50,50,100,100,fill="blue",outline = "black",width=2)
#
texto1 = Label(frame2,text="texto1")
texto1.pack()
texto1 = Label(frame2,text="texto1")
texto1.pack()
texto1 = Label(frame2,text="texto1")
texto1.pack()
texto1 = Label(frame2,text="texto1")
texto1.pack()
botao = Button(frame2,text="botao",command=lambda:mostrarframe(frame3))
botao.pack()
#
texto2 = Label(frame3,text="texto2")
texto2.pack()
texto2 = Label(frame3,text="texto2")
texto2.pack()
texto2 = Label(frame3,text="texto2")
texto2.pack()
texto2 = Label(frame3,text="texto2")
texto2.pack()
botao = Button(frame3,text="botao",command=lambda:mostrarframe(frame1))
botao.pack()

mostrarframe(frame)

janela.mainloop()
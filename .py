from tkinter import *

janela = Tk()
janela.resizable(False,False)
janela.title("titulo")
width = 640
height = 480
wheight = str(width)+"x"+str(height)
janela.geometry(wheight)

def mudarjanela(frame):
    frame.tkraise()

azul = Frame(janela)
verde = Frame(janela)
rosa = Frame(janela)

for frame in (azul, verde, rosa):
    frame.grid(row=0, column=0, sticky="nsew")

cnv = Canvas(azul,width=width,height=height,bg="pink")
cnv.pack(expand=True)
retangulo = cnv.create_rectangle(10,10,width-10,height-10,fill="blue",outline="black",width=2)
bot = Button(azul,text="ficar verde",command=lambda:mudarjanela(verde)).place(x=0,y=30)
bot = Button(azul,text="ficar rosa",command=lambda:mudarjanela(rosa)).place(x=90,y=30)
bot = Button(azul,text = "ficar azul",command=lambda:mudarjanela(azul)).place(x=180,y=30)
cnv = Canvas(verde,width=width,height=height,bg="blue")
cnv.pack(expand=True)
retangulo = cnv.create_rectangle(10,10,width-10,height-10,fill="green",outline="black",width=2)
bot = Button(verde,text="ficar verde",command=lambda:mudarjanela(verde)).place(x=0,y=30)
bot = Button(verde,text="ficar rosa",command=lambda:mudarjanela(rosa)).place(x=90,y=30)
bot = Button(verde,text = "ficar azul",command=lambda:mudarjanela(azul)).place(x=180,y=30)
cnv = Canvas(rosa,width=width,height=height,bg="green")
cnv.pack(expand=True)
retangulo = cnv.create_rectangle(10,10,width-10,height-10,fill="pink",outline="black",width=2)
bot = Button(rosa,text="ficar verde",command=lambda:mudarjanela(verde)).place(x=0,y=30)
bot = Button(rosa,text="ficar rosa",command=lambda:mudarjanela(rosa)).place(x=90,y=30)
bot = Button(rosa,text = "ficar azul",command=lambda:mudarjanela(azul)).place(x=180,y=30)

mudarjanela(azul)
janela.mainloop()
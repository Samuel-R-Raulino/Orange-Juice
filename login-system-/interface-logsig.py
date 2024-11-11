import tkinter as tk 

window = tk.Tk()

window.title("janela")
window.geometry("640x480")

#centralizar
window.columnconfigure(0, weight=1)
window.columnconfigure(1, weight=1)
window.columnconfigure(2, weight=1)
#titulo
texto1 = tk.Label(window,text="Login:")
texto1.grid(column=1,row=0,pady=5)
#login
texto = tk.Label(window,text="Email:")
texto.grid(column = 1,row = 1,sticky="e",pady=5)

barra = tk.Entry(window,width=20)
barra.grid(column = 2,row = 1,sticky="w",pady = 5)
#senha
texto = tk.Label(window,text="Senha:")
texto.grid(column = 1,row = 2,sticky="e",pady=5)

barra = tk.Entry(window,width=20,show="*")
barra.grid(column = 2,row = 2,sticky="w",pady=5)
window.mainloop()
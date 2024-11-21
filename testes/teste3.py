import tkinter as tk

# Configuração da janela principal
janela = tk.Tk()
janela.title("OraGame")
janela.geometry("400x300")
janela.configure(bg="orange")

# Função para alternar frames
def mostrarframe(frame):
    frame.tkraise()

# Frames criados e posicionados
frame_conta = tk.Frame(janela, bg="lightblue", width=400, height=300)
frame_conta.place(x=0, y=0)

frame_navegacao = tk.Frame(janela, bg="lightgreen", width=400, height=300)
frame_navegacao.place(x=0, y=0)

frame_biblioteca = tk.Frame(janela, bg="lightyellow", width=400, height=300)
frame_biblioteca.place(x=0, y=0)

frame_jogos = tk.Frame(janela, bg="lightpink", width=400, height=300)
frame_jogos.place(x=0, y=0)

# Botões para alternar frames
btn_conta = tk.Button(janela, text="Conta", bg="orange", font=("Arial", 10), command=lambda: mostrarframe(frame_conta))
btn_conta.place(x=50, y=50)

btn_navegar = tk.Button(janela, text="Navegar", bg="orange", font=("Arial", 10), command=lambda: mostrarframe(frame_navegacao))
btn_navegar.place(x=150, y=50)

btn_biblioteca = tk.Button(janela, text="Biblioteca", bg="orange", font=("Arial", 10), command=lambda: mostrarframe(frame_biblioteca))
btn_biblioteca.place(x=250, y=50)

btn_jogos = tk.Button(janela, text="Jogos", bg="orange", font=("Arial", 10), command=lambda: mostrarframe(frame_jogos))
btn_jogos.place(x=350, y=50)

# Conteúdo do frame_conta
texto_conta = tk.Label(frame_conta, text="Este é o Frame Conta", bg="lightblue", font=("Arial", 16))
texto_conta.place(x=100, y=150)

# Mostra o frame inicial
mostrarframe(frame_conta)

# Loop principal
janela.mainloop()

import os
def clear():
    os.system('cls')
clear()

#Criando a classe do cadastro
class CadastroJogo():
    #Informações do cadastro
    def __init__(self, titulo = str, descricao = str, preco = float, link = str, cadastrado = True):
        self.titulo = titulo
        self.descricao = descricao
        self.preco = preco
        self.link = link
        self.cadastrado = cadastrado
        
    #exibindo as informações do jogo cadastrado
    def exibir_detalhes(self):
        if not self.cadastrado:
            print('Jogo não cadastrado!')
            return
        
        print(f'Informações de {self.titulo}:')
        print(f'Descrição:\n {self.descricao}\n')
        print(f'Preço: R${self.preco:.2f}\n')
        print(f'Link: {self.link}\n')
        
    #editar as informações do jogo
    def editar_informacoes(self, titulo = None, descricao = None, preco = None, link = None):
        if titulo:
            self.titulo = titulo
        if descricao:
            self.descricao = descricao
        if preco is not None:  
            self.preco = preco
        if link:
            self.link = link
        print("Detalhes atualizados com sucesso!")
        
    #excluir jogo cadastrado
    def excluir_jogo(self):
        self.titulo = None
        self.descricao = None
        self.preco = None
        self.link = None
        self.cadastrado = False
import os
def clear():
    os.system('cls')
clear()

from cadastro_jogo import CadastroJogo

j1 = CadastroJogo('Minecraft', 'descriçãokk', 30, 'abacate.com')
#j1 = CadastroJogo(titulo, descricao, preco, link)
j2 = CadastroJogo('Cookie Clicker', 'Clicar em cookies', 100, 'cookieclicker.com')

j1.exibir_detalhes()
j2.exibir_detalhes()


#titulo = input('Insira o nome do jogo:\n')
#clear()

#descricao = input('Insira a descrição do jogo:\n')
#clear()

#preco = int(input('Insira o preço do jogo:\n'))
#clear()

#link = input('Insira o link de download do jogo:\n')
#clear()

j1.editar_informacoes('GTA5', 'Tilápia', 1000, 'goiaba.com')
j2.excluir_jogo()

j1.exibir_detalhes()
j2.exibir_detalhes()
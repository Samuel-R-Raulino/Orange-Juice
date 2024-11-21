import os
def clear():
    os.system('cls')
clear()

#Importando a class do cadastro de jogos
from cadastro_jogo import CadastroJogo

#Teste
j1 = CadastroJogo('Minecraft', 'descriçãokk', 30, 'abacate.com') #Cadastrando o primeiro jogo
j2 = CadastroJogo('Cookie Clicker', 'Clicar em cookies', 100, 'cookieclicker.com') #Cadastrando o segundo jogo

#exibindo detalhes dos jogos
j1.exibir_detalhes()
j2.exibir_detalhes()

j1.editar_informacoes('GTA5', 'Tilápia', 1000, 'goiaba.com') #Editando as informações do primeiro jogo 
j2.excluir_jogo() #Excluindo o segundo jogo 

#exibindo detalhes dos jogos
j1.exibir_detalhes() 
j2.exibir_detalhes()
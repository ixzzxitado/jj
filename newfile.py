
from time import sleep

sleep(2)

print('\033[1;49;37m Você deve ser novo por aqui..\033[m')

sleep(2)

resposta = str(input('\033[1;49;37m Meu nome é ------, Qual é o Seu?: \033[m'))

print('\033[1;49;37m Bem vindo {}!, queria te fazer uma pergunta....\033[m'.format(resposta))

input("press enter")

sleep(4)

print('\033[1;49;91m JÁ PODE AO-MOSSAR?:  \033[m')





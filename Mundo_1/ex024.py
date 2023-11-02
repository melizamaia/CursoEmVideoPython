## Crie um programa que leia o nome de uma cidade diga se ela começa ou não com o nome "SANTO".

cidade = str(input("Em que cidade você nasceu? : ")).strip() ##strip elimina os espaços
print(cidade[0:5].upper() == "SANTO") ##coloquei tudo em maiúscula para verificação

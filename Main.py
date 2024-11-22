from biblioteca import *


menu = 0
opcao = 0
print("teste")

while opcao != 4:
    menu = int(input("====MENU====\n"
                 "[1] CADASTRO\n"
                 "[2] TRIAGEM\n"
                 "[3] SAIR\n"
                 ""))
    if menu > 3 or menu <= 0:
        print("Operação Invalida!!")
    match menu:
        case 1:
            print(cadastrar(nome,cpf,ano_nascimento,peso,altura,telefone,endereco,cep))

cond = 1
while cond != 0:

    try:
        priori = int(input("Qual nivel de prioridade do paciente:\n"
                           "[1] BAIXA\n"
                           "[2] MODERADA\n"
                           "[3] URGENTE\n"
                           "[4] EMERGÊNCIA\n"))
    except TypeError:
        print("Erro! Digite de forma númerica.")

    match priori:
        case 1:
            prioridade = "Baixa"
            baixa = + 1
            cond = 0

        case 2:
            prioridade = "Moderada"
            moderada = + 1
            cond = 0

        case 3:
            prioridade = "Urgente"
            urgente = + 1
            cond = 0

        case 4:
            prioridade = "Emergencia"
            emergencia = + 1
            cond = 0
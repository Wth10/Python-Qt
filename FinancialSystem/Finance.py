import os

o = 0
r_t = 0
d_t = 0


def Menu():
    global o
    print("###### DEV.FINANCE ####### \n")
    print("[1] Cadastrar Receita: ")
    print("[2] Cadastrar Despesas: ")
    print("[3] Gerar Relatório: ")
    print("[4] Sair: \n")
    o = int(input("Digite Um Número: "))


def CadastrarReceita():
    global r_t
    print("####### Cadastrar Receita ####### \n")
    r = float(input("Digite Sua Receita: "))
    r_t = r_t + r


def CadastrarDespesas():
    global d_t
    print("####### Cadastrar Despesas ####### \n")
    d = float(input("Digite Sua Despesas: "))
    d_t = d_t + d


def GerarRelatorio():
    print("###### Relatórios ####### \n")
    print("Total De Receita: R$", r_t)
    print("Total De Despesas: R$", d_t)
    total = r_t - d_t
    print("Sua Carteira Tem: R$", total, "\n")

    if total > 0:
        print("Tá No Lucro 🤑")
    else:
        print("Ficou Negativo😢")


while o != 4:
    os.system("cls")
    Menu()

    if o == 1:
        CadastrarReceita()
    if o == 2:
        CadastrarDespesas()
    if o == 3:
        GerarRelatorio()
    input("\nAperte 'ENTER' Para Continuar\n")

print("OBRIGADO POR USAR O SISTEMA")

from datetime import datetime

def validar_entrada_int(prompt, min_value, max_value):
    while True:
        try:
            value = int(input(prompt))
            if min_value <= value <= max_value:
                return value
            else:
                print(f"Por favor, insira um valor entre {min_value} e {max_value}.")
        except ValueError:
            print("Entrada inválida. Tente novamente.")

def validar_data(prompt):
    while True:
        try:
            data = input(prompt)
            return datetime.strptime(data, "%d/%m/%Y")
        except ValueError:
            print("Formato de data inválido. Tente novamente no formato DD/MM/YYYY.")

horarioinicial = 0
horariofinal = 0
tarifag = 0
tarifap = 0
tarifav = 0
tarifagadd = 0
tarifapadd = 0
tarifavadd = 0
tarifatotal = 0
option = 0 
usuario = ""
valortotal = 0
formapagamento = 0
impressoesq = 0
totalarrecadado = 0
vtarrecadado = 0
ttuso = 0
totaldias = 0
quantidadeg = 0
quantidadep = 0
quantidadev = 0
vmedio = 0

while option != 6:
    formapagamento = 0
    print("---------------------------------------------")
    print(" 1.Cadastrar Tarifas")
    print("\n 2.Registrar Início de Impressão")
    print("\n 3.Registrar Fim de Impressão")
    print("\n 4.Gerar Relatório Diário")
    print("\n 5.Gerar Relatório por tipo de usuário")
    print("\n 6. Sair")
    print("---------------------------------------------")
    option = int(input("\n Escolha uma das opções: "))

    if option == 1:
        print("-------------------------------------------------------------------------------")
        print("\n Cadastrar Tarifas")
        tarifag = float(input("Insira o valor para alunos de graduação: "))
        tarifap = float(input("Insira o valor para professor: "))
        tarifav = float(input("Insira o valor para visitantes: "))
        tarifagadd = float(input("Insira o valor para horas adicionais para aluno: "))
        tarifapadd = float(input("Insira o valor para horas adicionais para professores: "))
        tarifavadd = float(input("Insira o valor para horas adicionais para Visitantes: "))
        print("-------------------------------------------------------------------------------")

    elif option == 2:
        print("--------------------------------------------------------------------------------")
        print("\n Registro inicial")
        nome = input("Qual seu Nome: ")
        idade = int(input("Qual sua Idade: "))
        email = input("Qual seu email: ")
        usuario = input("Qual seu tipo de usuário (G/P/V): ").upper()
        datainicial = validar_data("Qual data de início da impressão (DD/MM/YYYY): ")
        horarioinicial = validar_entrada_int("Qual horário de início da impressão (0-23): ", 0, 23)
        print("-----------------------------------------------------------------------------------")

    elif option == 3:
        print("------------------------------------------------------------------")
        print("\n Registro final")
        horariofinal = validar_entrada_int("Digite o horário final de uso (0-23): ", 0, 23)
        datafinal = validar_data("Digite a data final de uso (DD/MM/YYYY): ")
        totalhoras = horariofinal - horarioinicial
        totaldias = (datafinal - datainicial).days
        print("O total de dias usados foi de:", totaldias)
        print("O total de horas usadas foi de:", totalhoras)
        print("------------------------------------------------------------------")

        if usuario == "G":
            valortotal = 0
            ttuso = totalhoras
            quantidadeg += 1
            valortotal = 1 * tarifag + (totalhoras-1) * tarifagadd if totalhoras > 1 else tarifag
            print("\n O valor total a ser pago é de: ", valortotal)

        elif usuario == "P":
            ttusop = totalhoras
            valortotal = 0
            quantidadep += 1
            valortotal = 1 * tarifap + (totalhoras-1) * tarifapadd if totalhoras > 1 else tarifap
            print("\n O valor total a ser pago é de: ", valortotal)

        elif usuario == "V":
            ttusov = totalhoras
            valortotal = 0
            quantidadev += 1
            valortotal = 1 * tarifav + (totalhoras-1) * tarifavadd if totalhoras > 1 else tarifav
            print("\n O valor total a ser pago é de: ", valortotal)

        impressoesq += 1
        ttuso += totalhoras

        while formapagamento != 3:
            print("\n Forma de Pagamento")
            print("\n[1] PIX")
            print("\n[2] CARTÃO DE CRÉDITO")
            print("\n[3] OUTRA FORMA")

            formapagamento = int(input("Escolha uma das opções: "))

            if formapagamento == 1:
                print("\n Forma de Pagamento: PIX")
                valortotal = valortotal * 0.95
                print("O valor a ser pago é de R$: ", valortotal)
                break

            elif formapagamento == 2:
                print("\n Forma de Pagamento: CARTÃO DE CRÉDITO")
                valortotal = valortotal * 1.05
                print("O valor a ser pago é de R$: ", valortotal)
                break

            elif formapagamento == 3:
                print("\n Forma de Pagamento: OUTRA")
                print("\n O valor a ser pago é de R$:", valortotal)
                break
        vtarrecadado += valortotal
        vmediog = vtarrecadado / quantidadeg if quantidadeg > 0 else 0
        vmediop = vtarrecadado / quantidadep if quantidadep > 0 else 0
        vmediov = vtarrecadado / quantidadev if quantidadev > 0 else 0

    elif option == 4:
        print("\n Relatório diário")
        print("\n Impressões realizadas no dia foi de: ", impressoesq)

        if impressoesq > 0:
            print("\n O tempo médio de uso na impressora foi de:", ttuso / impressoesq)
        else:
            print("A impressora ainda não foi usada")

        print("\n O valor total arrecadado foi de:", vtarrecadado)

    elif option == 5:
        print("\n \t \t Relatório por Tipo de Usuário ")
        print("----------------------------------------------------------------")
        print("Quantidade utilizada por alunos: ", quantidadeg)
        print("Valor médio gasto por alunos: ", vmediog)
        print("----------------------------------------------------------------")
        print("Quantidade utilizada por professores: ", quantidadep)
        print("Valor médio gasto por professores: ", vmediop)
        print("----------------------------------------------------------------")
        print("Quantidade utilizada por Visitantes: ", quantidadev)
        print("O Valor médio utilizado por visitantes: ", vmediov)
        print("----------------------------------------------------------------")

    elif option == 6:
        print("Sair")

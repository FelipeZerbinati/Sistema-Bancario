saldo = 0
numero_saques = 0
LIMITE_SAQUE = 3
transacoes = []

def menu():
    print("""             |Bem Vindo ao Sistema Bancário!|
             | [S] Saque   | [D] Depositar  |
             | [E] Extrato | [Q] Sair       |""")
    

def depositar():
    global saldo
    print("|Depósito|")
    valor_adicionar = float(input("Digite o valor a ser depositado: "))
    if valor_adicionar > 0:
        saldo += valor_adicionar
        valor_formatado_adicionar = "{:.2f}".format(valor_adicionar)
        transacoes.append(f"Depósito: + R${valor_formatado_adicionar}")
    else:
        print("Valor inválido! Tente novamente.")
        return saldo, "0.00"
    return saldo, valor_formatado_adicionar


def saque():
    global saldo, numero_saques
    print("|Saque|")
    valor_retirar = float(input("Digite o valor a ser sacado: "))
    if valor_retirar > 0 and valor_retirar <= 500 and numero_saques < LIMITE_SAQUE:
        if valor_retirar <= saldo:
            saldo -= valor_retirar
            numero_saques += 1
            valor_formatado_retirar = "{:.2f}".format(valor_retirar)
            transacoes.append(f"Saque: - R${valor_formatado_retirar}")
        else:
            print("Saldo insuficiente.")
            return saldo, "0.00"
    else:
        print("Saque inválido! Tente novamente.")
        return saldo, "0.00"
    return saldo, valor_formatado_retirar


def extrato():
    global saldo
    print("|Extrato|")
    print(f"Seu saldo é: R$ {saldo:.2f}")
    if saldo == 0:
        print("Nenhuma transação realizada.")
    else:
        print("Transações realizadas:")
        for transacao in transacoes:
            print(transacao)

def main():
    while True:
        menu()
        opcao = input("Digite uma opção: ").upper()
        if opcao == "S":
            saldo, valor_formatado_retirar = saque()
        elif opcao == "D":
            saldo, valor_formatado_adicionar = depositar()
        elif opcao == "E":
            extrato()
        elif opcao == "Q":
            print("Obrigado por utilizar o sistema!")
            break
        else:
            print("Por favor, digite uma opção válida!")

if __name__ == "__main__":
    main()

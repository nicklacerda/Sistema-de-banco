import random
import os

#NÚMERO DA CONTA

def gerar_numero_da_conta():
    return  random.randint(1000,10000)

# numero_da_conta = []
# if numero_da_conta == []:
#     numero_da_conta.append(gerar_numero_da_conta())
# else:
#     numero_da_conta.remove[1]
#MENU

def menu():
    while True:
        print('MACK BANK – ESCOLHA UMA OPÇÃO'
              '\n')
        print('(1) CADASTRAR CONTA CORRENTE')
        print('(2) DEPOSITAR')
        print('(3) SACAR')
        print('(4) CONSULTAR SALDO')
        print('(5) CONSULTAR EXTRATO')
        print('(6) FINALIZAR'
              '\n')
        opcao = input('SUA OPÇÃO: ')

        if opcao == "1":
            cadastrar_conta_corrente()
        elif opcao == "2":
            depositar()
        elif opcao == "3":
            sacar()
        elif opcao == "4":
            consultar_saldo()
        elif opcao == "5":
            consultar_extrato()
        elif opcao == "6":
            print("Finalizando o programa...")
            break
        else:
            print("Opção inválida. Por favor, escolha uma opção válida.")


# CADASTRO

def cadastrar_conta_corrente():
    numero_da_conta = gerar_numero_da_conta()
    cadastro_salvo = 0
    os.system('cls')
    while True:
        print(f'NÚMERO DA CONTA: {numero_da_conta}')

        if cadastro_salvo >= 1:
            print(f'NOME DO CLIENTE: {nome_cliente}')
            pass
        else:
            nome_cliente = input('NOME DO CLIENTE: ')
            if nome_cliente == '':
                print('-'*33,'\n','ESTE CAMPO PRECISA SER PREENCHIDO','\n','-'*33)
                continue
            else:
                cadastro_salvo += 1
        
        if cadastro_salvo >= 2:
            print(f'TELEFONE.......:  {telefone}')
            pass
        else:
            telefone = input('TELEFONE.......: ')
            if telefone == '':
                print('-'*33,'\n','ESTE CAMPO PRECISA SER PREENCHIDO','\n','-'*33)
                continue
            else:
                cadastro_salvo += 1


        if cadastro_salvo >= 3:
            print(f'EMAIL..........:  {email}')
            pass
        else:
            email = input('EMAIL..........: ')
            if email == '':
                print('-'*33,'\n','ESTE CAMPO PRECISA SER PREENCHIDO','\n','-'*33)
                continue
            else:
                cadastro_salvo += 1


        if cadastro_salvo >= 4:
            print(f'SALDO INICIAL...:  {saldo_inicial}')
            pass
        else:
            saldo_inicial = float(input('SALDO INICIAL...: '))
            if saldo_inicial < 1000:
                print('-'*49,'\n','O SALDO INICIAL NÃO PODE SER INFERIOR A R$1000,00','\n','-'*49) 
                continue
            else:
                cadastro_salvo += 1


        if cadastro_salvo >= 5:
            print(f'LIMITE DE CRÉDITO: {limite_de_credito}')
            pass
        else:
            limite_de_credito = float(input('LIMITE DE CRÉDITO: '))
            if limite_de_credito < 0:
                print('-'*49,'\n','O LIMITE DE CRÉDITO NÃO PODE SER MENOR QUE R$0,00','\n','-'*49)
                continue
            else:
                cadastro_salvo += 1

        if cadastro_salvo >= 6:
            print(f'SENHA............: {senha}')
            pass
        else:
            senha = input('SENHA (6 CARACTERES): ')
            if len(senha) < 6 or len(senha) > 6:
                print('-'*37,'\n','A SENHA DEVE CONTER APENAS 6 CARACTERES','\n','-'*37)
                continue
            else:
                cadastro_salvo += 1

        if cadastro_salvo >= 7:
            print(f'REPITA A SENHA...: {repetir_senha}')
            pass
        else:
            repetir_senha = input('REPITA A SENHA...: ')
            if repetir_senha != senha:
                print('-'*23,'\n','AS SENHAS NÃO COINCIDEM','\n','-'*23)
                continue
            else:
                os.system('cls')
                fim_cadastro = input('CADASTRO REALIZADO! PRESSIONE *enter* PARA VOLTAR AO MENU...')
                if fim_cadastro == '':
                    menu()
                    break
                else:
                    menu()
                    break

        cadastro = {
            'numero_da_conta': numero_da_conta,
            'nome': nome_cliente,
        }
        
        return cadastro


#DEPOSITO
def depositar(cadastro):
    os.system('cls')
    while True:

        numero_da_conta = cadastro['numero_da_conta']
        print(numero_da_conta)
        numero_digitado = input('DIGITE O NÚMERO DA CONTA: ')
        if numero_digitado == numero_da_conta:
            print('NÚMERO DA CONTA CORRETO!!')
            continue
        else:
            print('TEM PARADA ERRADA AÍ MERMAO')
            continue



#SAQUE
def sacar():
    a = input('digita ai: ')
    print(a)

menu()

#CONSULTAR SALDO

def consultar_saldo():
    pass

def consultar_extrato():
    pass
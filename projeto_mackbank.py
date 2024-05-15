import random
import os

#MENU

dados_cadastro = []
conta_bloqueada = False
dados_extrato = []
def menu():
    while True:
        if conta_bloqueada == False:
            print()
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
        else:
            print()
            print('MACK BANK – ESCOLHA UMA OPÇÃO'
                '\n')
            print('(1) CADASTRAR CONTA CORRENTE')
            print('(2) DEPOSITAR')
            print('(̶3̶)̶ S̶A̶C̶A̶R̶  : OPÇÃO BLOQUEADA')
            print('(̶4̶)̶ C̶O̶N̶S̶U̶L̶T̶A̶R̶ S̶A̶L̶D̶O̶  : OPÇÃO BLOQUEADA')
            print('(̶5̶)̶ C̶O̶N̶S̶U̶L̶T̶A̶R̶ E̶X̶T̶R̶A̶T̶O̶  : OPÇÃO BLOQUEADA')
            print('(6) FINALIZAR'
                '\n')
            opcao = input('SUA OPÇÃO: ')
            if opcao == "1":
                cadastrar_conta_corrente()
            elif opcao == "2":
                depositar()
            elif opcao == "6":
                os.system('cls||clear')
                print("FINALIZANDO PROGRAMA...")
                print('PROGRAMA FINALIZADO. OBRIGADO POR ACESSAR O MACKBANK!')
                break
            else:
                print("Opção inválida. Por favor, escolha uma opção válida.")

# CADASTRO

def cadastrar_conta_corrente():
    numero_da_conta = random.randint(1000,10000)
    cadastro_salvo = 0
    os.system('cls||clear')

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
        dados_extrato.append(- saldo_inicial)

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

        dados_cadastro.extend([numero_da_conta, nome_cliente, telefone, email, saldo_inicial, limite_de_credito, senha])        

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


#DEPOSITO
def depositar():
    os.system('cls||clear')
    numero_certo = dados_cadastro[0]
    nome_cliente = dados_cadastro[1]
    print(numero_certo)
    while True:
        numero_digitado = int(input('DIGITE O NÚMERO DA CONTA: '))
        print(f'Número digitado: {numero_digitado}')
        if numero_certo == numero_digitado:
            print(f'NOME DO CLIENTE: {nome_cliente}')
            while True:
                deposito = float(input('VALOR DO DEPÓSITO: '))
                if deposito <= 0:
                    print('O VALOR DO DEPÓSITO DEVE SER MAIOR QUE R$0,00')
                    continue
                else:
                    confirmar_deposito = input(f'CONFIRMAR DEPÓSITO NO VALOR DE {deposito} ? SIM(S) NÃO(N): ').upper()
                    if confirmar_deposito == 'S':
                        saldo_inicial = dados_cadastro[4]
                        saldo_atual = saldo_inicial + deposito
                        dados_cadastro[4] = saldo_atual
                        voltando_menu = input('DEPÓSITO CONFIRMADO! PRESSIONE *ENTER* PARA VOLTAR AO MENU')
                        if voltando_menu == '':
                            menu()
                            break
                        else:
                            menu()
                            break
                    else:
                        continue
            
        else:
            alerta = 'NÚMERO DE CONTA INEXISTENTE'
            print(len(alerta)*'-')
            print(alerta)
            print(len(alerta)*'-')
            continue



#SAQUE
def sacar():
    os.system('cls||clear')
    numero_certo = dados_cadastro[0]
    nome_cliente = dados_cadastro[1]
    senha_certa = dados_cadastro[6]
    saldo_inicial = dados_cadastro[4]
    credito = dados_cadastro[5]
    senha_acertada = 0
    tentativas = 0
    usando_credito_e_saldo = False
    usando_credito = False
    tentativas_erro = 3
    print(numero_certo)
    while True:
        if tentativas > 3 :
                    print('VOCÊ ATINGIU O LIMITE DE TENTATIVAS. SUA CONTA SERÁ BLOQUEADA E VOCÊ SERÁ REDIRECIONADO AO MENU', '\n')
                    global conta_bloqueada
                    conta_bloqueada = True
                    menu()
                    break
        numero_digitado = int(input('DIGITE O NÚMERO DA CONTA: '))
        print(f'Número digitado: {numero_digitado}')
        if numero_certo == numero_digitado:
            print(f'NOME DO CLIENTE: {nome_cliente}')
            while tentativas <= 3:
                if senha_acertada > 0:
                    pass
                else:
                    senha = input('DIGITE A SENHA: ')
                if senha == senha_certa:
                    senha_acertada += 1
                    saque  = float(input('DIGITE O VALOR DO SAQUE: '))
                    if  saque <= 0:
                        print('O VALOR DO SAQUE DEVE SER MAIOR QUE R$0,00')
                        continue
                    elif saque <= saldo_inicial:
                        usando_credito = False
                        usando_credito_e_saldo = False
                    elif saque > saldo_inicial and saque <= (saldo_inicial + credito):
                        print('VOCÊ ESTÁ USANDO TODO SEU SALDO E O SEU LIMITE DE CRÉDITO')
                        usando_credito_e_saldo = True
                    elif saque > saldo_inicial and saque <= credito :
                        print('VOCÊ ESTÁ USANDO O SEU LIMITE DE CRÉDITO')
                        usando_credito = True
                    elif saque > saldo_inicial and saque > credito:
                        print('VOCÊ NÃO POSSUI SALDO SUFICIENTE PARA ESSA TRANSAÇÃO')
                        continue
                    if saque <= saldo_inicial or usando_credito_e_saldo == True or usando_credito == True:
                        confirmar_saque = input(f'CONFIRMAR SAQUE NO VALOR DE {saque} ? SIM(S) NÃO(N): ').upper()
                        if confirmar_saque == 'S':
                            if usando_credito == True:
                                credito_atual = credito - saque
                                dados_cadastro[5] = credito_atual
                            elif usando_credito_e_saldo == True:
                                dados_cadastro[4] = 0
                                credito_atual = credito - saque
                                dados_cadastro[5] = credito_atual
                            else:
                                saldo_atual = saldo_inicial - saque
                                dados_cadastro[4] = saldo_atual
                            voltando_menu = input('SAQUE CONFIRMADO! PRESSIONE *ENTER* PARA VOLTAR AO MENU')
                            if voltando_menu == '':
                                menu()
                                break
                            else:
                                menu()
                                break
                        else:
                            continue
                else:
                    tentativas_erro -= 1
                    if tentativas_erro >= 0:
                        print(f'SENHA INCORRETA - VOCÊ POSSUI MAIS {tentativas_erro} TENTATIVAS ANTES DA SUA CONTA SER BLOQUEADA')
                    tentativas += 1
                    continue
            
        else:
            alerta = 'NÚMERO DE CONTA INEXISTENTE'
            print(len(alerta)*'-')
            print(alerta)
            print(len(alerta)*'-')
            continue


#CONSULTAR SALDO

def consultar_saldo():
    os.system('cls||clear')
    nome_cliente = dados_cadastro[1]
    numero_certo = dados_cadastro[0]
    senha_certa = dados_cadastro[6]
    tentativas = 0
    tentativas_erro = 3
    print(f'{numero_certo}')
    while True:
        if tentativas > 3 :
                    print('VOCÊ ATINGIU O LIMITE DE TENTATIVAS. SUA CONTA SERÁ BLOQUEADA E VOCÊ SERÁ REDIRECIONADO AO MENU', '\n')
                    global conta_bloqueada
                    conta_bloqueada = True
                    menu()
                    break
        numero_digitado = int(input('DIGITE O NÚMERO DA CONTA: '))
        print(f'Número digitado: {numero_digitado}')
        if numero_certo == numero_digitado:
            print(f'NOME DO CLIENTE: {nome_cliente}')
            while tentativas <= 3:
                senha = input('DIGITE A SENHA: ')
                if senha == senha_certa:

                    print(f'SALDO DA CONTA: R${dados_cadastro[4]}')
                    print(f'SALDO DE CRÉDITO: {dados_cadastro[5]}')
                    voltar_ao_menu = input('PRESSIONE *ENTER* PARA VOLTAR AO MENU: ')
                    if voltar_ao_menu == '':
                        menu()
                        break
                    else:
                        menu()
                        break   

                else:
                    tentativas_erro -= 1
                    if tentativas_erro >= 0:
                        print(f'SENHA INCORRETA - VOCÊ POSSUI MAIS {tentativas_erro} TENTATIVAS ANTES DA SUA CONTA SER BLOQUEADA')
                    tentativas += 1
                    continue

        else:
            alerta = 'NÚMERO DE CONTA INEXISTENTE'
            print(len(alerta)*'-')
            print(alerta)
            print(len(alerta)*'-')
            continue

def consultar_extrato():
    os.system('cls||clear')
    nome_cliente = dados_cadastro[1]
    numero_certo = dados_cadastro[0]
    senha_certa = dados_cadastro[6]
    tentativas = 0
    tentativas_erro = 3
    print(f'{numero_certo}')
    while True:
        if tentativas > 3 :
                    print('VOCÊ ATINGIU O LIMITE DE TENTATIVAS. SUA CONTA SERÁ BLOQUEADA E VOCÊ SERÁ REDIRECIONADO AO MENU', '\n')
                    global conta_bloqueada
                    conta_bloqueada = True
                    menu()
                    break
        numero_digitado = int(input('DIGITE O NÚMERO DA CONTA: '))
        print(f'Número digitado: {numero_digitado}')
        if numero_certo == numero_digitado:
            print(f'NOME DO CLIENTE: {nome_cliente}')
            while tentativas <= 3:
                senha = input('DIGITE A SENHA: ')
                if senha == senha_certa:

                    print(f'SALDO DA CONTA: R${dados_cadastro[4]}')
                    print(f'SALDO DE CRÉDITO: {dados_cadastro[5]}')
                    voltar_ao_menu = input('PRESSIONE *ENTER* PARA VOLTAR AO MENU: ')
                    if voltar_ao_menu == '':
                        menu()
                        break
                    else:
                        menu()
                        break   

                else:
                    tentativas_erro -= 1
                    if tentativas_erro >= 0:
                        print(f'SENHA INCORRETA - VOCÊ POSSUI MAIS {tentativas_erro} TENTATIVAS ANTES DA SUA CONTA SER BLOQUEADA')
                    tentativas += 1
                    continue

        else:
            alerta = 'NÚMERO DE CONTA INEXISTENTE'
            print(len(alerta)*'-')
            print(alerta)
            print(len(alerta)*'-')
            continue

menu()

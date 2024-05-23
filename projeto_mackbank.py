#POR FAVOR UTILIZE O COMANDO 'pip install keyboard' NO SEU TERMINAL ANTES DE RODAR O CÓDIGO

import keyboard
import sys
import time
import random
import os

#SENHA DIGITADA COMO *

def senha_digitada(prompt="Password: "):
    print(prompt, end="", flush=True)
    senha = ""
    while True:
        event = keyboard.read_event(suppress=True)  # Suprimir o evento para evitar saída duplicada
        if event.event_type == keyboard.KEY_DOWN:
            if event.name == "enter":
                break
            elif event.name == "backspace":
                if senha:
                    senha = senha[:-1]
                    sys.stdout.write("\b \b")
                    sys.stdout.flush()
            else:
                if len(event.name) == 1:  # Garantir que seja um único caractere
                    senha += event.name
                    sys.stdout.write("*")
                    sys.stdout.flush()
        time.sleep(0.01)
    print()  # Ir para a próxima linha após a entrada da senha
    return senha

#MENU

dados_cadastro = []
conta_bloqueada = False
dados_extrato = []
validacao_menu = False

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
            elif opcao == "2" and validacao_menu == True:
                depositar()
            elif opcao == "3" and validacao_menu == True:
                sacar()
            elif opcao == "4" and validacao_menu == True:
                consultar_saldo()
            elif opcao == "5" and validacao_menu == True:
                consultar_extrato()
            elif opcao == "6":
                os.system('cls||clear')
                print('-'*17)
                print('MACK BANK – SOBRE')
                print('-'*17)
                print('\nEste pograma foi desenvolvido por:')
                print('Nicolas Oliveira Lacerda')
                print('RA: 10425260')
                exit('MUITO OBRIGADO POR ACESSAR O MACKBANK! VOLTE SEMPRE!\n')
            else:
                print("OPÇÃO INVÁLIDA. POR FAVOR, ESCOLHA UMA OPÇÃO VÁLIDA.")
        else:
            print()
            print('MACK BANK – ESCOLHA UMA OPÇÃO'
                '\n')
            print('(1) CADASTRAR CONTA CORRENTE')
            print('(2) DEPOSITAR')
            print('(̶3̶)̶ S̶A̶C̶A̶R̶  : OPÇÃO BLOQUEADA')
            print('(̶4̶)̶ C̶O̶N̶S̶U̶L̶T̶A̶R̶ S̶A̶L̶D̶O̶  : OPÇÃO BLOQUEADA')
            print('(̶5̶)̶ C̶O̶N̶S̶U̶L̶T̶A̶R̶ E̶X̶T̶R̶A̶T̶O̶  : OPÇÃO BLOQUEADA')
            print('(6) DESBLOQUEAR CONTA')
            print('(7) FINALIZAR'
                '\n')
            opcao = input('SUA OPÇÃO: ')
            if opcao == "1":
                cadastrar_conta_corrente()
            elif opcao == "2":
                depositar()
            elif opcao == '6':
                desbloquear_conta()
            elif opcao == "7":
                os.system('cls||clear')
                print('-'*17)
                print('MACK BANK – SOBRE')
                print('-'*17)
                print('\nEste pograma foi desenvolvido por:')
                print('Nicolas Oliveira Lacerda')
                print('RA: 10425260')
                exit('MUITO OBRIGADO POR ACESSAR O MACKBANK! VOLTE SEMPRE!\n')
            else:
                print("OPÇÃO INVÁLIDA. POR FAVOR, ESCOLHA UMA OPÇÃO VÁLIDA.")

# CADASTRO

def cadastrar_conta_corrente():
    numero_da_conta = random.randint(1000,10000)
    token_recuperacao = random.randint(10000000,99999999)
    cadastro_salvo = 0
    os.system('cls||clear')
    boas_vindas = 'BEM VINDO AO MACKBANK!'
    print(len(boas_vindas)*'-')
    print(boas_vindas)
    print(len(boas_vindas)*'-')
    

    while True:
        print(f'NÚMERO DA CONTA: {numero_da_conta}')

        if cadastro_salvo >= 1:
            print(f'NOME DO CLIENTE: {nome_cliente}')
            pass
        else:
            nome_cliente = input('NOME DO CLIENTE: ')
            if nome_cliente == '':
                print('-'*33,'\nESTE CAMPO PRECISA SER PREENCHIDO\n','-'*33)
                continue
            else:
                cadastro_salvo += 1
        
        if cadastro_salvo >= 2:
            print(f'TELEFONE.......:  {telefone}')
            pass
        else:
            telefone = input('TELEFONE.......: ')
            if telefone == '':
                print('-'*33,'\nESTE CAMPO PRECISA SER PREENCHIDO\n','-'*33)
                continue
            else:
                cadastro_salvo += 1


        if cadastro_salvo >= 3:
            print(f'EMAIL..........:  {email}')
            pass
        else:
            email = input('EMAIL..........: ')
            if email == '':
                print('-'*33,'\nESTE CAMPO PRECISA SER PREENCHIDO\n','-'*33)
                continue
            else:
                cadastro_salvo += 1


        if cadastro_salvo >= 4:
            print(f'SALDO INICIAL...:  {saldo_inicial}')
            pass
        else:
            saldo_inicial = float(input('SALDO INICIAL...: '))
            if saldo_inicial < 1000:
                print('-'*49,'\nO SALDO INICIAL NÃO PODE SER INFERIOR A R$1000,00\n','-'*49) 
                continue
            else:
                cadastro_salvo += 1

        if cadastro_salvo >= 5:
            print(f'LIMITE DE CRÉDITO: {limite_de_credito}')
            pass
        else:
            limite_de_credito = float(input('LIMITE DE CRÉDITO: '))
            if limite_de_credito < 0:
                print('-'*49,'\nO LIMITE DE CRÉDITO NÃO PODE SER MENOR QUE R$0,00\n','-'*49)
                continue
            else:
                cadastro_salvo += 1

        if cadastro_salvo >= 6:
            print('SENHA............: ******')
            pass
        else:
            senha = senha_digitada('SENHA (6 CARACTERES): ')
            if len(senha) < 6 or len(senha) > 6:
                print('-'*37,'\nA SENHA DEVE CONTER APENAS 6 CARACTERES\n','-'*37)
                continue
            else:
                cadastro_salvo += 1

        dados_cadastro.extend([numero_da_conta, nome_cliente, telefone, email, saldo_inicial, limite_de_credito, senha, token_recuperacao])        

        if cadastro_salvo >= 7:
            print(f'REPITA A SENHA...: {repetir_senha}')
            pass
        else:
            repetir_senha = senha_digitada('REPITA A SENHA...: ')
            if repetir_senha != senha:
                print('-'*23,'\nAS SENHAS NÃO COINCIDEM','\n','-'*23)
                continue
            else:
                os.system('cls')
                print(f'SALVE O NÚMERO DA SUA CONTA: {numero_da_conta}')
                print(f'SALVE O TOKEN DE RECUPERAÇÃO DA CONTA EM CASO DE BLOQUEIO: {token_recuperacao}')
                print('VOCÊ SÓ PODERÁ DESBLOQUEAR A CONTA COM O TOKEN DE RECUPERAÇÃO')
                fim_cadastro = input('CADASTRO REALIZADO! PRESSIONE *enter* PARA VOLTAR AO MENU...')
                global validacao_menu
                validacao_menu = True
                if fim_cadastro == '':
                    os.system('cls||clear')
                    menu()
                    break
                else:
                    os.system('cls||clear')
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
                        dados_extrato.append(deposito)
                        saldo_inicial = dados_cadastro[4]
                        saldo_atual = saldo_inicial + deposito
                        dados_cadastro[4] = saldo_atual
                        voltando_menu = input('DEPÓSITO CONFIRMADO! PRESSIONE *ENTER* PARA VOLTAR AO MENU')
                        if voltando_menu == '':
                            os.system('cls||clear')
                            menu()
                            break
                        else:
                            os.system('cls||clear')
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
        if numero_certo == numero_digitado:
            print(f'NOME DO CLIENTE: {nome_cliente}')
            while tentativas <= 3:
                if senha_acertada > 0:
                    pass
                else:
                    senha = senha_digitada('DIGITE A SENHA: ')
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
                    elif saque > saldo_inicial and saque > credito:
                        print('VOCÊ NÃO POSSUI SALDO SUFICIENTE PARA ESSA TRANSAÇÃO')
                        continue
                    if saque <= saldo_inicial or usando_credito_e_saldo == True:
                        confirmar_saque = input(f'CONFIRMAR SAQUE NO VALOR DE {saque} ? SIM(S) NÃO(N): ').upper()
                        if confirmar_saque == 'S':
                            dados_extrato.append(-saque)
                            if usando_credito == True:
                                credito_atual = credito - saque
                                dados_cadastro[5] = credito_atual
                            elif usando_credito_e_saldo == True:
                                saldo_atual = saldo_inicial - saque
                                dados_cadastro[4] = saldo_atual
                                credito_atual = credito - (saque - saldo_inicial)
                                dados_cadastro[5] = credito_atual
                            else:
                                saldo_atual = saldo_inicial - saque
                                dados_cadastro[4] = saldo_atual
                            voltando_menu = input('SAQUE CONFIRMADO! PRESSIONE *ENTER* PARA VOLTAR AO MENU')
                            if voltando_menu == '':
                                os.system('cls||clear')
                                menu()
                                break
                            else:
                                os.system('cls||clear')
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
        if numero_certo == numero_digitado:
            print(f'NOME DO CLIENTE: {nome_cliente}')
            while tentativas <= 3:
                senha = senha_digitada('DIGITE A SENHA: ')
                if senha == senha_certa:

                    print(f'SALDO DA CONTA: R${dados_cadastro[4]}'
                          '\n')
                    if dados_cadastro[4] < 0:
                        print('SUA CONTA ESTÁ COM SALDO NEGATIVO')
                    print(f'SALDO DE CRÉDITO: {dados_cadastro[5]}')
                    voltar_ao_menu = input('PRESSIONE *ENTER* PARA VOLTAR AO MENU: ')
                    if voltar_ao_menu == '':
                        os.system('cls||clear')
                        menu()
                        break
                    else:
                        os.system('cls||clear')
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
        if numero_certo == numero_digitado:
            print(f'NOME DO CLIENTE: {nome_cliente}')
            while tentativas <= 3:
                senha = senha_digitada('DIGITE A SENHA: ')
                if senha == senha_certa:
                    print(f'SALDO DE CRÉDITO: {dados_cadastro[5]}')
                    for valores in dados_extrato:
                        if valores < 0:
                            print(f'SAQUE REALIZADO NO VALOR DE R${-valores}'
                                  '\n')
                        else:
                            print(f'DEPÓSITO REALIZADO NO VALOR DE R${valores}'
                                  '\n')
                    print(f'SALDO DA CONTA: {dados_cadastro[4]}')
                    if dados_cadastro[4] < 0:
                        print('ATENÇÃO AO SEU SALDO!!')
                    voltar_ao_menu = input('PRESSIONE *ENTER* PARA VOLTAR AO MENU: ')
                    if voltar_ao_menu == '':
                        os.system('cls||clear')
                        menu()
                        break
                    else:
                        os.system('cls||clear')
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

def desbloquear_conta():
    os.system('cls||clear')
    numero_certo = dados_cadastro[0]
    token_certo = dados_cadastro[7]
    print(dados_cadastro[0])
    while True:
        numero_digitado = int(input('DIGITE O NÚMERO DA CONTA: '))
        if numero_certo == numero_digitado:
            print(f'NOME DO CLIENTE: {dados_cadastro[1]}')
            token_digitado = int(input('DIGITE O TOKEN PARA RECUPERAÇÃO DA CONTA: '))
            if token_digitado == token_certo:
                while True:
                    nova_senha = senha_digitada('DIGITE A NOVA SENHA (6 CARACTERES): ')
                    if nova_senha == '' or len(nova_senha) > 6 or len(nova_senha) < 6:
                        print('A SENHA DIGITADA NÃO ATENDE AOS PADRÕES EXIGIDOS. POR FAVOR DIGITE UMA SENHA VÁLIDA')
                        continue
                    else:
                        confirmar_senha = senha_digitada('CONFIRME A SENHA: ')
                        if nova_senha == confirmar_senha:
                            print('SENHA ATUALIZADA COM SUCESSO!\n')
                            dados_cadastro[6] = nova_senha
                            global conta_bloqueada
                            conta_bloqueada = False
                            voltar_ao_menu = input('PRESSIONE *ENTER* PARA VOLTAR AO MENU: ')
                            if voltar_ao_menu == '':
                                os.system('cls||clear')
                                menu()
                                break
                            else:
                                os.system('cls||clear')
                                menu()
                                break 
                        else:
                            print('AS SENHAS NÃO COINCIDEM')
                            continue
            else:
                print('NÚMERO DE TOKEN INVÁLIDO. DIGITE UM NÚMERO DE TOKEN VÁLIDO PARA PROSSEGUIR')
                continue
        else:
            print('NÚMERO DE CONTA INEXISTENTE. DIGITE UM NÚMERO VÁLIDO PARA PROSSEGUIR')
            continue
        pass

menu()

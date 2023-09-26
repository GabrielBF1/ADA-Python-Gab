import os 
from cliente import *



option = 0
os.system('cls')
while option != 5:
    print("Bem vindo a Carteira xxxx")
    option = input("\nPor favor selecione a opcao desejada:\n \t1 - Cliente\n \t2 - Ordem\n \t3 - Realizar analise da carteira\n \t4 - Imprimir relatorio da carteira ou Consultar relatorio da acao\n \t5 - Sair\n")
    while (not option.isdigit()):
           print("\nOpcao digitada nao existe, favor selecionar uma opcao valida...")
           option = input("Por favor selecione a opcao desejada:\n \t1 - Cliente\n \t2 - Ordem\n \t3 - Realizar analise da carteira\n \t4 - Imprimir relatorio da carteira ou Consultar relatorio da acao\n \t5 - Sair\n")    
    option = int(option)
    if option == 1:
       menu_customer()
    elif option == 2:
        os.system('cls')
        print("Preencha os campos a seguir para cadastrar uma nova Ordem")
        order_name = input("\n\tNome da ordem: " )
        ticket = input("\tTicket: ")
        buy_price = input("\tValor da compra: ")
        buy_quantity = input("\tQuantidade compra: ")
        buy_date = input("\tData da compra: ")
        while (not validate_date(buy_date, False)):
            buy_date = input("\tData da compra: ")
        client_id = input("\tID do cliente: ")
    elif option == 3:
        print("Realizar analise da carteira")
    elif option == 4:
        print("imprimir relatorio da carteira ou Consultar relatorio da acao")
    elif option == 5:
        exit_program()
    else:
        print("\n\tOpcao invalida, por favor selecione alguma opcao valida: ")


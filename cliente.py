from utils import *
from database import *

def menu_customer():
    menu_control = True
    customer_list = []

    while menu_control:
        customer_option = int(input("Digite a opção desejada do menu cliente: \n \t1 - Cadastrar Cliente\n \t2 - Consultar Cliente\n \t3 - Atualizar Cliente\n \t4 - Deletar Cliente\n \t5 - Lista de clientes\n \t6 - Voltar\n"))
        if customer_option == 1:
            os.system('cls')
            print("Informe os campos abaixo para cadastrar um novo cliente:\n")
            name = input("\tNome: ")
            CPF = validate_cpf(input("\tCPF: "))
            RG = validate_rg(input("\tRG: "))            
            birth_date = validate_date(input("\tData de nascimento: "), True)
            CEP = buscar_cep(input("\tCEP: "))
            house_number = input("\tNumero residencia: ")
            while (not house_number.isdigit()):
                print("Insira apenas numeros")
                house_number = input("\tDigite da residencia: ")
            customer_dict = {
                "Nome": name,
                "CPF": CPF,
                "RG": RG,
                "Nascimento": birth_date,
                "Endereco": str(CEP),
                "Numero": house_number
            }
            insert_banco_dados(customer_dict)
            customer_list.append(customer_dict)
            print("\nCliente " + name + " cadastrado com sucesso!!\n")
        elif customer_option == 2:
            CPF = validate_cpf(input("\nDigite o CPF para consulta: "))
        elif customer_option == 3:
            print("Atualizar Cliente")            
        elif customer_option == 4:
            CPF = validate_cpf(input("\nDigite o CPF para deletar o cliente: "))
        elif customer_option == 5:
            os.system('cls')
            print("\nLista de clientes: ")
            print(customer_list)
        elif customer_option == 6:
            print("Voltando para menu inicial...")
            menu_control = False


dict_test = [{'Nome': 'g',
                'CPF': '110.415.949-09',
                'RG': '09.123.456-9',
                'Nascimento': '05/06/1997', 
                'Endereco': {'CEP': '82560-420', 'Logradouro': 'Rua Roque Lazarotto', 'Numero': '50'}},
            {'Nome': 'pedro',
              'CPF': '629.437.920-20',
              'RG': '09.345.123-9',
              'Nascimento': '10/10/2000',
              'Endereco': {'CEP': '80030-000', 'Logradouro': 'Avenida João Gualb', 'Numero': '50'}}]

dict_test[1].update({'Nome':'miguel'})
print(dict_test)
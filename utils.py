import sys
import os
import re
import datetime
import requests

def exit_program():
    print("\n\tSaindo do programa...")
    sys.exit(0)

def validate_cpf(CPF):
    while True:
        numbers = [int(digit) for digit in CPF if digit.isdigit()]
        first_digit_sum = sum(cpf_digit* n for cpf_digit, n in zip (numbers[0:9], range (10, 1,-1)))
        rest = first_digit_sum % 11
        first_digit = 0 if rest <=1 else 11-rest

        second_digit_sum = sum(cpf_digit* n for cpf_digit, n in zip (numbers[0:10], range (11, 1,-1)))
        rest = second_digit_sum % 11
        second_digit = 0 if rest <=1 else 11-rest

        if re.match(r'\d{3}\.\d{3}\.\d{3}-\d{2}', CPF) or re.match(r'\d{3}\d{3}\d{3}\d{2}', CPF) and len(numbers) == 11 and first_digit == numbers[9] and second_digit == numbers[10]:
            CPF = re.sub('[-.]', '',CPF)
            cpf_formatado = f"{CPF[:3]}.{CPF[3:6]}.{CPF[6:9]}-{CPF[9:]}"
            return cpf_formatado
        else:
            print("\tCPF: " + str(CPF) + " e invalido, por favor insira um CPF valido.")
            CPF = input("\tCPF: ")

def validate_date(date_text, isbirth):
    today = datetime.date.today()
    year = today.year
    date_text = date_text.replace("-", "").replace("/", "")
    while True:
        try:
            if (year - int(date_text[4:8]) < 18 and isbirth == True):
                print("\tInfelizmente voce nao pode se cadastrar, pois nao tem mais de 18 anos")
                exit_program()
            newDate = datetime.datetime.strptime(date_text, '%d%m%Y').date()
            return newDate.strftime("%d/%m/%Y")
        except ValueError:
            print("\tData no formato errado, por favor manter o formato DD-MM-YYYY\n")
            date_text = input("\tDigite a data novamente: ")

def validate_rg(RG):
  pattern_rg = r'^\d{2}\.\d{3}\.\d{3}-[0-9A-Za-z]$'

  while True:
    RG = re.sub('[-.]','', RG)
    RG = f'{RG[:2]}.{RG[2:5]}.{RG[5:8]}-{RG[8:]}'

    if re.match(pattern_rg, RG):
      return RG
    else:
      RG = print("\tRG inválido. Digite novamente.")
      RG = input("\tRG: ")

def buscar_cep(cep_input):  
  while True:
    url = f'https://viacep.com.br/ws/{cep_input}/json/'
    response = requests.get(url, verify=False)
    if response.status_code == 200:
        data = response.json()
        adress = {
        "CEP": data['cep'],
        "Logradouro": data['logradouro'],
        "Bairro": data['bairro'],
        "Cidade": data['localidade'],
        "Estado": data['uf']
        }
        return adress
    else:
       print('\tCEP Invalido, por favor digite um CEP existente.')
       cep_input = input("\tCEP: ")
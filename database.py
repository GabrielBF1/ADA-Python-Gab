import pyodbc 

def retornar_cursor_banco_dados():
  connection = pyodbc.connect(retorna_string_conexao_banco_dados())
  cursor = connection.cursor()
  return cursor, connection
  
def retorna_string_conexao_banco_dados():
  return(
    "DRIVER={SQL Server};"
    "SERVER=hoesql633;"
    "DATABASE=Python-Gab;"
    "UID=SA\gbdfigu;"
    "Trusted_Connection=yes;"
  )

def select_banco_dados():
  cursor, connection = retornar_cursor_banco_dados()
  cursor.execute("select * from cliente;")
  clientes = cursor.fetchall()
  i = 0
  for c in clientes:
    print("Cliente " + str(i) + ": " + str(c) + "\n")
    i = i + 1
  connection.commit()


def insert_banco_dados(cliente):
  cursor, connection = retornar_cursor_banco_dados()
  insert_query = """
  INSERT INTO cliente (nome, CPF, RG, nascimento, endereco, numero)
  VALUES (?, ?, ?, ?, ?, ?);
  """
  values = (cliente['Nome'], cliente['CPF'], cliente['RG'], cliente['Nascimento'], cliente['Endereco'],cliente['Numero'])
  cursor.execute(insert_query, values)
  connection.commit()

def update_banco_dados(cliente):
  cursor, connection = retornar_cursor_banco_dados()
  update_query = """UPDATE cliente SET nome = ?, RG = ?, nascimento = ?, endereco = ?, numero = ? where CPF = """ + '\'' + cliente["CPF"] + '\''
  values = (cliente['Nome'], cliente['RG'], cliente['Nascimento'], cliente['Endereco'],cliente['Numero'])
  cursor.execute(update_query, values)
  connection.commit()

def delete_banco_dados(cpf):
  cursor, connection = retornar_cursor_banco_dados()
  delete_query = "DELETE FROM cliente WHERE cpf = '" + cpf + "';"
  cursor.execute(delete_query)
  connection.commit()  


# cliente = {'Nome': 'gabrie', 
#            'CPF': '110.415.949-09', 
#            'RG': '09.318.296-4', 
#            'Nascimento': '05/05/1997',
#              'Endereco': "{'CEP': '82560-420', 'Logradouro': 'Roque Lazarotto', 'Bairro': 'Boa Vista', 'Cidade': 'Curitiba', 'Estado': 'PR'}",
#             'Numero': '66'}
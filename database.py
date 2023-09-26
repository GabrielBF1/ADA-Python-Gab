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
  print(clientes)
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

def delete_banco_dados(cpf):
  cursor, connection = retornar_cursor_banco_dados()
  delete_query = "DELETE FROM cliente WHERE cpf = '" + cpf + "';"
  cursor.execute(delete_query)
  connection.commit()  

cliente = [{'Nome': 'gabriel', 
           'CPF': '110.415.949-09', 
           'RG': '09.318.294-4', 
           'Nascimento': '05/06/1997',
             'Endereco': "{'CEP': '82560-420', 'Logradouro': 'Rua Roque Lazarotto', 'Bairro': 'Boa Vista', 'Cidade': 'Curitiba', 'Estado': 'PR'}",
            'Numero': '55'}]
insert_banco_dados(cliente[0])

# select_banco_dados()
# delete_banco_dados(cliente["CPF"])
# select_banco_dados()


select_banco_dados()
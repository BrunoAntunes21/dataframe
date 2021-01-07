#manipulação de dados
import pandas as pd
import sqlite3

#criação do conector

conector=sqlite3.connect("conta.db")

df=pdread_sql_query("select*from Cadastro",conector)
print(df.head())

for nome in df['nome']:
    print(nome)



print(data)

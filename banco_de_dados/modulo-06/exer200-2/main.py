""" 
1. Localize na internet uma lista com todos os Municípios do Brasil, 5570 municípios com a Unidade da Federação
2. Consolide esses dados em um arquivo CSV/sheets.csv
3. Crie uma tabela CIDADES (ID/UF/CIDADE)
4. (PANDAS:)Importe todos os municípios para dentro desta tabela. 
5. Imprima todos municípios em uma select * from
6. Imprima um contador do sql count
7. Localize na Internet uma lista de todos os nomes de pessoas registrados em cartório, 100787. 
8. Consolide esses dados em um arquivo CSV/sheets.csv
9. Crie uma tabela PESSOAS (ID,NOME,IDADE,CIDADE_ID)
10. (PANDAS:)Importe todos os municípios para dentro desta tabela utilizando os seguintes critérios:
    Nome = nome transportados do csv
    Idade = Range de 0 a 100 (Random)
    Cidade_id = Range de 1 a Total de municípios na tabela SQL
11. Imprima todos em uma select *
12. Imprima um contador do sql 

13. Imprima lista de 2000 pessoas, ordenada por estado,cidade,idade,nome (vinda do SQL).
"""

import sqlite3
import pandas as pd 
import random


cnx = sqlite3.connect('ex_200-2.sqlite3')
cur = cnx.cursor()

cur.execute("""
    DROP TABLE IF EXISTS CIDADES; 
""")

cur.execute("""    
    CREATE TABLE CIDADES (
            CIDADE_ID INTEGER PRIMARY KEY AUTOINCREMENT,
            CIDADE_UF TEXT NOT NULL,
            CIDADE_NOME TEXT NOT NULL
    );
""")

cur.execute("""
    DROP TABLE IF EXISTS PESSOAS; 
""")

cur.execute("""
    CREATE TABLE PESSOAS(
        PESSOA_ID INTEGER PRIMARY KEY AUTOINCREMENT,
        PESSOA_NOME TEXT NOT NULL,
        PESSOA_IDADE INTEGER, 
        PESSOA_CIDADE_ID INTEGER NOT NULL
    );
""")

#  Tabela de Cidades
url_or_file = 'https://docs.google.com/spreadsheets/d/e/2PACX-1vSp3N0iSajaKoFaRiiTOV1Qxm1Y6-_B1IKJsKaqjiBhJbNIrjER4Kr2YtDHn8xNsFvWhQiGBK-Q5MQN/pub?gid=0&single=true&output=csv'
colunas = list(['id','UF','Município'])
df = pd.read_csv(url_or_file, index_col=0, header=0, usecols=colunas)

numero_cidades = list((df.shape))[0]

sql=("INSERT INTO CIDADES (CIDADE_UF,CIDADE_NOME) VALUES (?, ?) ")
for index, row in df.iterrows():
    val=(row.UF, row.Município)    
    cur.execute(sql,val)

cnx.commit()

# Tabela de Pessoas

url_or_file = 'https://docs.google.com/spreadsheets/d/e/2PACX-1vQrw2IJT8L_iuyYyZRehzDK89pNRRQUEVvUl1KxEJ8U182AEkUMIyWtGtQf3SHG8rxsEoni_-cqr4yo/pub?gid=945554847&single=true&output=csv'

colunas = list(['id','first_name'])
df = pd.read_csv(url_or_file, index_col=0, header=0, usecols=colunas)

sql=("INSERT INTO PESSOAS (PESSOA_NOME,PESSOA_IDADE,PESSOA_CIDADE_ID) VALUES (?, ?, ?) ")
for index,row in df.iterrows():
    nome = row.first_name
    idade = random.randrange(0,120)
    cidade_id = random.randrange(1,numero_cidades)          
    # print(nome,idade,cidade_id)
    val=(nome,idade,cidade_id)
    cur.execute(sql,val)
cnx.commit()
cur.close
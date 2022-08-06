import sqlite3

cnx = sqlite3.connect('ex_200-2.sqlite3')
cur = cnx.cursor()

# cur.execute("SELECT * FROM CIDADES;")
# todos = cur.fetchall()
# print(f'\nTodos: {todos}')
# print(type(todos))

# for x, y, z in todos:
#     print(f'{x}:{y}:{z}')


# cur.execute("SELECT * FROM PESSOAS;")
# todos = cur.fetchall()
# for x, y, z, w  in todos:
#     print(f'{x}:{y}:{z}:{w}')


# for i in ["PESSOAS","CIDADES"]:
#     sql = "SELECT COUNT(*) FROM " + i 
#     cur.execute(sql)
#     result = cur.fetchall()
#     print (f'{i}:{result}')


#cur.execute("""
 #   SELECT PESSOA_NOME,CIDADE_NOME FROM PESSOAS,CIDADES
 #       WHERE PESSOA_CIDADE_ID = CIDADE_ID;
#""")
#resultado=cur.fetchall()
#print(f'\nTodas as Linhas Nome e Cidade: {resultado}')

cur.execute("""
    SELECT CIDADE_UF, PESSOA_CIDADE_ID, PESSOA_IDADE, PESSOA_NOME FROM PESSOAS,CIDADES
        WHERE PESSOA_CIDADE_ID = CIDADE_ID AND PESSOA_ID <= 2000
        ORDER BY CIDADE_UF, PESSOA_CIDADE_ID, PESSOA_IDADE, PESSOA_NOME;
""")
resultado=cur.fetchall()
print(f'\nTodas as Linhas Nome e Cidade: {resultado}')

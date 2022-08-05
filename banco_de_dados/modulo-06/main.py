import sqlite3

cnx = sqlite3.connect('modulo06.sqlite3')

cur = cnx.cursor()

cur.execute("""
    DROP TABLE IF EXISTS CIDADES;
""")

cur.execute("""
    CREATE TABLE CIDADES (
        CIDADE_ID INTEGER PRIMARY KEY AUTOINCREMENT,
        CIDADE_NOME TEXT NOT NULL
    );
""")

cur.execute("""
    DROP TABLE IF EXISTS PESSOAS;
""")

cur.execute("""
    CREATE TABLE PESSOAS (
        PESSOA_ID INTEGER PRIMARY KEY AUTOINCREMENT,
        PESSOA_NOME TEXT NOT NULL,
        PESSOA_IDADE INTEGER,
        PESSOA_CIDADE_ID INTEGER NOT NULL
    );
""")

### INSERT INTO

cur.execute("""
    INSERT INTO CIDADES(CIDADE_NOME) VALUES
    ('Guaratuba'),
    ('Lages'),
    ('Blumenau'),
    ('Caxias'),
    ('Balneário Camboriú'),
    ('Florianópolis');
""")

cur.execute("""
    INSERT INTO PESSOAS(PESSOA_NOME,PESSOA_IDADE,PESSOA_CIDADE_ID)
        VALUES
        ('Adriano',47,1),
        ('Adriana',47,1),
        ('Karina',45,5),
        ('Kleber',50,2),
        ('Rafael',23,3),
        ('Amanda',32,4),
        ('Carlos',19,5),
        ('Ricardo',24,6),
        ('Patricia',12,2),
        ('Lira',15,3);
""")
cnx.commit()

# Fetchone()

# cur.execute("SELECT * FROM CIDADES;")
# primeiro_resultado = cur.fetchone()
# print(f'\nPrimeira linha: {primeiro_resultado}')

# Fetchmany()

# cur.execute("SELECT * FROM CIDADES;")
# resultado = cur.fetchmany(2)
# print(f'Primeira e segunda linha: {resultado}')

# Fetchall

# cur.execute("SELECT * FROM CIDADES;")
# resultado = cur.fetchall()
# print(f'Todas as linhas: {resultado}')

cur.execute("""
    SELECT PESSOA_NOME,CIDADE_NOME FROM PESSOAS,CIDADES
        WHERE PESSOA_CIDADE_ID = CIDADE_ID;
""")
resultado = cur.fetchall()
print(f'Todas as linhas Nome e Cidade: {resultado}')
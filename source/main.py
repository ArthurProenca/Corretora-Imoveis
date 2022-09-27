import sqlite3 #essa linha importa uma biblioteca


conn = sqlite3.connect('corretor.db') #essa linha conecta com o banco de dados

cursor = conn.cursor()

cursor.execute("""
               CREATE TABLE Pessoa(
               id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
               p_nome TEXT NOT NULL,
               m_nome TEXT NOT NULL,
               u_nome TEXT NOT NULL
               );
               """)

cursor.execute("""
               CREATE TABLE Imovel(
               id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
               p_nome TEXT NOT NULL,
               m_nome TEXT NOT NULL,
               u_nome TEXT NOT NULL
               );
               """)
conn.close() # vale lembrar que essa linha fecha a conexão

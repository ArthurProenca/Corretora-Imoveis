import sqlite3


conn = sqlite3.connect('corretor.db')

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
conn.close()

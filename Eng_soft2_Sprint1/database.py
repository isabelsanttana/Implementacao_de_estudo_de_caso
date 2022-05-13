import sqlite3
from sqlite3.dbapi2 import Cursor

class Banco():
    print('conectado ao BD')

    def __init__(self):
        self.conexao = sqlite3.connect('arquivo_db')
        self.createTableClientes()
        # self.createTableFuncionarios()
    
    def createTableClientes(self):
        cursor = self.conexao.cursor()

        cursor.execute("""
        CREATE TABLE IF NOT EXISTS Clientes (
        Id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
        Cpf TEXT NOT NULL,
        Nome TEXT NOT NULL,
        Telefone TEXT ,
        Celular TEXT ,
        User TEXT NOT NULL,
        Senha TEXT NOT NULL,
        Estado TEXT NOT NULL,
        Cidade TEXT NOT NULL,
        Bairro TEXT NOT NULL,
        Rua TEXT NOT NULL,
        Cep TEXT NOT NULL,
        Numero TEXT NOT NULL
        );""")

        self.conexao.commit()
        cursor.close()

    # def createTableFuncionarios(self):
    #     cursor = self.conexao.cursor()

    #     cursor.execute("""
    #     CREATE TABLE IF NOT EXISTS Funcionarios (
    #     Id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
    #     Nome TEXT NOT NULL,
    #     User TEXT NOT NULL,
    #     Senha TEXT NOT NULL,
    #     Cargo TEXT NOT NULL,
    #     Salario REAL,
    #     );""")

    #     self.conexao.commit()
    #     cursor.close()

# #Criando um unico funcionario 'ADM' 
# banco = Banco()
# c = banco.conexao.cursor()
# c.execute("""
# INSERT INTO Funcionarios(Nome,User,Senha,Cargo,Salario) VALUES(?,?,?,?,?)
# """,('Minerva McGonagall','adm','adm','Administrador','10.000,00'))
# banco.conexao.commit()



# class Banco():
#     print('conectado ao BD')
#     def __init__(self):
#         self.conexao = sqlite3.connect('arquivo_db')

    
# def createTableClientes(banco):
#     cursor = banco.conexao.cursor()

#     cursor.execute("""
#     CREATE TABLE IF NOT EXISTS Clientes (
#     Id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
#     Cpf TEXT NOT NULL,
#     Nome TEXT NOT NULL,
#     Telefone TEXT ,
#     Celular TEXT ,
#     User TEXT NOT NULL,
#     Senha TEXT NOT NULL,
#     Endereco TEXT NOT NULL
#     );""")

#     banco.conexao.commit()
#     cursor.close()

# def createTableFuncionarios(banco):
#     cursor = banco.conexao.cursor()

#     cursor.execute("""
#     CREATE TABLE IF NOT EXISTS Funcionarios (
#     Id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
#     Nome TEXT NOT NULL,
#     User TEXT NOT NULL,
#     Senha TEXT NOT NULL,
#     Cargo TEXT NOT NULL,
#     Salario REAL NOT NULL,
#     );""")

#     banco.conexao.commit()
#     cursor.close()
    
# banco = Banco()
# createTableClientes(banco)
# createTableFuncionarios(banco)

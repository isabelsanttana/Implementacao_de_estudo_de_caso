import sqlite3
from sqlite3.dbapi2 import Cursor


class Banco():
    print('conectado ao BD')

    def __init__(self):
        self.conexao = sqlite3.connect('arquivo_db')
        self.createTableClientes()
        self.createTableFuncionarios()
        self.createTableVenda()
        self.createTableProdutos()
    
    def createTableClientes(self):
        cursor = self.conexao.cursor()

        cursor.execute("""
        CREATE TABLE IF NOT EXISTS Clientes (
        Id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
        Cpf  VARCHAR(11) NOT NULL,
        Nome TEXT NOT NULL,
        Telefone  VARCHAR(11),
        Celular  VARCHAR(11),
        User TEXT NOT NULL,
        Senha TEXT NOT NULL,
        Estado TEXT NOT NULL,
        Cidade TEXT NOT NULL,
        Bairro TEXT NOT NULL,
        Rua TEXT NOT NULL,
        Cep  VARCHAR(8) NOT NULL,
        Numero TEXT NOT NULL
        );""")
        self.conexao.commit()
        cursor.close()

    def createTableFuncionarios(self):
        cursor = self.conexao.cursor()

        cursor.execute("""
        CREATE TABLE IF NOT EXISTS Funcionarios(
        Id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
        Cpf  VARCHAR(11) NOT NULL,
        Nome TEXT NOT NULL,
        User TEXT NOT NULL,
        Senha TEXT NOT NULL,
        Cargo TEXT NOT NULL,
        Salario_base REAL NOT NULL,
        Estado TEXT NOT NULL,
        Cidade TEXT NOT NULL,
        Bairro TEXT NOT NULL,
        Rua TEXT NOT NULL,
        Cep  VARCHAR(8) NOT NULL,
        Numero TEXT NOT NULL
        );""")
        self.conexao.commit()
        cursor.close()

    def createTableProdutos(self):
        cursor = self.conexao.cursor()

        cursor.execute("""
        CREATE TABLE IF NOT EXISTS Produtos(
        Id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
        Nome TEXT NOT NULL,
        Descricao  VARCHAR(300) NOT NULL,
        Valor REAL NOT NULL,
        Quantidade_em_estoque INTEGER NOT NULL,
        Estoque_minimo INTEGER NOT NULL,
        Validade TEXT NOT NULL 
        );""")
        self.conexao.commit()
        cursor.close()

    def createTableVenda(self):
        cursor = self.conexao.cursor()

        cursor.execute("""
        CREATE TABLE IF NOT EXISTS Venda(
        Id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
        Cliente TEXT NOT NULL,
        Funcionario TEXT NOT NULL,
        Total REAL NOT NULL,
        Forma_pagamento TEXT NOT NULL,
        Data TEXT NOT NULL,
        Desconto VARCHAR(2) NOT NULL,
        Parcelas VARCHAR(2) NOT NULL
        );""")
        self.conexao.commit()
        cursor.close() 

import class_
import database

clientes = []
funcionarios = []
produtos = []

banco = database.Banco()
c = banco.conexao.cursor()

#   Criando um unico funcionario 'ADM'
c.execute("""
SELECT * FROM Funcionarios
WHERE Cargo = ?
""",("Administrador",))

verificaAdm = c.fetchone()
if (verificaAdm == None) or ('Administrador' not in verificaAdm):
    c.execute("""
    INSERT INTO Funcionarios(Nome,User,Senha,Cargo,Salario_base) VALUES(?,?,?,?,?)
    """,('Minerva McGonagall','adm','adm','Administrador',10000))
    banco.conexao.commit()

# inserindo alguns produtos no banco
c.execute("""
SELECT * FROM Produtos
WHERE Nome = ?
""",('Blusa Preta',))

verificaProdutoTeste = c.fetchone()
if (verificaProdutoTeste == None) or ('Blusa Preta' not in verificaProdutoTeste):
    c.execute("""
    INSERT INTO Produtos(Validade,Nome,Qnt_estoque,Valor,Estoque_minimo) VALUES(?,?,?,?,?)
    """,('12/21','Blusa Preta',5,29,2))

    c.execute("""
    INSERT INTO Produtos(Validade,Nome,Qnt_estoque,Valor,Estoque_minimo) VALUES(?,?,?,?,?)
    """,('10/22','Blusa Azul',10,19.90,2))

    c.execute("""
    INSERT INTO Produtos(Validade,Nome,Qnt_estoque,Valor,Estoque_minimo) VALUES(?,?,?,?,?)
    """,('10/22','Blusa Verde',7,19.99,4))
    banco.conexao.commit()

#   Criando as instâncias das classes 
c.execute("""
SELECT * FROM Clientes;
""")

for i in c.fetchall():
    #end i[7] -> no banco vai ficar o endereço do obj, deixar assim msm ?
    end = class_.Endereco(i[7],i[8],i[9],i[10],i[11],i[12])
    clientes.append(class_.Cliente(i[0],i[1],i[2],end,i[5],i[6],i[3],i[4]))

c.execute("""
SELECT * FROM Funcionarios;
""")

for f in c.fetchall():
    funcionarios.append(class_.Funcionario(f[1],f[2],f[3],f[4],f[0]))

c.execute("""
SELECT * FROM Produtos;
""")
for p in c.fetchall():
    produtos.append(class_.Produto(p[0],p[2],p[3],p[5],p[1],p[4]))


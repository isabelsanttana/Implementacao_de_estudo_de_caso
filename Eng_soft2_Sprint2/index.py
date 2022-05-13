import class_
import database

clientes = []
funcionarios = []
produtos = []

banco = database.Banco()
c = banco.conexao.cursor()

# Criando um unico funcionario 'ADM' que pode inserir novos produtos e funcionarios
c.execute("""
SELECT * FROM Funcionarios
WHERE Cargo = ?
""",("Administrador",))

verificaAdm = c.fetchone()
if (verificaAdm == None) or ('Administrador' not in verificaAdm):
    c.execute("""
    INSERT INTO Funcionarios(Cpf,Nome,User,Senha,Cargo,Salario_base,Estado,Cidade,Bairro,Rua,Cep,Numero) VALUES(?,?,?,?,?,?,?,?,?,?,?,?)
    """,('12345678914','Minerva McGonagall','adm','adm','Administrador',10000,'RJ','Rio de Janeiro','Copacabana','Carioquinha','14523698','14'))
    
    banco.conexao.commit()


# Criando as instâncias das classes 
c.execute("""
SELECT * FROM Clientes;
""")

for i in c.fetchall():
    end = class_.Endereco(i[7],i[8],i[9],i[10],i[11],i[12])
    clientes.append(class_.Cliente(i[0],i[1],i[2],end,i[5],i[6],i[3],i[4]))

#############################
c.execute("""
SELECT * FROM Funcionarios;
""")

for f in c.fetchall():
    end = class_.Endereco(f[7],f[8],f[9],f[10],f[11],f[12])
    funcionarios.append(class_.Funcionario(f[2],f[1],end,f[3],f[4],f[5],f[6],f[0]))

# ##############################
c.execute("""
SELECT * FROM Produtos;
""")
for p in c.fetchall():
    produtos.append(class_.Produto(p[0],p[1],p[2],p[4],p[5],p[6],p[3]))


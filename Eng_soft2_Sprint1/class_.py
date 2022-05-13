from tkinter import messagebox

class Endereco():
  def __init__(self,estado,cidade,bairro,rua,cep,n):
    self.estado = estado
    self.cidade = cidade
    self.bairro = bairro
    self.cep = cep
    self.rua = rua
    self.numero = n

class Cliente():
  def __init__(self,id,cpf,nome,Endereco,user,senha,tel = False,cel = False):
    self.id = id
    self.cpf = cpf
    self.nome = nome
    self.tel = tel
    self.cel = cel
    self.end = Endereco
    self.user = user
    self.senha = senha
    self.img = False
    self.carrinho = [] 

class Produto():
  def __init__(self,cod,nome,qnt_estoque,estoque_minimo,validade,valor):
    self.cod = cod
    self.nomeProduto = nome
    self.descricao = str
    self.qnt_estoque = qnt_estoque
    self.valor = valor
    self.estoque_minimo = estoque_minimo
    self.validade = validade

class Funcionario():
  def __init__(self,nome,user,senha,cargo,id):
    self.id = id
    self.nome = nome
    self.user = user
    self.senha = senha
    self.cargo = cargo
    self.salario = float()
  
  def consultarCliente(self,listaClientes,IDcliente):
    for c in listaClientes:
      if c.id == IDcliente:
        dados = {'nome':c.nome,'cpf':c.cpf,'tel':c.tel,'cel':c.cel,'estado':c.end.estado,'cidade':c.end.cidade,'bairro':c.end.bairro,'cep':c.end.cep,'rua':c.end.rua,'n':c.end.numero,'carrinho':len(c.carrinho)}
        return dados
    
def div(n,simbolo):
  return str(n * simbolo)


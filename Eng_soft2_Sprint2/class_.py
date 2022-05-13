from tkinter import messagebox
import database 
import index

class Endereco():
  def __init__(self,estado,cidade,bairro,rua,cep,n,complemento = False):
    self.estado = estado
    self.cidade = cidade
    self.bairro = bairro
    self.cep = cep
    self.rua = rua
    self.numero = n
    self.complemento = complemento

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
    self.carrinho = [] #list[[cod,nome,qnt,valor],[cod,nome,qnt,valor]...]

  def realizarPagamento(self):
    total = 0
    for p in cliente.carrinho:
      total += p[3]*p[2]

    desconto = 0.0
    if total > 1000:
      desconto = 0.03
    else:
      desconto = 0.05

    totalPagar = total * desconto
    
    return {'total':total,'desconto':desconto,'totalPagar':totalPagar}

  def adicionarNoCarrinho(self,listaProdutos,cod,qnt): #add pra add só a qnt
    for p in listaProdutos:
      if p.cod == cod:
        return self.carrinho.append([p.cod,p.nomeProduto,qnt,p.valor])       

  def removerDoCarrinho(self,cod,qnt):
    for p in self.carrinho:
      if p[0] == cod:
        if qnt == p[2]:
          del self.carrinho[self.carrinho.index(p)]
        elif qnt > p[2]:
          print('msg de erro')
        else:
          p[2] = p[2] - qnt
      else:
        print('item não esta no carrinho')

class Produto():
  def __init__(self,cod,nome,descricao,qnt_estoque,estoque_minimo,validade,valor):
    self.cod = cod
    self.nomeProduto = nome
    self.descricao = descricao
    self.qnt_estoque = qnt_estoque
    self.valor = valor
    self.estoque_minimo = estoque_minimo
    self.validade = validade

class Funcionario():
  def __init__(self,nome,cpf,Endereco,user,senha,cargo,salario,id):
    self.matricula = id
    self.nome = nome
    self.cpf = cpf
    self.endereco = Endereco
    self.user = user
    self.senha = senha
    self.cargo = cargo
    self.salarioBase = salario

  def inserirCliente(self,banco,cpf,nome,tel,cel,user,senha,estado,cidade,bairro,rua,cep,n):

    try:
      c = banco.conexao.cursor()
      c.execute("""
      INSERT INTO Clientes(Cpf,Nome,Telefone,Celular,User,Senha,Estado,Cidade,Bairro,Rua,Cep,Numero) VALUES(?,?,?,?,?,?,?,?,?,?,?,?)
      """,(cpf,nome,tel,cel,user,senha,estado,cidade,bairro,rua,cep,n))
      banco.conexao.commit()
      return messagebox.showinfo(title='Informação de cadastro',message='Conta criada com Sucesso!!!!')

    except:
      return messagebox.showerror(title='Erro',message='Algo deu errado, tente novamente!')

  def alterarCliente(self,banco,nome,cpf,tel,cel,estado,cidade,bairro,cep,rua,n,id):
    try:
      c = banco.conexao.cursor()
      c.execute("""
      UPDATE Clientes
      SET Nome = ?,Cpf = ?, Telefone = ?,Celular = ?,Estado = ?,Cidade = ?,Bairro = ?,Cep = ?, Rua = ?, Numero = ?
      WHERE Id = ?
      """, (nome,cpf,tel,cel,estado,cidade,bairro,cep,rua,n,id))

      banco.conexao.commit()
      c.close()
      return messagebox.showinfo(title='Atualizado',message='Usuário atualizado com sucesso!')

    except:
      return messagebox.showerror(title='Erro',message='Ocorreu um erro na alteração do usuário ou o usuário não foi encontrado.')

  def deletaCliente(self,banco,id): #só o adm 
    for c in index.clientes:
      if c.id == id:
          if len(c.carrinho)==0:
              try:
                  del index.clientes[index.clientes.index(c)]
                  c = banco.conexao.cursor()
                  c.execute("""
                  DELETE FROM Clientes
                  WHERE Id = ?
                  """,(id,))

                  banco.conexao.commit()
                  c.close()
                  return messagebox.showinfo(title='!',message="Cliente excluído com sucesso!")
              except:
                  return messagebox.showerror(message='Ocorreu algo errado na exclusão do cliente.')
          else:
              return messagebox.showerror(title='!',message="Cliente não pode ser excluido se ainda possuir compras.")

  def consultarCliente(self,listaClientes,IDcliente):
    for c in listaClientes:
      if c.id == IDcliente:
        dados = {'nome':c.nome,'cpf':c.cpf,'tel':c.tel,'cel':c.cel,'estado':c.end.estado,'cidade':c.end.cidade,'bairro':c.end.bairro,'cep':c.end.cep,'rua':c.end.rua,'n':c.end.numero,'carrinho':c.carrinho,'cliente':c}
        return dados

  def realizarVenda(self,cliente):
    total = 0
    for p in cliente.carrinho:
      total += p[3]*p[2]

    desconto = 0.0
    if total > 1000:
      desconto = 0.03
    else:
      desconto = 0.05

    totalPagar = total * (1-desconto)
    
    return {'total':total,'desconto':desconto,'totalPagar':totalPagar}

  def inserirProduto(self,banco,nome,descricao,valor,qntEstoque,estoqueMinimo,validade): #só o adm
    try:
      c = banco.conexao.cursor()
      c.execute("""
      INSERT INTO Produtos(Nome,Descricao,Valor,Quantidade_em_estoque,Estoque_minimo,Validade) VALUES(?,?,?,?,?,?)
      """,(nome,descricao,valor,qntEstoque,estoqueMinimo,validade))
          
      banco.conexao.commit()
      return messagebox.showinfo(title='Informação de cadastro',message='Produto registrado com Sucesso!')

    except:
      return messagebox.showerror(title='Erro',message='Algo deu errado, tente novamente!')

  def alterarProduto(self,banco,nome,descricao,valor,qntEstoque,estoqueMinimo,validade,id): #só o adm

    try:
        c = banco.conexao.cursor()
        c.execute("""
        UPDATE Produtos
        SET Nome = ?,Descricao = ?,Valor = ?,Quantidade_em_estoque = ?,Estoque_minimo = ?, Validade = ?
        WHERE Id = ?
        """,(nome,descricao,valor,qntEstoque,estoqueMinimo,validade,id))

        banco.conexao.commit()
        return messagebox.showinfo(title='Informação de cadastro',message='Produto atualizado com Sucesso!')

    except:
        return messagebox.showerror(title='Erro',message='Algo deu errado, tente novamente!')

  def cadastrarFuncionario(self,banco,cpf,nome,cargo,salarioBase,user,senha,estado,cidade,bairro,rua,cep,n):#só o adm
    
    try:
        c = banco.conexao.cursor()
        c.execute("""
        INSERT INTO Funcionarios(Cpf,Nome,Cargo,Salario_base,User,Senha,Estado,Cidade,Bairro,Rua,Cep,Numero) VALUES(?,?,?,?,?,?,?,?,?,?,?,?)
        """,(cpf,nome,cargo,float(salarioBase),user,senha,estado,cidade,bairro,rua,cep,n))
        
        banco.conexao.commit()
        return messagebox.showinfo(title='Informação de cadastro',message='Funcionario registrado com Sucesso!')

    except:
        return messagebox.showerror(title='Erro',message='Algo deu errado, tente novamente!')

  def alterarFuncionario(self,banco,cpf,nome,cargo,salarioBase,estado,cidade,bairro,rua,cep,n,id):#só o adm
    try:
        c = banco.conexao.cursor()
        c.execute("""
        UPDATE Funcionarios
        SET Cpf = ?, Nome = ?,Cargo = ?,Salario_base = ?,Estado = ?,Cidade = ?,Bairro = ?,Rua = ?,Cep = ?,Numero = ? 
        WHERE Id = ?
        """,(cpf,nome,cargo,float(salarioBase),estado,cidade,bairro,rua,cep,n,id))
            
        banco.conexao.commit()
        return messagebox.showinfo(title='Informação de cadastro',message='Funcionario atualizado com Sucesso!')

    except :
        return messagebox.showerror(title='Erro',message='Algo deu errado, tente novamente!')

def div(n,simbolo):
  return str(n * simbolo)

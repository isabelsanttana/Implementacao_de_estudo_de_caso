#   App principal
from tkinter import *
from tkinter import messagebox
from tkinter import ttk
import index
import database
import class_

admLogado = False #se o login for feito pelo adm a variavel muda para o obj 'Funcionario adm'
clienteLogado = False #se o login for feito por um cliente a variavel muda para o obj cliente

class AppInicial(Tk):
    def __init__(self):
        Tk.__init__(self)
        self._frame = ''
        self.trocaPag(login)

    def trocaPag(self, frame_class):
        novoFrame = frame_class(self)
        if self._frame is not '':
            self._frame.destroy()
        self._frame = novoFrame
        self._frame.grid()

class login(Frame):
    def __init__(self, master): #master == janela
        self.fonte = ("Verdana", 12)
        self.jan = master

        master.title('Login')
        master.resizable(width=False, height=False)

        Frame.__init__(self, master)

        self.userLabel = Label(self,text='Login:',font= self.fonte,fg="black").grid(row=0,pady=(15,0))
        self.userEntry = ttk.Entry(self,width=30)
        self.userEntry.grid(row=0,column=1,padx=(0,10),pady=(16,0))

        self.senhaLabel = Label(self,text='Senha:',font= self.fonte,fg="black" ).grid(row=1,pady=(5,0))
        self.senhaEntry = ttk.Entry(self,width=30,show='•')
        self.senhaEntry.grid(row=1,column=1,padx=(0,10),pady=(6,0))

        self.entrarButton = ttk.Button(self,text='Entrar',width=20,command=self.logar)
        self.entrarButton.grid(row=2,column=1,padx=(0,70),pady=(20,0))

        self.criarContaButton = ttk.Button(self,text='Criar conta',width=15,command=lambda: master.trocaPag(CriarConta))
        self.criarContaButton.grid(row=3,column=1,padx=(0,70),pady=(5,10))


    def logar(self):
        banco = database.Banco()

        user = self.userEntry.get()
        senha = self.senhaEntry.get()
        c = banco.conexao.cursor()

        c.execute("""
        SELECT * FROM Clientes
        WHERE (User = ? and Senha = ?)
        """,(user,senha))

        verificaLogin = c.fetchone()
        try:
            if user ==  'adm' and senha == 'adm':
                for f in index.funcionarios:
                    if f.user == user and f.senha == senha and f.cargo == 'Administrador':
                        global admLogado
                        admLogado = f
                        self.jan.trocaPag(PagAdm)
            elif (user in verificaLogin)and (senha in verificaLogin):
                for c in index.clientes:
                    if user == c.user:
                        global clienteLogado
                        clienteLogado = c
                        self.jan.trocaPag(PagCliente)
        except :
            messagebox.showinfo(title='Login',message='Acesso Negado. Verifique se esta cadastrado no sistema.')

class CriarConta(Frame):
    def __init__(self, master):
        self.fonte = ("Verdana", 10)
        master.title('Login')
        master.resizable(width=False, height=False)

        Frame.__init__(self, master)

        legenda = ('*Campo obrigatório.')

        self.tituloLabel = Label(self,text='Insira seus dados nos campos a seguir:',font= ("Verdana", 10,'bold')).grid(row=0,columnspan=3,padx=(10,0),pady=(15,0),sticky=W)
  
        self.nomeLabel = Label(self,text='*Nome:',font= self.fonte).grid(row=1,columnspan=3,padx=(15,0),pady=(10,0),sticky=W)
        self.nomeEntry = ttk.Entry(self,width=55)
        self.nomeEntry.grid(row=2,columnspan=3,padx=(30,20),sticky=W)

        self.cpfLabel = Label(self,text='*CPF:',font= self.fonte).grid(row=3,columnspan=3,padx=(15,0),pady=(5,0),sticky=W)
        self.cpfEntry = ttk.Entry(self,width=55)
        self.cpfEntry.grid(row=4,columnspan=3,padx=(30,20),sticky=W)

        self.userLabel = Label(self,text='*Login:',font= self.fonte).grid(row=5,columnspan=3,padx=(15,0),pady=(5,0),sticky=W)
        self.userEntry = ttk.Entry(self,width=55)
        self.userEntry.grid(row=6,columnspan=3,padx=(30,20),sticky=W)

        self.senhaLabel = Label(self,text='*Senha:',font= self.fonte).grid(row=7,columnspan=3,padx=(15,0),pady=(5,0),sticky=W)
        self.senhaEntry = ttk.Entry(self,width=55,show='•')
        self.senhaEntry.grid(row=8,columnspan=3,padx=(30,20),sticky=W)

        self.confirmaSenhaLabel = Label(self,text='*Confirme sua senha:',font= self.fonte).grid(row=9,columnspan=3,padx=(15,0),pady=(5,0),sticky=W)
        self.confirmaSenhaEntry = ttk.Entry(self,width=55,show='•')
        self.confirmaSenhaEntry.grid(row=10,columnspan=3,padx=(30,20),sticky=W)
        
        self.telLabel = Label(self,text=' Tel:',font= self.fonte).grid(row=11,columnspan=3,padx=(15,0),pady=(5,0),sticky=W)
        self.telEntry = ttk.Entry(self,width=55)
        self.telEntry.grid(row=12,columnspan=3,padx=(30,20),sticky=W)

        self.celLabel = Label(self,text=' Cel:',font= self.fonte).grid(row=13,columnspan=3,padx=(15,0),pady=(5,0),sticky=W)
        self.celEntry = ttk.Entry(self,width=55)
        self.celEntry.grid(row=14,columnspan=3,padx=(30,20),sticky=W)

        self.endLabel = Label(self,text='Endereço:',font= self.fonte).grid(row=15,columnspan=3,padx=(15,0),pady=(15,0),sticky=W)
        self.estadoLabel = Label(self,text='*Estado:',font= self.fonte).grid(row=16,padx=(20,0),pady=(2,0),sticky=W)
        self.cidadeLabel = Label(self,text='*Cidade:',font= self.fonte).grid(row=16,column=1,padx=(5,0),pady=(2,0),sticky=W)
        self.bairroLabel = Label(self,text='*Bairro:',font= self.fonte).grid(row=16,column=2,padx=(5,0),pady=(2,0),sticky=W)
        self.ruaLabel = Label(self,text='*Rua:',font= self.fonte).grid(row=18,padx=(20,0),pady=(5,0),sticky=W)
        self.cepLabel = Label(self,text='*CEP:',font= self.fonte).grid(row=18,column=1,padx=(5,0),pady=(5,0),sticky=W)
        self.nLabel = Label(self,text='*Nº:',font= self.fonte).grid(row=18,column=2,padx=(5,0),pady=(5,0),sticky=W)

        self.estadoEntry = ttk.Combobox(self, values=['AC','AL','AP','AM','BA','CE','DF','ES','GO','MA','MT','MS','MG','PA','PB','PR','PE','PI','RJ','RN','RS','RO','RR','SC','SP','SE','TO'])
        self.estadoEntry.grid(row=17,padx=(20,0),sticky=W)
        self.cidadeEntry = ttk.Entry(self,width=15)
        self.cidadeEntry.grid(row=17,column=1,padx=(5,0),sticky=W)
        self.bairroEntry = ttk.Entry(self,width=15)
        self.bairroEntry.grid(row=17,column=2,padx=(5,15),sticky=W)
        self.ruaEntry = ttk.Entry(self,width=20)
        self.ruaEntry.grid(row=19,padx=(20,0),sticky=W)
        self.cepEntry = ttk.Entry(self,width=15)
        self.cepEntry.grid(row=19,column=1,padx=(5,0),sticky=W)
        self.nEntry = ttk.Entry(self,width=5)
        self.nEntry.grid(row=19,column=2,padx=(5,0),sticky=W)

        self.legLabel = Label(self,text=legenda,font=("Verdana", 6)).grid(row=20,columnspan=3,padx=(15,0),pady=(5,0),sticky=W)

        self.regButton = ttk.Button(self,text='Criar conta',width=30,command= self.registerdb)
        self.regButton.grid(row=21,columnspan=3,pady=(20,0))

        self.back = ttk.Button(self,text='Voltar no login',width=20,command=lambda: master.trocaPag(login))
        self.back.grid(row=22,columnspan=3,pady=(5,10))


    def registerdb(self):
        banco = database.Banco()

        nome = self.nomeEntry.get().title()
        cpf = self.cpfEntry.get()
        user = self.userEntry.get()
        senha = self.senhaEntry.get()
        confSenha = self.confirmaSenhaEntry.get()
        tel = self.telEntry.get()
        cel = self.celEntry.get()
        estado = self.estadoEntry.get()
        cidade = self.cidadeEntry.get().capitalize()
        bairro = self.bairroEntry.get().capitalize()
        rua = self.ruaEntry.get().capitalize()
        cep = self.cepEntry.get()
        n = self.nEntry.get()


        verificaUser = []
        for c in index.clientes:
            verificaUser.append(c.user)

        if (nome == '' or cpf == '' or user == '' or senha == '' or  estado == '' or  bairro == '' or cidade == '' or rua == '' or cep == '' or  n == ''):
            messagebox.showerror(title='Erro',message='Preencha Todos os Campos Obrigatórios!')

        elif tel == '' and cel == '':
            messagebox.showerror(title='Erro',message='Insira pelo menos uma informação de contato.')

        elif user in verificaUser:
            messagebox.showwarning(message='Nome de usuário já esta em uso, escolha outro.')

        elif (cpf.isdigit() == False) or (len(cpf) != 11):
            messagebox.showerror(message='Digite apenas números no campo "CPF" sendo 11 dígitos.')

        elif(cep.isdigit() == False) or (len(cep) != 8 ):
            messagebox.showerror(message='Digite apenas números no campo "Cep" sendo 8 dígitos.')

        else:
            if senha != confSenha:
                messagebox.showerror(title='Senhas Diferentes',message='As senhas não são iguais, tente novamente.')

            else:
                try:
                    c = banco.conexao.cursor()
                    c.execute("""
                    INSERT INTO Clientes(Cpf,Nome,Telefone,Celular,User,Senha,Estado,Cidade,Bairro,Rua,Cep,Numero) VALUES(?,?,?,?,?,?,?,?,?,?,?,?)
                    """,(cpf,nome,tel,cel,user,senha,estado,cidade,bairro,rua,cep,n))
                    banco.conexao.commit()
                    return messagebox.showinfo(title='Informação de cadastro',message='Conta criada com Sucesso!!!!')

                except:
                    return messagebox.showerror(title='Erro',message='Algo deu errado, tente novamente!')

class PagCliente(Frame):
    def __init__(self, master):
        self.fonte = ("Verdana", 12)
        master.title('Pagina Do Cliente')
        master.resizable(width=False, height=False)

        Frame.__init__(self, master)

        self.pagLabel = Label(self,text=clienteLogado.nome,font= ("Verdana", 12,'bold'),fg="black").grid(row=0,padx=(15,0),pady=(15,10),sticky=W)
        self.sub3Label = Label(self,text='Produtos disponiveis:',font= self.fonte,fg="black").grid(row=2,columnspan=4,padx=(15,0),pady=(0,10),sticky=W)
        self.pagLabel = Label(self,text='Itens no carrinho:',font= ("Verdana", 12),fg="black").grid(row=1,padx=(15,0),pady=(15,10),sticky=W)
        self.pagLabel = Label(self,text=len(clienteLogado.carrinho),font= ("Verdana", 12),fg="black").grid(row=1,column=1,padx=(15,0),pady=(15,10),sticky=W)
        
        def adicionarProduto(p):
            clienteLogado.carrinho.append(p)
            messagebox.showinfo(message='Item adicionado ao carrinho!')
            return print(f'Qnt carrinho:{len(clienteLogado.carrinho)}')

        def removerProduto(p):

            if p not in clienteLogado.carrinho:
                messagebox.showinfo(message='Este item não esta no seu carrinho!')
            else:
                del clienteLogado.carrinho[clienteLogado.carrinho.index(p)]
                messagebox.showinfo(message='Item Removido do carrinho!')
            return print(f'Qnt carrinho:{len(clienteLogado.carrinho)}')
        row = 3
        for p in index.produtos:
            self.produtoLabel = Label(self,text=p.nomeProduto,font= self.fonte,fg="black").grid(row=row,pady=(0,5),padx=(15,0),sticky=W)
            self.valorLabel = Label(self,text='R$'+str(p.valor),font= self.fonte,fg="black").grid(row=row,column=1,pady=(0,5),padx=(10,0))
            self.addButton = ttk.Button(self,text='+',width=5,command= lambda: adicionarProduto(p))
            self.removeButton = ttk.Button(self,text='-',width=5,command= lambda: removerProduto(p))
            self.addButton .grid(row=row,column=2,pady=(0,5),sticky=E)
            self.removeButton .grid(row=row,column=3,pady=(0,5),padx=(0,15),sticky=E)
            row+=1
            self.eLabel = Label(self,text=' ').grid(row=row)
            row+=1

        self.legLabel = Label(self,text='(+)Para adicionar o produto no seu carrinho',font= ("Verdana", 7),fg="black").grid(row=row,columnspan=4,pady=(0,5),padx=(15,0),sticky=W)
        row+=1
        self.legLabel = Label(self,text='(-)Para remover do carrinho',font= ("Verdana", 7),fg="black").grid(row=row,columnspan=4,pady=(0,10),padx=(15,0),sticky=W)
        row+=1
        self.back = ttk.Button(self,text='Sair',width=20,command=lambda: master.trocaPag(login))
        self.back.grid(row=row,columnspan=4,pady=(10,10))

class PagAdm(Frame):
    def __init__(self, master):
        self.fonte = ("Verdana", 12)
        master.title('Tela de Administração')
        master.resizable(width=False, height=False)

        Frame.__init__(self, master)

        self.nomeLabel = Label(self,text='Menu de Administração',font= ("Century Gothic",15),fg="black").grid(row=0,pady=(15,0))
        self.nomeLabel = Label(self,text='Escolha qual procedimento quer seguir:',font= self.fonte,fg="black").grid(row=1,padx=(60,60),pady=(15,0))
        
        self.icButton = ttk.Button(self, text="Inserir Cliente",width=30,command=lambda: master.trocaPag(inserirClienteTl)).grid(row=2,pady=(20,0))
        self.acButton = ttk.Button(self, text="Alterar Cliente",width=30,command=lambda: master.trocaPag(alterarClienteTl)).grid(row=3,pady=(5,0))
        self.dcButton = ttk.Button(self, text="Deletar Cliente",width=30,command=lambda: master.trocaPag(deletarClienteTl)).grid(row=4,pady=(5,0))
        self.ccButton = ttk.Button(self, text="Consultar Cliente",width=30,command=lambda: master.trocaPag(consultarClienteTl)).grid(row=5,pady=(5,0))
        self.lcButton = ttk.Button(self, text="Listar Clientes",width=30,command=lambda: master.trocaPag(listarClientesTl)).grid(row=6,pady=(5,20))
        self.sairButton = ttk.Button(self, text="Sair",width=30,command=lambda: master.trocaPag(login)).grid(row=7,pady=(0,10))
    
class inserirClienteTl(Frame):
    def __init__(self,master):
        self.fonte = ("Verdana", 12)
        master.title('Tela de Administração')
        master.resizable(width=False, height=False)

        Frame.__init__(self, master)
  
        legenda = ('*Campo obrigatório.')

        self.tituloLabel = Label(self,text='Insira seus dados nos campos a seguir:',font= ("Verdana", 10,'bold')).grid(row=0,columnspan=3,padx=(10,0),pady=(15,0),sticky=W)
  
        self.nomeLabel = Label(self,text='*Nome:',font= self.fonte).grid(row=1,columnspan=3,padx=(15,0),pady=(10,0),sticky=W)
        self.nomeEntry = ttk.Entry(self,width=55)
        self.nomeEntry.grid(row=2,columnspan=3,padx=(30,20),sticky=W)

        self.cpfLabel = Label(self,text='*CPF:',font= self.fonte).grid(row=3,columnspan=3,padx=(15,0),pady=(5,0),sticky=W)
        self.cpfEntry = ttk.Entry(self,width=55)
        self.cpfEntry.grid(row=4,columnspan=3,padx=(30,20),sticky=W)

        self.userLabel = Label(self,text='*Login:',font= self.fonte).grid(row=5,columnspan=3,padx=(15,0),pady=(5,0),sticky=W)
        self.userEntry = ttk.Entry(self,width=55)
        self.userEntry.grid(row=6,columnspan=3,padx=(30,20),sticky=W)

        self.senhaLabel = Label(self,text='*Senha:',font= self.fonte).grid(row=7,columnspan=3,padx=(15,0),pady=(5,0),sticky=W)
        self.senhaEntry = ttk.Entry(self,width=55,show='•')
        self.senhaEntry.grid(row=8,columnspan=3,padx=(30,20),sticky=W)

        self.confirmaSenhaLabel = Label(self,text='*Confirme sua senha:',font= self.fonte).grid(row=9,columnspan=3,padx=(15,0),pady=(5,0),sticky=W)
        self.confirmaSenhaEntry = ttk.Entry(self,width=55,show='•')
        self.confirmaSenhaEntry.grid(row=10,columnspan=3,padx=(30,20),sticky=W)
        
        self.telLabel = Label(self,text=' Tel:',font= self.fonte).grid(row=11,columnspan=3,padx=(15,0),pady=(5,0),sticky=W)
        self.telEntry = ttk.Entry(self,width=55)
        self.telEntry.grid(row=12,columnspan=3,padx=(30,20),sticky=W)

        self.celLabel = Label(self,text=' Cel:',font= self.fonte).grid(row=13,columnspan=3,padx=(15,0),pady=(5,0),sticky=W)
        self.celEntry = ttk.Entry(self,width=55)
        self.celEntry.grid(row=14,columnspan=3,padx=(30,20),sticky=W)

        self.endLabel = Label(self,text='Endereço:',font= self.fonte).grid(row=15,columnspan=3,padx=(15,0),pady=(15,0),sticky=W)
        self.estadoLabel = Label(self,text='*Estado:',font= self.fonte).grid(row=16,padx=(20,0),pady=(2,0),sticky=W)
        self.cidadeLabel = Label(self,text='*Cidade:',font= self.fonte).grid(row=16,column=1,padx=(5,0),pady=(2,0),sticky=W)
        self.bairroLabel = Label(self,text='*Bairro:',font= self.fonte).grid(row=16,column=2,padx=(5,0),pady=(2,0),sticky=W)
        self.ruaLabel = Label(self,text='*Rua:',font= self.fonte).grid(row=18,padx=(20,0),pady=(5,0),sticky=W)
        self.cepLabel = Label(self,text='*CEP:',font= self.fonte).grid(row=18,column=1,padx=(5,0),pady=(5,0),sticky=W)
        self.nLabel = Label(self,text='*Nº:',font= self.fonte).grid(row=18,column=2,padx=(5,0),pady=(5,0),sticky=W)

        self.estadoEntry = self.estadoEntry = ttk.Combobox(self, values=['AC','AL','AP','AM','BA','CE','DF','ES','GO','MA','MT','MS','MG','PA','PB','PR','PE','PI','RJ','RN','RS','RO','RR','SC','SP','SE','TO'])
        self.estadoEntry.grid(row=17,padx=(20,0),sticky=W)
        self.cidadeEntry = ttk.Entry(self,width=15)
        self.cidadeEntry.grid(row=17,column=1,padx=(5,0),sticky=W)
        self.bairroEntry = ttk.Entry(self,width=15)
        self.bairroEntry.grid(row=17,column=2,padx=(5,15),sticky=W)
        self.ruaEntry = ttk.Entry(self,width=20)
        self.ruaEntry.grid(row=19,padx=(20,0),sticky=W)
        self.cepEntry = ttk.Entry(self,width=15)
        self.cepEntry.grid(row=19,column=1,padx=(5,0),sticky=W)
        self.nEntry = ttk.Entry(self,width=5)
        self.nEntry.grid(row=19,column=2,padx=(5,0),sticky=W)

        self.legLabel = Label(self,text=legenda,font=("Verdana", 6)).grid(row=20,columnspan=3,padx=(15,0),pady=(5,0),sticky=W)

        self.regButton = ttk.Button(self,text='Criar conta',width=30,command= self.registerdb)
        self.regButton.grid(row=21,columnspan=3,pady=(20,0))

        self.back = ttk.Button(self,text='Voltar na Tela inicial',width=20,command=lambda: master.trocaPag(PagAdm))
        self.back.grid(row=22,columnspan=3,pady=(5,10))


    def registerdb(self):
        banco = database.Banco()

        nome = self.nomeEntry.get().title()
        cpf = self.cpfEntry.get()
        user = self.userEntry.get()
        senha = self.senhaEntry.get()
        confSenha = self.confirmaSenhaEntry.get()
        tel = self.telEntry.get()
        cel = self.celEntry.get()
        estado = self.estadoEntry.get()
        cidade = self.cidadeEntry.get().capitalize()
        bairro = self.bairroEntry.get().capitalize()
        rua = self.ruaEntry.get().capitalize()
        cep = self.cepEntry.get()
        n = self.nEntry.get()

        if (nome == '' or cpf == '' or user == '' or senha == '' or  estado == '' or  bairro == '' or cidade == '' or rua == '' or cep == '' or  n == ''):
            messagebox.showerror(title='Erro',message='Preencha Todos os Campos Obrigatórios!')
        elif tel == '' and cel == '':
            messagebox.showerror(title='Erro',message='Insira pelo menos uma informação de contato.')
        elif (cpf.isdigit() == False) or (len(cpf) != 11):
            messagebox.showerror(message='Digite apenas números no campo "CPF" sendo 11 dígitos.')

        elif(cep.isdigit() == False) or (len(cep) != 8 ):
            messagebox.showerror(message='Digite apenas números no campo "Cep" sendo 8 dígitos.')

        else:
            if senha != confSenha:
                messagebox.showerror(title='Senhas Diferentes',message='As senhas não são iguais, tente novamente.')
            else:
                try:
                    c = banco.conexao.cursor()
                    c.execute("""
                    INSERT INTO Clientes(Cpf,Nome,Telefone,Celular,User,Senha,Estado,Cidade,Bairro,Rua,Cep,Numero) VALUES(?,?,?,?,?,?,?,?,?,?,?,?)
                    """,(cpf,nome,tel,cel,user,senha,estado,cidade,bairro,rua,cep,n))
                    banco.conexao.commit()
                    return messagebox.showinfo(title='Informação de cadastro',message='Conta criada com Sucesso!!!!')

                except:
                    return messagebox.showerror(title='Erro',message='Algo deu errado, tente novamente!')

class alterarClienteTl(Frame):
    def __init__(self,master):
        self.fonte = ("Verdana", 11)
        master.title('Administração')
        master.resizable(width=False, height=False)

        Frame.__init__(self, master)

        legenda = ('*Campo obrigatório.')

        self.idLabel = Label(self,text='ID do cliente a ser atualizado:',font= ("Verdana", 10,'bold'),fg="black").grid(row=0,columnspan=3 ,padx=(15,0),pady=(15,0),sticky=W)
        self.idEntry = ttk.Entry(self,width=10)
        self.idEntry.grid(row=0,column=2,padx=(15,10),pady=(16,0))

        self.divLabel = Label(self,text= class_.div(70,'_')).grid(row=1,columnspan=3)
        self.idLabel = Label(self,text='Insira os novos Dados:',font= ("Verdana", 10,'bold'),fg="black").grid(row=2,columnspan=3 ,padx=(15,0),pady=(5,0),sticky=W)

        self.cpfLabel = Label(self,text='*Cpf:',font= self.fonte,fg="black").grid(row=3,padx=(15,0),pady=(5,0),sticky=W)
        self.cpfEntry = ttk.Entry(self,width=55)
        self.cpfEntry.grid(row=4,columnspan=3,padx=(20,10),pady=(6,0),sticky=W)

        self.nomeLabel = Label(self,text='*Nome:',font= self.fonte,fg="black").grid(row=5,padx=(15,0),pady=(5,0),sticky=W)
        self.nomeEntry = ttk.Entry(self,width=55)
        self.nomeEntry.grid(row=6,columnspan=3,padx=(20,10),pady=(6,0),sticky=W)

        self.telLabel = Label(self,text='Telefone:',font= self.fonte,fg="black").grid(row=7,padx=(15,0),pady=(5,0),sticky=W)
        self.telEntry = ttk.Entry(self,width=55)
        self.telEntry.grid(row=8,columnspan=3,padx=(20,10),pady=(6,0),sticky=W)

        self.celLabel = Label(self,text='Celular:',font= self.fonte,fg="black").grid(row=9,padx=(15,0),pady=(5,0),sticky=W)
        self.celEntry = ttk.Entry(self,width=55)
        self.celEntry.grid(row=10,columnspan=3,padx=(20,10),pady=(6,0),sticky=W)

        self.endLabel = Label(self,text='*Endereço:',font= self.fonte).grid(row=11,columnspan=3,padx=(15,0),pady=(15,0),sticky=W)
        self.estadoLabel = Label(self,text='*Estado:',font= self.fonte).grid(row=12,padx=(20,0),pady=(2,0),sticky=W)
        self.cidadeLabel = Label(self,text='*Cidade:',font= self.fonte).grid(row=12,column=1,padx=(5,0),pady=(2,0),sticky=W)
        self.bairroLabel = Label(self,text='*Bairro:',font= self.fonte).grid(row=12,column=2,padx=(5,0),pady=(2,0),sticky=W)
        self.ruaLabel = Label(self,text='*Rua:',font= self.fonte).grid(row=14,padx=(20,0),pady=(5,0),sticky=W)
        self.cepLabel = Label(self,text='*CEP:',font= self.fonte).grid(row=14,column=1,padx=(5,0),pady=(5,0),sticky=W)
        self.nLabel = Label(self,text='*Nº:',font= self.fonte).grid(row=14,column=2,padx=(5,0),pady=(5,0),sticky=W)

        self.estadoEntry = self.estadoEntry = ttk.Combobox(self, values=['AC','AL','AP','AM','BA','CE','DF','ES','GO','MA','MT','MS','MG','PA','PB','PR','PE','PI','RJ','RN','RS','RO','RR','SC','SP','SE','TO'])
        self.estadoEntry.grid(row=13,padx=(20,0),sticky=W)
        self.cidadeEntry = ttk.Entry(self,width=15)
        self.cidadeEntry.grid(row=13,column=1,padx=(5,0),sticky=W)
        self.bairroEntry = ttk.Entry(self,width=15)
        self.bairroEntry.grid(row=13,column=2,padx=(5,10),sticky=W)
        self.ruaEntry = ttk.Entry(self,width=20)
        self.ruaEntry.grid(row=15,padx=(20,0),sticky=W)
        self.cepEntry = ttk.Entry(self,width=15)
        self.cepEntry.grid(row=15,column=1,padx=(5,0),sticky=W)
        self.nEntry = ttk.Entry(self,width=5)
        self.nEntry.grid(row=15,column=2,padx=(5,10),sticky=W)

        self.legLabel = Label(self,text=legenda,font=("Verdana", 6)).grid(row=16,columnspan=3,padx=(15,0),pady=(5,0),sticky=W)

        self.updateButton = ttk.Button(self,text='Atualizar Dados',width=30,command= self.update)
        self.updateButton.grid(row=17,columnspan=3,pady=(20,0))

        self.back = ttk.Button(self,text='Voltar na Tela inicial',width=20,command=lambda: master.trocaPag(PagAdm))
        self.back.grid(row=18,columnspan=3,pady=(5,10))


    def update(self):
        banco = database.Banco()

        id = self.idEntry.get()
        cpf = self.cpfEntry.get()
        nome = self.nomeEntry.get().title()
        tel = self.telEntry.get()
        cel = self.celEntry.get()
        estado = self.estadoEntry.get()
        cidade = self.cidadeEntry.get().capitalize()
        bairro = self.bairroEntry.get().capitalize()
        cep = self.cepEntry.get()
        rua = self.ruaEntry.get().capitalize()
        n = self.nEntry.get()

        if (nome == '' or cpf == '' or  estado == '' or  bairro == '' or cidade == '' or rua == '' or cep == '' or  n == ''):
            messagebox.showerror(title='Erro',message='Preencha Todos os Campos Obrigatórios!')
        elif tel == '' and cel == '':
            messagebox.showerror(title='Erro',message='Insira pelo menos uma informação de contato.')
        elif (cpf.isdigit() == False) or (len(cpf) != 11):
            messagebox.showerror(message='Digite apenas números no campo "CPF" sendo 11 dígitos.')

        elif(cep.isdigit() == False) or (len(cep) != 8 ):
            messagebox.showerror(message='Digite apenas números no campo "Cep" sendo 8 dígitos.')
        else:
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

class deletarClienteTl(Frame):
    def __init__(self,master):
        self.fonte = ("Verdana", 12)
        master.title('Administração')
        master.resizable(width=False, height=False)

        Frame.__init__(self, master)

        self.idLabel = Label(self,text='ID:',font= self.fonte,fg="black").grid(row=2,pady=(5,0))
        self.idEntry = ttk.Entry(self,width=30)
        self.idEntry.grid(row=2,column=1,padx=(0,10),pady=(6,0))

        self.delButton = ttk.Button(self,text='Deletar Cliente',width=30,command= self.deletarCliente)
        self.delButton.grid(row=7,column=1,padx=(0,70),pady=(20,0))

        self.back = ttk.Button(self,text='Voltar na Tela inicial',width=20,command=lambda: master.trocaPag(PagAdm))
        self.back.grid(row=8,column=1,padx=(0,70),pady=(5,10))

    def deletarCliente(self):
        banco = database.Banco()
        id = self.idEntry.get()
        id = int(id)

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

class consultarClienteTl(Frame):
    def __init__(self,master):
        self.fonte = ("Verdana", 12)
        master.title('Administração')
        master.resizable(width=False, height=False)

        Frame.__init__(self, master)

        self.tituloLabel = Label(self,text='Insira o Id do cliente:',font= ("Verdana", 11,'bold'),fg="black").grid(row=0,columnspan=2,padx=(15,20),pady=(15,0),sticky=W)

        self.idLabel = Label(self,text='Id:',font= self.fonte,fg="black").grid(row=1,padx=(15,0),pady=(5,0),sticky=W)
        self.idEntry = ttk.Entry(self,width=15)
        self.idEntry.grid(row=1,columnspan=2,padx=(0,30),pady=(6,0))

        self.buscarButton = ttk.Button(self,text='Buscar Cliente',width=30,command= self.buscarCliente)
        self.buscarButton.grid(row=2,columnspan=2,pady=(20,0))

        self.back = ttk.Button(self,text='Voltar na Tela inicial',width=20,command=lambda: master.trocaPag(PagAdm))
        self.back.grid(row=3,columnspan=2,pady=(5,10))

    def buscarCliente(self):
        popup = Tk()
        popup.title('Cliente selecionado')
        popup.resizable(width=False,height=False)
        
        frame = Frame(popup)
        frame.grid()
        
        id = int(self.idEntry.get())

        consulta = admLogado.consultarCliente(index.clientes,id)
    
        cpf = consulta.get('cpf')
        nome = consulta.get('nome')
        tel = consulta.get('tel')
        cel = consulta.get('cel')
        estado = consulta.get('estado')
        cidade = consulta.get('cidade')
        bairro = consulta.get('bairro')
        cep = consulta.get('cep')
        rua = consulta.get('rua')
        n = consulta.get('n')
        qnt = consulta.get('carrinho')

        if cel == '' or tel == '':
            if cel == '':
                cel = 'Não informado'
            else:
                tel = 'Não informado'

        Label(frame,text='Cliente Selecionado',font= ("Verdana", 11,'bold'),fg="black").grid(row=0,columnspan=2,padx=(15,15),pady=(10,0),sticky=W)

        Label(frame,text='Itens no carrinho:',font= self.fonte,fg="black").grid(row=1,padx=(15,0),pady=(10,0),sticky=W)
        Label(frame,text=qnt,font= self.fonte).grid(row=1,column=1,padx=(10,15),pady=(10,0),sticky=W)

        Label(frame,text='Nome:',font= self.fonte,fg="black").grid(row=2,padx=(15,0),pady=(10,0),sticky=W)
        Label(frame,text=nome,font= self.fonte).grid(row=2,column=1,padx=(10,15),pady=(10,0),sticky=W)

        Label(frame,text='CPF:',font= self.fonte,fg="black").grid(row=3,padx=(15,0),pady=(5,0),sticky=W)
        Label(frame,text=cpf,font= self.fonte).grid(row=3,column=1,padx=(10,15),pady=(5,0),sticky=W)

        Label(frame,text='Telefone:',font= self.fonte,fg="black").grid(row=4,padx=(15,0),pady=(5,0),sticky=W)
        Label(frame,text=tel,font= self.fonte).grid(row=4,column=1,padx=(10,15),pady=(5,0),sticky=W)
        
        Label(frame,text='Celular:',font= self.fonte,fg="black").grid(row=5,padx=(15,0),pady=(5,0),sticky=W)
        Label(frame,text=cel,font= self.fonte).grid(row=5,column=1,padx=(10,15),pady=(5,0),sticky=W)

        Label(frame,text='Endereço:',font= self.fonte,fg="black").grid(row=6,padx=(15,15),pady=(5,0),sticky=W)
        Label(frame,text=cidade+','+estado,font= self.fonte,fg="black").grid(row=6,column=1,padx=(10,15),pady=(5,0),sticky=W)
        Label(frame,text='CEP: '+cep,font= self.fonte).grid(row=9,columnspan=2,padx=(15,15),pady=(5,0),sticky=W)
        Label(frame,text='Bairro: '+bairro,font= self.fonte).grid(row=10,columnspan=2,padx=(15,15),pady=(5,15),sticky=W)
        Label(frame,text='Rua: '+rua+','+'n:'+n,font= self.fonte).grid(row=8,columnspan=2,padx=(15,15),pady=(5,0),sticky=W)
        
        popup.mainloop()

class listarClientesTl(Frame):
    def __init__(self,master):
        self.fonte = ("Consolas", 10)
        self.fonteColunas = ("Consolas ",11)
        master.title('Administração')
        master.resizable(width=False, height=True)

        Frame.__init__(self, master)

        banco = database.Banco()
        
        c = banco.conexao.cursor()

        c.execute("""
        SELECT * FROM Clientes;
        """)
        Label(self,text='Clientes Cadastrados',font= ("Verdana", 16),fg="black").grid(row=0,columnspan=13,pady=(5,10))
        row = 3
        for linha in c.fetchall():
            tel = linha[3]
            cel = linha[4]
            
            if tel=='':
                tel = '----'
            if cel=='':
                cel = '----'

            Label(self,text=class_.div(90,'—'),fg="black").grid(row=2,columnspan=13)

            Label(self,text='|     ID     |',font= self.fonteColunas,fg="black").grid(row=1,sticky=W)
            Label(self,text=linha[0],font= self.fonte).grid(row=row)
    
            Label(self,text='      Nome      |',font= self.fonteColunas,fg="black").grid(row=1,column=1,sticky=W)
            Label(self,text=linha[2],font= self.fonte).grid(row=row,column=1,sticky=W)
            
            Label(self,text='      CPF      |',font= self.fonteColunas,fg="black").grid(row=1,column=2,sticky=W)
            Label(self,text=linha[1],font= self.fonte).grid(row=row,column=2,sticky=W)
           
            Label(self,text='     Telefone     |',font= self.fonteColunas,fg="black").grid(row=1,column=3,sticky=W)
            Label(self,text= tel,font= self.fonte).grid(row=row,column=3,sticky=W)

            Label(self,text='     Celular     |',font= self.fonteColunas,fg="black").grid(row=1,column=4)
            Label(self,text= cel,font= self.fonte).grid(row=row,column=4,sticky=W)

            Label(self,text='      Estado      |',font= self.fonteColunas,fg="black").grid(row=1,column=5,sticky=W)
            Label(self,text=linha[7],font= self.fonte).grid(row=row,column=5)

            Label(self,text='        Cidade        |',font= self.fonteColunas,fg="black").grid(row=1,column=6,sticky=W)
            Label(self,text=linha[8],font= self.fonte).grid(row=row,column=6,sticky=W)   

            Label(self,text='          Bairro         |',font= self.fonteColunas,fg="black").grid(row=1,column=7,sticky=W)
            Label(self,text=linha[9],font= self.fonte).grid(row=row,column=7,sticky=W)

            Label(self,text='          Rua         |',font= self.fonteColunas,fg="black").grid(row=1,column=8,sticky=W)
            Label(self,text=linha[10],font= self.fonte).grid(row=row,column=8,sticky=W)

            Label(self,text='     Cep     |',font= self.fonteColunas,fg="black").grid(row=1,column=9,sticky=W)
            Label(self,text=linha[11],font= self.fonte).grid(row=row,column=9,sticky=W)

            Label(self,text='     Número     |',font= self.fonteColunas,fg="black").grid(row=1,column=10,sticky=W)
            Label(self,text=linha[12],font= self.fonte).grid(row=row,column=10)
         
            row+=1
            Label(self,text=class_.div(90,'—'),fg="black").grid(row=row,columnspan=13)
            row+=1

        self.back = ttk.Button(self,text='Voltar na Tela inicial',width=20,command=lambda: master.trocaPag(PagAdm))
        self.back.grid(row=row,columnspan=13,pady=(20,20))

        c.close()

app = AppInicial()
app.mainloop()
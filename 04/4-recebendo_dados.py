from tkinter import *
# Importa todos os módulos e funções do tkinter, uma biblioteca padrão do Python usada para criar interfaces gráficas (GUIs).

class Application:
    def __init__(self, master=None):
        # Define o método construtor da classe 'Application'
        # 'master' é o widget principal, por padrão é None

        self.fontePadrao = ("Arial", "10")
        # Define a fonte padrão a ser utilizada nos widgets

        self.primeiroContainer = Frame(master)
        self.primeiroContainer["pady"] = 10
        self.primeiroContainer.pack()
        # Cria o primeiro container (Frame) e define um padding vertical de 10 pixels
        # Adiciona o Frame ao widget principal, organizando-o na tela

        self.segundoContainer = Frame(master)
        self.segundoContainer["padx"] = 20
        self.segundoContainer.pack()
        # Cria o segundo container (Frame) e define um padding horizontal de 20 pixels
        # Adiciona o Frame ao widget principal, organizando-o na tela

        self.terceiroContainer = Frame(master)
        self.terceiroContainer["padx"] = 20
        self.terceiroContainer.pack()
        # Cria o terceiro container (Frame) e define um padding horizontal de 20 pixels
        # Adiciona o Frame ao widget principal, organizando-o na tela

        self.quartoContainer = Frame(master)
        self.quartoContainer["pady"] = 20
        self.quartoContainer.pack()
        # Cria o quarto container (Frame) e define um padding vertical de 20 pixels
        # Adiciona o Frame ao widget principal, organizando-o na tela

        self.titulo = Label(self.primeiroContainer, text="Dados do usuário")
        self.titulo["font"] = ("Arial", "10", "bold")
        self.titulo.pack()
        # Cria um Label (rótulo) no primeiro container com o texto "Dados do usuário" e fonte Arial, tamanho 10, negrito

        self.nomeLabel = Label(self.segundoContainer, text="Nome", font=self.fontePadrao)
        self.nomeLabel.pack(side=LEFT)
        # Cria um Label (rótulo) no segundo container com o texto "Nome" usando a fonte padrão
        # Organiza o Label no lado esquerdo do container

        self.nome = Entry(self.segundoContainer)
        self.nome["width"] = 30
        self.nome["font"] = self.fontePadrao
        self.nome.pack(side=LEFT)
        # Cria um campo de entrada de texto (Entry) no segundo container com largura de 30 e fonte padrão
        # Organiza o campo no lado esquerdo do container

        self.senhaLabel = Label(self.terceiroContainer, text="Senha", font=self.fontePadrao)
        self.senhaLabel.pack(side=LEFT)
        # Cria um Label (rótulo) no terceiro container com o texto "Senha" usando a fonte padrão
        # Organiza o Label no lado esquerdo do container

        self.senha = Entry(self.terceiroContainer)
        self.senha["width"] = 30
        self.senha["font"] = self.fontePadrao
        self.senha["show"] = "*"
        self.senha.pack(side=LEFT)
        # Cria um campo de entrada de texto (Entry) no terceiro container com largura de 30 e fonte padrão
        # Configura o campo para mostrar '*' ao invés de caracteres para senhas
        # Organiza o campo no lado esquerdo do container

        self.autenticar = Button(self.quartoContainer)
        self.autenticar["text"] = "Autenticar"
        self.autenticar["font"] = ("Calibri", "8")
        self.autenticar["width"] = 12
        self.autenticar["command"] = self.verificaSenha
        self.autenticar.pack()
        # Cria um botão no quarto container com o texto "Autenticar", fonte Calibri, tamanho 8, e largura de 12
        # Configura o botão para chamar o método 'verificaSenha' quando clicado
        # Adiciona o botão ao container, organizando-o na tela

        self.mensagem = Label(self.quartoContainer, text="", font=self.fontePadrao)
        self.mensagem.pack()
        # Cria um Label (rótulo) no quarto container para mostrar mensagens de feedback
        # O texto inicial é vazio e usa a fonte padrão
        # Adiciona o Label ao container, organizando-o na tela

    def verificaSenha(self):
        # Define o método 'verificaSenha' que será chamado quando o botão de autenticação for clicado
        usuario = self.nome.get()
        senha = self.senha.get()
        if usuario == "aluno" and senha == "dev":
            self.mensagem["text"] = "Autenticado"
            # Se o nome de usuário for "aluno" e a senha for "dev", exibe "Autenticado" no Label de mensagens
        else:
            self.mensagem["text"] = "Erro na autenticação"
            # Caso contrário, exibe "Erro na autenticação" no Label de mensagens

root = Tk()
# Cria uma instância da classe Tk, que é a janela principal da aplicação tkinter
# 'root' é o objeto da janela principal

Application(root)
# Cria uma instância da classe 'Application', passando 'root' como argumento
# Isso inicializa a aplicação com a janela principal como mestre (master)

root.mainloop()
# Inicia o loop principal do tkinter, que espera por eventos e mantém a janela aberta até que seja fechada
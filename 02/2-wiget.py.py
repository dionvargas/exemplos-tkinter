from tkinter import *
# Importa todos os módulos e funções do tkinter, uma biblioteca padrão do Python usada para criar interfaces gráficas (GUIs).

class Application:
    def __init__(self, master=None):
        # Define o método construtor da classe 'Application'
        # 'master' é o widget principal, por padrão é None
        
        self.widget1 = Frame(master)
        # Cria um widget Frame dentro do widget 'master'

        self.widget1.pack(side=RIGHT)
        # Adiciona o Frame ao widget principal, organizando-o na tela no lado direito
        
        self.msg = Label(self.widget1, text="Primeiro widget")
        # Cria um widget Label (rótulo) dentro do Frame 'widget1' com o texto "Primeiro widget"
        
        self.msg["font"] = ("Verdana", "10", "italic", "bold")
        # Configura a fonte do Label para Verdana, tamanho 10, itálico e negrito
        
        self.msg.pack()
        # Adiciona o Label ao Frame, organizando-o na tela
        
        self.sair = Button(self.widget1)
        # Cria um widget Button (botão) dentro do Frame 'widget1'
        
        self.sair["text"] = "Sair"
        # Define o texto do botão como "Sair"
        
        self.sair["font"] = ("Verdana", "10")
        # Configura a fonte do botão para Verdana, tamanho 10 (mudança em relação ao código anterior)
        
        self.sair["width"] = 5
        # Define a largura do botão para 5 unidades
        
        self.sair["command"] = self.widget1.quit
        # Configura o comando do botão para chamar o método 'quit' do Frame, fechando a aplicação
        
        self.sair.pack(side=RIGHT)
        # Adiciona o botão ao Frame, organizando-o na tela no lado direito (mudança em relação ao código anterior)

root = Tk()
# Cria uma instância da classe Tk, que é a janela principal da aplicação tkinter
# 'root' é o objeto da janela principal

Application(root)
# Cria uma instância da classe 'Application', passando 'root' como argumento
# Isso inicializa a aplicação com a janela principal como mestre (master)

root.mainloop()
# Inicia o loop principal do tkinter, que espera por eventos e mantém a janela aberta até que seja fechada
from tkinter import *
# Importa todos os módulos e funções do tkinter, uma biblioteca padrão do Python usada para criar interfaces gráficas (GUIs).

class Application:
    def __init__(self, master=None):
        # Define o método construtor da classe 'Application'
        # 'master' é o widget principal, por padrão é None
        
        self.widget1 = Frame(master)
        # Cria um widget Frame dentro do widget 'master'
        
        self.widget1.pack()
        # Adiciona o Frame ao widget principal, organizando-o na tela
        
        self.msg = Label(self.widget1, text="Primeiro widget")
        # Cria um widget Label (rótulo) dentro do Frame 'widget1' com o texto "Primeiro widget"
        
        self.msg["font"] = ("Calibri", "9", "italic")
        # Configura a fonte do Label para Calibri, tamanho 9 e itálico
        
        self.msg.pack()
        # Adiciona o Label ao Frame, organizando-o na tela
        
        self.sair = Button(self.widget1)
        # Cria um widget Button (botão) dentro do Frame 'widget1'
        
        self.sair["text"] = "Clique aqui"
        # Define o texto do botão como "Clique aqui"
        
        self.sair["font"] = ("Calibri", "9")
        # Configura a fonte do botão para Calibri, tamanho 9
        
        self.sair["width"] = 10
        # Define a largura do botão para 10 unidades
        
        self.sair["command"] = self.mudarTexto
        # Configura o comando do botão para chamar o método 'mudarTexto' quando o botão for clicado
        
        self.sair.pack()
        # Adiciona o botão ao Frame, organizando-o na tela

    def mudarTexto(self):
        # Define o método 'mudarTexto' que será chamado quando o botão for clicado
        if self.msg["text"] == "Primeiro widget":
            self.msg["text"] = "O botão recebeu um clique"
            # Se o texto do Label for "Primeiro widget", altera para "O botão recebeu um clique"
        else:
            self.msg["text"] = "Primeiro widget"
            # Caso contrário, altera o texto do Label de volta para "Primeiro widget"

root = Tk()
# Cria uma instância da classe Tk, que é a janela principal da aplicação tkinter
# 'root' é o objeto da janela principal

Application(root)
# Cria uma instância da classe 'Application', passando 'root' como argumento
# Isso inicializa a aplicação com a janela principal como mestre (master)

root.mainloop()
# Inicia o loop principal do tkinter, que espera por eventos e mantém a janela aberta até que seja fechada
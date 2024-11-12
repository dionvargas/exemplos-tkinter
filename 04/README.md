## Recebendo Dados

### Código
``` python
from tkinter import *

class Application:
    def __init__(self, master=None):
        self.fontePadrao = ("Arial", "10")
        self.primeiroContainer = Frame(master)
        self.primeiroContainer["pady"] = 10
        self.primeiroContainer.pack()

        self.segundoContainer = Frame(master)
        self.segundoContainer["padx"] = 20
        self.segundoContainer.pack()

        self.terceiroContainer = Frame(master)
        self.terceiroContainer["padx"] = 20
        self.terceiroContainer.pack()

        self.quartoContainer = Frame(master)
        self.quartoContainer["pady"] = 20
        self.quartoContainer.pack()

        self.titulo = Label(self.primeiroContainer, text="Dados do usuário")
        self.titulo["font"] = ("Arial", "10", "bold")
        self.titulo.pack()

        self.nomeLabel = Label(self.segundoContainer,text="Nome", font=self.fontePadrao)
        self.nomeLabel.pack(side=LEFT)

        self.nome = Entry(self.segundoContainer)
        self.nome["width"] = 30
        self.nome["font"] = self.fontePadrao
        self.nome.pack(side=LEFT)

        self.senhaLabel = Label(self.terceiroContainer, text="Senha", font=self.fontePadrao)
        self.senhaLabel.pack(side=LEFT)

        self.senha = Entry(self.terceiroContainer)
        self.senha["width"] = 30
        self.senha["font"] = self.fontePadrao
        self.senha["show"] = "*"
        self.senha.pack(side=LEFT)

        self.autenticar = Button(self.quartoContainer)
        self.autenticar["text"] = "Autenticar"
        self.autenticar["font"] = ("Calibri", "8")
        self.autenticar["width"] = 12
        self.autenticar["command"] = self.verificaSenha
        self.autenticar.pack()

        self.mensagem = Label(self.quartoContainer, text="", font=self.fontePadrao)
        self.mensagem.pack()

    #Método verificar senha
    def verificaSenha(self):
        usuario = self.nome.get()
        senha = self.senha.get()
        if usuario == "usuariodevmedia" and senha == "dev":
            self.mensagem["text"] = "Autenticado"
        else:
            self.mensagem["text"] = "Erro na autenticação"

root = Tk()
Application(root)
root.mainloop()
```

### Explicação Geral:

**Classe `` Application ``:** Define a estrutura da interface gráfica da aplicação.

**Método `` __init__ ``:** Inicializa a classe `` Application ``, criando containers e widgets com suas propriedades.

**Containers (`` primeiroContainer ``, `` segundoContainer ``, `` terceiroContainer ``, `` quartoContainer ``):** Organizadores para agrupar widgets, cada um com espaçamento (`` pady `` ou `` padx ``).

**Widgets (`` titulo ``, `` nomeLabel ``, `` nome ``, `` senhaLabel ``, `` senha ``, `` autenticar ``, `` mensagem ``):** Rótulos, campos de entrada e botão com suas respectivas configurações de texto, fonte e comandos.

**Método `` verificaSenha ``:** Captura os valores dos campos de entrada de usuário e senha, verifica se estão corretos e atualiza o texto do rótulo de mensagem de acordo com o resultado da verificação.

**Janela Principal (`` root ``):** Cria a janela principal da aplicação tkinter.

**Instância da Classe `` Application ``:** Inicializa a aplicação e cria a interface gráfica dentro da janela principal.

**Loop Principal (`` root.mainloop ``):** Mantém a aplicação em execução, respondendo a eventos até que a janela seja fechada.
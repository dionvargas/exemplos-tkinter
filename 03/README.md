## Event Handler

### Código
``` python
from tkinter import *

class Application:
    def __init__(self, master=None):
        self.widget1 = Frame(master)
        self.widget1.pack()
        self.msg = Label(self.widget1, text="Primeiro widget")
        self.msg["font"] = ("Calibri", "9", "italic")
        self.msg.pack ()
        self.sair = Button(self.widget1)
        self.sair["text"] = "Clique aqui"
        self.sair["font"] = ("Calibri", "9")
        self.sair["width"] = 10
        self.sair["command"] = self.mudarTexto
        self.sair.pack ()

    def mudarTexto(self):
        if self.msg["text"] == "Primeiro widget":
            self.msg["text"] = "O botão recebeu um clique"
        else:
            self.msg["text"] = "Primeiro widget"

root = Tk()
Application(root)
root.mainloop()
```

### Explicação Geral:

**Classe `` Application ``:** Define a estrutura da interface gráfica da aplicação.

**Método `` __init__ ``:** Inicializa a classe `` Application `` criando widgets e configurando suas propriedades.

**Frame (`` widget1 ``):** Cria um container para organizar outros widgets.

**Label (`` msg ``):** Adiciona um rótulo com texto estilizado ao Frame.

**Button (`` sair ``):** Adiciona um botão que muda o texto do Label quando clicado, ligando o evento de clique à função `` mudarTexto ``.

**Método `` mudarTexto ``:** Define a ação a ser executada quando o botão é clicado, alterando o texto do Label entre "Primeiro widget" e "O botão recebeu um clique".

**Janela Principal (`` root ``):** Cria a janela principal da aplicação tkinter.

**Instância da Classe `` Application ``:** Inicializa a aplicação e cria a interface gráfica dentro da janela principal.

**Loop Principal (`` root.mainloop ``):** Mantém a aplicação em execução, respondendo a eventos até que a janela seja fechada.
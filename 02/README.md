## Criação de Wigets

### Código
``` python
from tkinter import *

class Application:
    def __init__(self, master=None):
        self.widget1 = Frame(master)
        self.widget1.pack(side=RIGHT)
        self.msg = Label(self.widget1, text="Primeiro widget")
        self.msg["font"] = ("Verdana", "10", "italic", "bold")
        self.msg.pack ()
        self.sair = Button(self.widget1)
        self.sair["text"] = "Sair"
        self.sair["font"] = ("Verdana", "10")
        self.sair["width"] = 5
        self.sair["command"] = self.widget1.quit
        self.sair.pack (side=RIGHT)
root = Tk()
Application(root)
root.mainloop()
```

### Explicação Geral:

**Classe `` Application ``:** Define a estrutura da interface gráfica da aplicação.

**Método `` __init__ ``:** Inicializa a classe `` Application `` criando widgets e configurando suas propriedades.

**Frame (`` widget1 ``):** Cria um container para organizar outros widgets.

**Label (`` msg ``):** Adiciona um rótulo com texto estilizado ao Frame.

**Button (`` sair ``):** Adiciona um botão que, quando clicado, fechará a aplicação.

**Janela Principal (`` root ``):** Cria a janela principal da aplicação tkinter.

**Instância da Classe `` Application ``:** Inicializa a aplicação e cria a interface gráfica dentro da janela principal.

**Loop Principal (`` root.mainloop ``):** Mantém a aplicação em execução, respondendo a eventos até que a janela seja fechada.
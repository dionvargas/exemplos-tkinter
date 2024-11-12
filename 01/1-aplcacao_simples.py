from tkinter import *
# Importa todos os módulos e funções do tkinter, uma biblioteca padrão do Python usada para criar interfaces gráficas (GUIs).

class Application:
    def __init__(self, master=None):
        pass
    # Define a classe 'Application' com um método construtor (__init__).
    # O método __init__ recebe um parâmetro 'master' que por padrão é None.
    # 'pass' é uma instrução que significa que não há implementação no método neste momento.

root = Tk()
# Cria uma instância da classe Tk, que é a janela principal da aplicação tkinter.
# 'root' é o objeto da janela principal.

Application(root)
# Cria uma instância da classe 'Application', passando 'root' como argumento.
# Isso inicializa a aplicação com a janela principal como mestre (master).

root.mainloop()
# Inicia o loop principal do tkinter, que espera por eventos e mantém a janela aberta até que seja fechada.

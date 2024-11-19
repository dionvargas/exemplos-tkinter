from pathlib import Path
from tkinter import Tk, Canvas, Entry, Text, Button, PhotoImage

class TelaPrincipal:
    def __init__(self, root, assets_path, on_navigate):
        """
        Inicializa a tela principal.

        :param root: Referência para a janela principal.
        :param assets_path: Caminho para os assets.
        :param on_navigate: Função para navegar para outra tela.
        """
        self.root = root
        self.assets_path = Path(assets_path)
        self.on_navigate = on_navigate  # Função para alternar entre telas
        self.setup_ui()

    def relative_to_assets(self, path: str) -> Path:
        """
        Gera o caminho absoluto para os assets.

        :param path: Caminho relativo do asset.
        :return: Caminho absoluto.
        """
        return self.assets_path / Path(path)

    def setup_ui(self):
        from tkinter import Canvas, Button, PhotoImage

        self.root.geometry("320x568")
        self.root.configure(bg="#FFFFFF")

        canvas = Canvas(
            self.root,
            bg="#FFFFFF",
            height=568,
            width=320,
            bd=0,
            highlightthickness=0,
            relief="ridge"
        )
        canvas.place(x=0, y=0)
        canvas.create_rectangle(10.0, 9.0, 310.0, 559.0, fill="#A3D2FF", outline="")
        canvas.create_text(29.0, 20.0, anchor="nw", text="Produtos", fill="#000000", font=("Graduate Regular", 36 * -1))

        # Adicionando um produto com botão
        self.create_product_section(canvas, "Produto 1", 90, "button_1.png", lambda: self.on_button_click(1))
        self.create_product_section(canvas, "Produto 2", 159, "button_2.png", lambda: self.on_button_click(2))
        self.create_product_section(canvas, "Produto 3", 228, "button_3.png", lambda: self.on_button_click(3))
        self.create_product_section(canvas, "Produto 4", 297, "button_4.png", lambda: self.on_button_click(4))
        self.create_product_section(canvas, "Produto 5", 366, "button_5.png", lambda: self.on_button_click(5))
        self.create_product_section(canvas, "Produto 6", 435, "button_6.png", lambda: self.on_button_click(6))

        self.root.resizable(False, False)

    def create_product_section(self, canvas, product_name, y_start, button_image, command):
        from tkinter import Button, PhotoImage

        canvas.create_rectangle(25.0, y_start, 293.0, y_start + 51.0, fill="#D9D9D9", outline="")
        canvas.create_text(39.0, y_start + 10.0, anchor="nw", text=product_name, fill="#000000", font=("Gudea", 24 * -1))

        button_img = PhotoImage(file=self.relative_to_assets(button_image))
        button = Button(
            image=button_img,
            borderwidth=0,
            highlightthickness=0,
            command=command,
            relief="flat"
        )
        button.image = button_img  # Evita descarte da imagem
        button.place(x=236.0, y=y_start + 5.0, width=40.0, height=40.0)

    def on_button_click(self, product_id):
        """
        Callback ao clicar em um botão de produto.

        :param product_id: ID do produto clicado.
        """
        print(f"Produto {product_id} clicado!")
        self.on_navigate(product_id)  # Chama a função de navegação


class TelaSecundaria:
    def __init__(self, root, assets_path, on_back):
        """
        Inicializa a tela secundária.

        :param root: Referência para a janela principal.
        :param assets_path: Caminho para os assets.
        :param on_back: Função para voltar à tela principal.
        """
        self.root = root
        self.assets_path = Path(assets_path)
        self.on_back = on_back  # Função para voltar à tela anterior
        self.setup_ui()

    def relative_to_assets(self, path: str) -> Path:
        """
        Gera o caminho absoluto para os assets.

        :param path: Caminho relativo do asset.
        :return: Caminho absoluto.
        """
        return self.assets_path / Path(path)

    def setup_ui(self):

        self.root.geometry("320x568")
        self.root.configure(bg="#FFFFFF")

        canvas = Canvas(
            self.root,
            bg="#FFFFFF",
            height=568,
            width=320,
            bd=0,
            highlightthickness=0,
            relief="ridge"
        )
        canvas.place(x=0, y=0)
        canvas.create_rectangle(
            10.0,
            9.0,
            310.0,
            559.0,
            fill="#A3D2FF",
            outline=""
        )
        canvas.create_text(
            34.0,
            101.0,
            anchor="nw",
            text="Descrição:",
            fill="#000000",
            font=("Gudea", 24 * -1)
        )
        canvas.create_text(
            34.0,
            302.0,
            anchor="nw",
            text="Valor:",
            fill="#000000",
            font=("Gudea", 24 * -1)
        )
        canvas.create_rectangle(
            33.0,
            71.0,
            282.0,
            72.0,
            fill="#000000",
            outline=""
        )
        canvas.create_text(
            28.0,
            30.0,
            anchor="nw",
            text="produto_nome",
            fill="#000000",
            font=("Graduate Regular", 24 * -1)
        )

        entry_image_1 = PhotoImage(
            file=self.relative_to_assets("entry_1.png"))
        canvas.create_image(
            191.5,
            318.5,
            image=entry_image_1
        )
        entry_1 = Entry(
            bd=0,
            bg="#D9D9D9",
            fg="#000716",
            highlightthickness=0
        )
        entry_1.place(
            x=101.0,
            y=305.0,
            width=181.0,
            height=25.0
        )

        entry_image_2 = PhotoImage(
            file=self.relative_to_assets("entry_2.png"))
        canvas.create_image(
            158.0,
            218.0,
            image=entry_image_2
        )
        entry_2 = Text(
            bd=0,
            bg="#D9D9D9",
            fg="#000716",
            highlightthickness=0
        )
        entry_2.place(
            x=34.0,
            y=140.0,
            width=248.0,
            height=154.0
        )

        # Botão para voltar
        button_img = PhotoImage(file=self.relative_to_assets("button_1.png"))
        back_button = Button(
            image=button_img,
            borderwidth=0,
            highlightthickness=0,
            command=self.on_back,
            relief="flat"
        )
        back_button.image = button_img
        back_button.place(x=34.0,
            y=499.0,
            width=248.0,
            height=40.0)

        self.root.resizable(False, False)


# Gerenciador de navegação
class App:
    def __init__(self, root):
        """
        Inicializa o gerenciador de telas.

        :param root: Janela principal.
        """
        self.root = root
        self.assets_path = Path(r"D:\Dion\Repositories\exemplos-tkinter\05\build\assets")
        self.current_screen = None
        self.show_tela_principal()

    def clear_screen(self):
        """
        Remove todos os widgets da janela.
        """
        for widget in self.root.winfo_children():
            widget.destroy()

    def show_tela_principal(self):
        """
        Exibe a tela principal.
        """
        self.clear_screen()
        self.current_screen = TelaPrincipal(self.root, self.assets_path / "frame0", self.show_tela_secundaria)

    def show_tela_secundaria(self, product_id):
        """
        Exibe a tela secundária com base no produto selecionado.

        :param product_id: ID do produto clicado.
        """
        print(f"Exibindo detalhes do Produto {product_id}.")
        self.clear_screen()
        self.current_screen = TelaSecundaria(self.root, self.assets_path / "frame1", self.show_tela_principal)


# Inicialização
if __name__ == "__main__":
    root = Tk()
    app = App(root)
    root.mainloop()

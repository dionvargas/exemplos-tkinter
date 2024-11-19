## Tkinter Designer

<p align="center">
  <img width="33%" src="../images/tkinter_designer.png" />
</p>

O Tkinter **Designer** é uma ferramenta poderosa que permite criar interfaces gráficas para aplicações em Python de maneira visual. Ele utiliza o **Figma**, uma ferramenta de design, para definir a interface, e converte o layout desenhado em código Python usando a biblioteca **Tkinter**.

### Pré-requisitos
Antes de começar, certifique-se de que possui:

1. Python instalado (versão 3.6 ou superior).
2. Uma conta no Figma (https://figma.com).
3. O repositório do Tkinter Designer configurado:

``` bash
git clone https://github.com/ParthJadhav/Tkinter-Designer.git
cd Tkinter-Designer
pip install -r requirements.txt
```

### Passo a Passo para Criar uma Interface
1. Crie um Design no Figma
    - Acesse o Figma e crie um novo arquivo.
    - Crie o layout da interface usando formas, botões e outros elementos.
    - Certifique-se de:
        - Nomear os elementos (como botões, entradas, textos) de forma única e significativa.
        - Agrupar elementos que pertencem ao mesmo "componente" da interface.

2. Obtenha o Link do Figma
    - No Figma, clique em Compartilhar e copie o link do arquivo.
    - Configure o link para permitir acesso de "qualquer pessoa com o link".
3. Execute o Tkinter Designer
    - Acesse o diretório do Tkinter Designer:
    ``` bash
    cd Tkinter-Designer
    ```
    - Execute o script principal:
    ``` bash
    python tkinter_designer.py
    ```
    - Quando solicitado:
        - Cole o link do Figma.
        - Insira sua chave de API do Figma (que pode ser obtida nas configurações da conta do Figma).
4. Gere os Arquivos
- O Tkinter Designer criará uma pasta chamada output.
- Dentro dela, você encontrará:
    - Arquivos Python (.py) gerados automaticamente.
    - Uma pasta de assets contendo as imagens e elementos do layout.

### Estrutura do Arquivo Gerado
O arquivo gerado será um script Python que contém:
- Elementos de interface definidos no layout do Figma (como botões, campos de texto e imagens).
- Código para inicializar uma janela Tkinter e exibir a interface.

Por exemplo, um botão pode ser representado como:
``` python
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
```

### Dicas de Personalização
1. Funções Personalizadas:
    - Substitua lambda: print("button_1 clicked") pela lógica desejada para cada botão.

2. Imagens e Estilos:
    - As imagens dos elementos são salvas na pasta assets. Substitua-as conforme necessário.

3. Classes e Organização:
    - Para projetos maiores, organize o código em classes, separando a lógica de exibição (interface) da lógica de negócio (funcionalidades).

### Limitações
1. Não suporta diretamente funcionalidades complexas (como navegação entre telas).
2. Pode gerar códigos que precisam de ajustes para atender a requisitos específicos.
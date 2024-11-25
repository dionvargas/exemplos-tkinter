
# This file was generated by the Tkinter Designer by Parth Jadhav
# https://github.com/ParthJadhav/Tkinter-Designer


from pathlib import Path

# from tkinter import *
# Explicit imports to satisfy Flake8
from tkinter import Tk, Canvas, Entry, Text, Button, PhotoImage


OUTPUT_PATH = Path(__file__).parent
ASSETS_PATH = OUTPUT_PATH / Path(r"D:\Dion\Repositories\exemplos-tkinter\05\build\assets\frame1")


def relative_to_assets(path: str) -> Path:
    return ASSETS_PATH / Path(path)


window = Tk()

window.geometry("320x568")
window.configure(bg = "#FFFFFF")


canvas = Canvas(
    window,
    bg = "#FFFFFF",
    height = 568,
    width = 320,
    bd = 0,
    highlightthickness = 0,
    relief = "ridge"
)

canvas.place(x = 0, y = 0)
canvas.create_rectangle(
    10.0,
    9.0,
    310.0,
    559.0,
    fill="#A3D2FF",
    outline="")

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
    outline="")

canvas.create_text(
    28.0,
    30.0,
    anchor="nw",
    text="produto_nome",
    fill="#000000",
    font=("Graduate Regular", 24 * -1)
)

entry_image_1 = PhotoImage(
    file=relative_to_assets("entry_1.png"))
entry_bg_1 = canvas.create_image(
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
    file=relative_to_assets("entry_2.png"))
entry_bg_2 = canvas.create_image(
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

button_image_1 = PhotoImage(
    file=relative_to_assets("button_1.png"))
button_1 = Button(
    image=button_image_1,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: print("button_1 clicked"),
    relief="flat"
)
button_1.place(
    x=34.0,
    y=499.0,
    width=248.0,
    height=40.0
)
window.resizable(False, False)
window.mainloop()
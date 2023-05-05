from tkinter import *
from tkinter import ttk
from connect import cursor
import numpy as np
from web import Web

janela = Tk()


class App:
    def __init__(self):
        self.marcas = ["Todas", "Xiaomi", "Asus", "Samsung", "Realme", "Motorola"]
        self. janela = janela
        self.tela()
        self.frames()
        # self.labels()
        # self.botoes()
        # self.lista_frame1()
        janela.mainloop()

    def tela(self):
        self.janela.title('Kabum Search')
        self.janela.geometry('700x700')
        self.janela.iconbitmap('src\kbm.ico')
        self.janela.configure(background='#0060b1')
        # #ff6501 laranja
        self.janela.resizable(True, True)
        self.janela.maxsize(width=700, height=700)
    
    def frames(self):
        self.frame_0 = Frame(self.janela, bg='#ff6501', highlightthickness=1, highlightbackground='#332F2E')
        self.frame_0.place(relx=0.03, rely=0.03, relwidth=0.94, relheight=0.10)
    
    def botoes(self):
        self.btAtualizar = ttk.Button(self.frame_0, text="Atualizar", command=self.atualizar)
        self.btAtualizar.pack(side=RIGHT, padx=10, pady=10)


if __name__ == '__main__':
    App()

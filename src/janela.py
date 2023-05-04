from tkinter import *
from tkinter import ttk
from connect import cursor
import matplotlib.pyplot as plt
import numpy as np
from web import Web

janela = Tk()


class App:
    def __init__(self):
        self.marcas = ["Todas", "Xiaomi", "Asus", "Samsung", "Realme", "Motorola"]
        self. janela = janela
        self.tela()
        # self.frames()
        # self.labels()
        # self.botoes()
        # self.lista_frame1()
        janela.mainloop()

    def tela(self):
        self.janela.title('Kabum Search')
        self.janela.geometry('700x700')
        self.janela.iconbitmap('kbm.ico')
        self.janela.configure(background='#0060b1')
        # #ff6501 laranja
        self.janela.resizable(True, True)
        self.janela.maxsize(width=700, height=700)


if __name__ == '__main__':
    App()

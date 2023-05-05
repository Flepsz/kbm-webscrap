from tkinter import *
from tkinter import ttk
from connect import cursor
from web import Web

janela = Tk()


class App:
    def __init__(self):
        self.marcas = ["Todas", "Xiaomi", "Iphone", "Asus", "Samsung", "Motorola"]
        self. janela = janela
        self.tela()
        self.frames()
        self.labels()
        self.botoes()
        self.lista_frame1()
        janela.mainloop()

    def tela(self):
        self.janela.title('Kabum Search')
        self.janela.geometry('700x700')
        self.janela.iconbitmap('kbm.ico')
        self.janela.configure(background='#0060b1')
        self.janela.resizable(True, True)
        self.janela.maxsize(width=700, height=700)
    
    def frames(self):
        self.frame_0 = Frame(self.janela, bg='#ff6501', highlightthickness=1, highlightbackground='#332F2E')
        self.frame_0.place(relx=0.03, rely=0.03, relwidth=0.94, relheight=0.15)

        self.frame_1 = Frame(self.janela, bg='#ff6501', highlightthickness=1, highlightbackground='#332F2E')
        self.frame_1.place(relx=0.03, rely=0.20, relwidth=0.94, relheight=0.45)

    def botoes(self):
        self.btPesquisar = Button(self.frame_0, text="Pesquisar", fg='#011013', bg='#fff', relief='flat', command=self.pesquisar)
        self.btPesquisar.place(relx=0.28, rely=0.32, relwidth=0.1, relheight=0.3)

        self.btAtualizar = Button(self.frame_0, text='Atualizar', fg='#011013', bg='#fff', relief='flat', command=self.atualizar)
        self.btAtualizar.place(relx=0.41, rely=0.32, relwidth=0.1, relheight=0.3)

    def labels(self):
        self.label_marcas = Label(self.frame_0, text="Marcas:", font=("Arial", 12), fg='#fff', bg='#ff6501')
        self.label_marcas.place(relx=0.05, rely=0.10)

        self.combo_marcas = ttk.Combobox(self.frame_0, values=self.marcas, font=("sans-serif", 12))
        self.combo_marcas.set(self.marcas[0])
        self.combo_marcas.pack()
        self.combo_marcas.place(relx=0.05, rely=0.32, relwidth=0.2, relheight=0.32)

    def lista_frame1(self):
        self.trviewKbm = ttk.Treeview(self.frame_1, height=3, columns=('col1',
                                                                       'col2',
                                                                       'col3',
                                                                       'col4'))
        self.trviewKbm.heading('#0', text='')
        self.trviewKbm.heading('#1', text='ID')
        self.trviewKbm.heading('#2', text='Modelo')
        self.trviewKbm.heading('#3', text='Preço (R$)')

        self.trviewKbm.column('#0', width=0)
        self.trviewKbm.column('#1', width=35, anchor=CENTER)
        self.trviewKbm.column('#2', width=358)
        self.trviewKbm.column('#3', width=200, anchor=CENTER)

        self.trviewKbm.place(relx=0.025, rely=0.05, relwidth=0.95, relheight=0.90)

        self.scroolLista = Scrollbar(self.frame_1, orient='vertical')
        self.trviewKbm.configure(yscrollcommand=self.scroolLista.set)
        self.scroolLista.place(relx=0.96, rely=0.0525, relwidth=0.02, relheight=0.895)

    def limpar(self):
        self.trviewKbm.delete(*self.trviewKbm.get_children())

    def atualizar(self):
        self.limpar()
        marca = self.combo_marcas.get().lower()

        cursor.execute(f"SELECT id, modelo, preco FROM phone_{marca}")

        for row in cursor.fetchall():
            self.trviewKbm.insert("", "end", values=row)

    def pesquisar(self):
        marca = self.combo_marcas.get().lower()
        Web(marca)

        self.limpar()
        query = f"SELECT * FROM phone_{marca}"
        cursor.execute(query)

        resultados = cursor.fetchall()

        frame = []
        for resultado in resultados:
            frame.append(resultado)

        self.atualizar()


if __name__ == '__main__':
    App()

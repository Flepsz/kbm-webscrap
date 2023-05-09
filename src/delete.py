from tkinter import messagebox
from connect import cursor, con


def del_usuario(marca, idPhone):
    try:
        sql = f"""DELETE FROM phone_{marca} WHERE id = '{idPhone}';"""
        cursor.execute(sql)
        con.commit()
        messagebox.showinfo(title="Sucesso",
                            message="Dado Apagado!")
    except:
        messagebox.showerror(title="Erro",
                             message="Sem dados, não foi encontrado nenhum resultado para apagar. Tente pesquisar!")

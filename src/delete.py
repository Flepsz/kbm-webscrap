import mysql.connector
from connect import cursor, con


def del_usuario(marca, idPhone):
    try:
        sql = f"""DELETE FROM phone_{marca} WHERE id = '{idPhone}';"""
        cursor.execute(sql)
        con.commit()
        print("Sucesso ao apagar os dados...")
    except:
        print("Erro ao apagar os dados...")

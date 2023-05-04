from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep
from connect import con, cursor


class Web:
    def __init__(self, marca):
        self.marca = marca  # Marcas: asus, xiaomi, samsung, realme, motorola e todas
        if self.marca == "todas":
            self.site = 'https://www.kabum.com.br/celular-smartphone/smartphones'
        else:
            self.site = f'https://www.kabum.com.br/celular-smartphone/smartphones/smartphone-{self.marca}'
        self.map = {
            'descricao': {
                'xpath': '/html/body/div[1]/div[1]/div[3]/div/div/div[2]/div/main/div[%desc%]/a/div/button/div/h2/span'
            },
            'preco': {
                'xpath': '/html/body/div[1]/div[1]/div[3]/div/div/div[2]/div/main/div[%preco%]/a/div/div/span[2]'
            }
        }
        self.con = con
        self.cursor = cursor
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()
        self.criar_tabela()
        self.scrap()

    def scrap(self):
        self.driver.get(self.site)
        sleep(5)
        resultados = []
        for i in range(1, 11):
            descricao = self.driver.find_element(By.XPATH, self.map['descricao']['xpath'].replace('%desc%', f'{i}')).text
            preco = self.driver.find_element(By.XPATH, self.map['preco']['xpath'].replace('%preco%', f'{i}')).text
            preco_new = preco[3:]
            resultados.append((descricao, preco_new))

        query = f"INSERT INTO phone_{self.marca} (modelo, preco) VALUES (%s, %s)"

        self.cursor.executemany(query, resultados)
        self.con.commit()

    def criar_tabela(self):
        self.cursor.execute(
            f"SELECT * FROM information_schema.tables WHERE table_name = 'phone_{self.marca}'")
        table_exists = self.cursor.fetchone()

        if table_exists:
            self.cursor.execute(f"DROP TABLE IF EXISTS phone_{self.marca}")

        self.cursor.execute(
            f"CREATE TABLE phone_{self.marca} (id INT AUTO_INCREMENT PRIMARY KEY,modelo varchar (255) NOT NULL,preco varchar (255));")
        self.con.commit()


if __name__ == '__main__':
    Web('todas')

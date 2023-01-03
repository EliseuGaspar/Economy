import json, sqlite3 as db
from time import sleep


class Conversor():

    def __init__(self):
        pass

    def Converter(self,dados):
        #   Conecting DATABASE
        self.bd = db.connect('admin/databases/cambio.db')
        self.cursor = self.bd.cursor()

        self.dados = self.cursor.execute(
            f"""SELECT Compra FROM {dados['banco']} WHERE Moeda like '{dados['moeda']}' """
        ).fetchall()

        self.dados = self.dados[0]
        self.dados = self.dados[0]

        resultado = float(self.dados.replace(',','.')) * float(dados['valor'])
        #sleep(10)
        return {'valor':resultado}
        


if __name__ == '__main__':
    Conversor()
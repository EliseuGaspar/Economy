import json, sqlite3 as db
from time import sleep


class Cambios():

    def __init__(self):
        pass

    def GET(self,bank):
        #   Conecting DATABASE
        DIC = {}
        self.bd = db.connect('admin/databases/cambio.db')
        self.cursor = self.bd.cursor()

        self.dados = self.cursor.execute(
            f"SELECT * FROM '{bank}' "
        ).fetchall()

        data = self.cursor.execute(
            f"select data FROM '{bank}' WHERE id like 1"
        ).fetchall()

        tamanho = self.cursor.execute(
            f"select Tamanho FROM '{bank}' WHERE id like 1"
        ).fetchall()
        
        ii = 0

        data_ = data[0]
        tamanho_ = tamanho[0]

        DIC['Data'] = data_[0]
        DIC['Tamanho'] = tamanho_[0]
        for data in self.dados:
            DIC[f'{data[0]}'] = {
                "Moeda":f"{data[1]}",
                "Compra":f"{data[2]}",
                "Venda":f"{data[3]}"
            }
            ii += 1
        #sleep(10)
        return DIC


    def POST(self,data):
        DIC = {}
        self.bd = db.connect('admin/databases/cambio.db')
        self.cursor = self.bd.cursor()

        self.cursor.execute(f"delete from '{data['banco']}'")

        print(data['banco'])
        for ii in range(data['Tamanho']):
            self.cursor.execute(
                f"INSERT INTO {data['banco']} VALUES ({ii}, '{data[str(ii)]['Moeda']}' , '{data[str(ii)]['Compra']}' , '{data[str(ii)]['Venda']}' , '{data['Data']}' , {data['Tamanho']} )")

        verificador = self.cursor.execute(f"select Moeda from '{data['banco']}'").fetchall()

        self.bd.commit()
        self.bd.close()

        return {'code':200}



if __name__ == '__main__':
    Cambios()
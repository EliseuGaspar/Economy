import sqlite3 as db
from flask import jsonify

class Teste_():

    def __init__(self):
        pass

    def GET(self):
        #   Conecting DATABASE
        DIC = {}
        self.bd = db.connect('admin/databases/teste.db')
        self.cursor = self.bd.cursor()

        self.datas = self.cursor.execute(
            f"SELECT * FROM 'Testes' "
        ).fetchall()

        self.datas_format = self.datas
        ii = 0

        for data in self.datas_format:
            DIC[f'{data[0]}'] = {
                "Tema":f"{data[1]}",
                "Header":f"{data[2]}",
                "Body":f"{data[3]}",
                "img_url":f"{data[4]}",
                "content_url":f"{data[5]}"
            }
            ii += 1


        return DIC

    def POST(self, datas):
        self.datas = datas
        return datas
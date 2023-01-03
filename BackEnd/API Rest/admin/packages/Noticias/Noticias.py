import json, sqlite3 as db

class Noticia():

    def __init__(self):
        self.GET()

    def GET(self):
        #   Conecting DATABASE
        DIC = {}
        self.bd = db.connect('admin/databases/noticias.db')
        self.cursor = self.bd.cursor()

        self.dados = self.cursor.execute(
            f"SELECT * FROM 'Noticias' "
        ).fetchall()
        
        ii = 0
        T = self.dados[0]
        DIC['Tamanho'] = T[8]
        for data in self.dados:
            DIC[f'{data[0]}'] = {
                "Tema":f"{data[1]}",
                "Cabeca":f"{data[2]}",
                "Corpo":f"{data[3]}",
                "Data":f"{data[4]}",
                "Hora":f"{data[5]}",
                "Link":f"{data[6]}",
                "Imagem":f"{data[7]}"
            }
            ii += 1

        return DIC

    def POST(self,data):
        self.bd = db.connect('admin/databases/noticias.db')
        self.cursor = self.bd.cursor()

        self.cursor.execute(f"delete from 'Noticias'")

        for ii in range(data['Tamanho']):
            print(ii)
            self.cursor.execute(
                f"""INSERT INTO Noticias VALUES ({ii},
                '{data[str(ii)]["Titulo"]}' , '{data[str(ii)]["Cabeca"]}' ,
                '{data[str(ii)]["Corpo"]}' , '{data[str(ii)]["Data"]}' ,
                '{data[str(ii)]["Hora"]}' , '{data[str(ii)]["Link"]}' ,
                '{data[str(ii)]["Imagem"]}' ,{data["Tamanho"]} )""")

        #verificador = self.cursor.execute(f"select Moeda from '{data['banco']}'").fetchall()

        self.bd.commit()
        self.bd.close()

        return {'code':200}



if __name__ == '__main__':
    Noticia()
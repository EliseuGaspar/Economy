from bs4 import BeautifulSoup
import requests as r
import urllib as ur
import os
from time import sleep


class Scraping_News():

    def __init__(self):

        Noticia = self.Noticias()
        #resposta = r.post('http://localhost:1111/noticias',json=Noticia)
        print(Noticia)
        print(f"Resposta_Noticia: {resposta.status}")

    
    def Noticias(self):
        try:
            lista_de_titulos2 = []
            lista_de_horas2 = []
            lista_de_datas2 = []
            lista_de_url = []
            lista_de_imagens = []
            lista_imagem_url = []
            DIC = {}
            i = 1
            caminho = 'https://www.jornaldeangola.ao'

            link2 = ur.request.urlopen("https://www.jornaldeangola.ao/ao/noticias/index.php?tipo=1&idSec=15")

            soup2 = BeautifulSoup(link2.read(), 'html.parser')

            lista_de_noticias = soup2.select('.container .row .col-lg-3 .item-noticia a')
            lista_de_titulos = soup2.select('.container .row .col-lg-3 .item-noticia h2')
            lista_de_datas = soup2.select('.container .row .col-lg-3 .item-noticia .data span:nth-of-type(1)')
            lista_de_horas = soup2.select('.container .row .col-lg-3 .item-noticia .data span:nth-of-type(2) span')
            lista_de_capas = soup2.select('.container .row .col-lg-3 .item-noticia a .capa')
            
            for titulo in lista_de_titulos:
                lista_de_titulos2.append(titulo.get_text())

            for hora in lista_de_horas:
                lista_de_horas2.append(hora.get_text())

            for data in lista_de_datas:
                if(i%2 != 0):
                    lista_de_datas2.append(data.get_text())
                i+= 1

            for link in lista_de_noticias:
                lista_de_url.append(link.get('href'))

            for link in lista_de_capas:
                lista_de_imagens.append(link.get('style'))

            for url in lista_de_imagens:
                lista_imagem_url.append(url[url.find('(')+1:url.rfind(')')])
            
            DIC['Tamanho'] = len(lista_de_titulos2)
            for x in range(len(lista_de_titulos2)):
                Resto = self.Noticias_Conteudo({'url':f"{caminho+lista_de_url[x]}",'url_img':f"{caminho+lista_imagem_url[x]}"})
                DIC[f'{x}'] = {
                    "Titulo":f"{lista_de_titulos2[x]}",
                    "Data":f"{lista_de_datas2[x]}",
                    "Hora":f"{lista_de_horas2[x]}",
                    "Cabeca":f"{Resto['Cabeca']}",
                    "Corpo":f"{Resto['Corpo']}",
                    "Imagem":f"{Resto['img']}",
                    "Link":f"{caminho+lista_de_url[x]}"
                }
            return DIC
        except:
            resposta = {
                "Status":400,
                "msg":"Erro! Sem resposta do servidor!"
            }
            return resposta

    
    def Noticias_Conteudo(self,url):
        DIC = {}
            
        link = r.get(f"{url['url']}")
        link2 = ur.request.urlopen(f"{url['url']}")

        soup = BeautifulSoup(link.content, 'html.parser')
        soup2 = BeautifulSoup(link2.read(), 'html.parser')

        titulo_cabecario = soup.select('.col-lg-6 .font-weight-bold')
        conteudo = soup.select('.col-lg-6 .body-news')

        DIC['Cabeca'] = titulo_cabecario[1].get_text().replace('\t',' ')
        DIC['Cabeca'] = DIC['Cabeca'].replace('\n','<br>')
        DIC['Cabeca'] = DIC['Cabeca'].replace('\r',' ')
        DIC['Corpo'] = conteudo[0].get_text().replace('\t',' ')
        DIC['Corpo'] = DIC['Corpo'].replace('\n',' ')
        DIC['Corpo'] = DIC['Corpo'].replace('\r',' ')
        DIC['Corpo'] = DIC['Corpo'].replace('. ','.')
        DIC['Corpo'] = DIC['Corpo'].replace('.','. ')
        DIC['img'] = url['url_img']

        return DIC


if __name__ == '__main__':
    Scraping_News()
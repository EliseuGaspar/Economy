from time import sleep
from schedule import (every, repeat, run_pending)
from admin.Noticia.Noticia import Scraping_News
from admin.Bancos.Banco import Scraping_Banking
p = 1


@repeat(every(5).seconds)
def Atualizador_API():
    #print('Atualizando Câmbios')
    #Scraping_Banking()
    print('Atualizando Noticias')
    Scraping_News()


while True:
    run_pending()
    sleep(1)
    print(p)
    p+=1
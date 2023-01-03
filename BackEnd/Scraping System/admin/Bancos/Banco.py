from bs4 import BeautifulSoup
import requests as r
import urllib as ur
import json as j
from admin.email_alert import Send_Alert as s


class Scraping_Banking():

    def __init__(self):
        
        BNI = self.BNI()
        if(BNI != 400):
            BNI['banco'] = 'BNI'
            resposta = r.post('http://localhost:1111/cambio',json=BNI)
            print(resposta.json())
        else:
            s.Send_Alert_Email()

        BAI = self.BAI()
        if(BAI != 400):
            BAI['banco'] = 'BAI'
            resposta = r.post('http://localhost:1111/cambio',json=BAI)
            print(resposta.json())
        else:
            s.Send_Alert_Email()

        FB = self.FB()
        if(FB != 400):
            FB['banco'] = 'FB'
            resposta = r.post('http://localhost:1111/cambio',json=FB)
            print(resposta.json())
        else:
            s.Send_Alert_Email()

        BDA = self.BDA()
        if(BDA != 400):
            BDA['banco'] = 'BDA'
            resposta = r.post('http://localhost:1111/cambio',json=BDA)
            print(resposta.json())
        else:
            s.Send_Alert_Email()

        BCI = self.BCI()
        if(BCI != 400):
            BCI['banco'] = 'BCI'
            resposta = r.post('http://localhost:1111/cambio',json=BCI)
            print(resposta.json())
        else:
            s.Send_Alert_Email()

        SOL = self.SOL()
        if(SOL != 400):
            SOL['banco'] = 'SOL'
            resposta = r.post('http://localhost:1111/cambio',json=SOL)
            print(resposta.json())
        else:
            s.Send_Alert_Email()

        BFA = self.BFA()
        if(BFA != 400):
            BFA['banco'] = 'BFA'
            resposta = r.post('http://localhost:1111/cambio',json=BFA)
            print(resposta.json())
        else:
            s.Send_Alert_Email(s)

        BIC = self.BIC()
        if(BIC != 400):
            BIC['banco'] = 'BIC'
            resposta = r.post('http://localhost:1111/cambio',json=BIC)
            print(resposta.json())
        else:
            s.Send_Alert_Email()

    
    def BNI(self):
        #Banco de Negócios Internacionais
        try:
            lista_de_vendas = []
            lista_de_moedas = []
            lista_de_compras = []
            DIC = {}

            link = r.get("https://www.bni.ao/pt/particulares/")
            link2 = ur.request.urlopen("https://www.bni.ao/pt/taxas")

            soup = BeautifulSoup(link.content, 'html.parser')
            soup2 = BeautifulSoup(link2.read(), 'html.parser')

            lista_de_moedas = soup.select('.col-md-7')
            lista_de_compras = soup.select('.buy-value')
            lista_de_vendas = soup.select('.sell-value')
            data_element = soup2.select('tr td:nth-of-type(5)')

            data_text = data_element[0].get_text()
            data_text = data_text.replace(" ","")
            data_text = data_text.replace("\n","")
            data_text = data_text.replace("\r","")

            DIC['Tamanho'] = len(lista_de_compras);
            DIC['Data'] = data_text
            DIC['Status'] = 200
            for x in range(len(lista_de_vendas)):
                DIC[f'{x}'] = {
                    "Moeda":f"{lista_de_moedas[x].get_text()}",
                    "Compra":f"{lista_de_compras[x].get_text()}",
                    "Venda":f"{lista_de_vendas[x].get_text()}"
                }
            return DIC
        except:
            return 400
    
    
    def BAI(self):
        #Banco Angolano de Investimento
        try:
            lista_de_vendas = []
            lista_de_paises = []
            lista_de_compras = []
            DIC = {}

            link = r.get("https://www.bancobai.ao/pt/cambios-e-valores")
            link2 = r.get("https://www.bancobai.ao/pt/particulares")

            soup = BeautifulSoup(link.content, 'html.parser')
            soup2 = BeautifulSoup(link2.content, 'html.parser')

            conteudo = soup.find('table', class_='table-striped')
            body = conteudo.find('tbody')

            lista_de_paises = body.find_all('div', class_='coin-val')
            lista_de_compras = body.find_all('td', class_='b-right')
            lista_de_vendas = body.select('tr td:nth-of-type(4)')
            data_element = soup2.select('.updated-on')

            data_text = data_element[0].get_text()
            data_text = data_text.replace(" ","")
            data_text = data_text.replace("\n","")
            data_text = data_text.replace("\r","")

            DIC['Tamanho'] = len(lista_de_vendas);
            data_text = data_text[data_text.find('m')+1:len(data_text)]
            DIC['Data'] = data_text[:10]
            DIC['Status'] = 200
            for x in range(len(lista_de_vendas)):
                DIC[f'{x}'] = {
                    "Moeda":f"{lista_de_paises[x].get_text()}",
                    "Compra":f"{lista_de_compras[x].get_text()}",
                    "Venda":f"{lista_de_vendas[x].get_text()}"
                }
            return DIC
        except:
            return 400

    
    def FB(self):
        #FiniBanco
        try:
            lista_de_vendas = []
            lista_de_moedas = []
            lista_de_compras = []
            DIC = {}


            link = r.get("https://www.finibancoangola.co.ao/pt/particulares/")
            link2 = ur.request.urlopen("https://www.finibancoangola.co.ao/pt/particulares/")

            soup = BeautifulSoup(link.content, 'html.parser')
            soup2 = BeautifulSoup(link2.read(), 'html.parser')

            lista_de_moedas = soup.select('div.currency')
            lista_de_compras = soup.select('.value div:nth-of-type(1) span:nth-of-type(2)')
            lista_de_vendas = soup.select('.value div:nth-of-type(2) span:nth-of-type(2)')


            DIC['Tamanho'] = len(lista_de_compras);
            DIC['Data'] = 'None'
            DIC['Status'] = 200
            for x in range(len(lista_de_vendas)):
                moeda = lista_de_moedas[x].get_text()
                moeda = moeda.replace(' ','')
                moeda = moeda.replace('\n','')
                moeda = moeda.replace('\r','')
                DIC[f'{x}'] = {
                    "Moeda":f"{moeda}",
                    "Compra":f"{lista_de_compras[x].get_text()}",
                    "Venda":f"{lista_de_vendas[x].get_text()}"
                }
            return DIC
        except:
            return 400

    
    def BDA(self):
        #Banco de Desenvolvimento Angolano
        try:
            lista_de_vendas = []
            lista_de_moedas = []
            lista_de_compras = []
            DIC = {}
            link = r.get("https://bda.ao/pt-pt/")
            link2 = ur.request.urlopen("https://bda.ao/pt-pt/")
            soup = BeautifulSoup(link.content, 'html.parser')
            soup2 = BeautifulSoup(link2.read(), 'html.parser')
            lista_de_moedas = soup.select('.finance-table  .finance-table-board-col:nth-of-type(1)')
            lista_de_compras = soup.select('.finance-table .finance-table-board-col:nth-of-type(2)')
            lista_de_vendas = soup.select('.finance-table  .finance-table-board-col:nth-of-type(3)')
            data_element = soup2.select('.updated')
            data_text = data_element[0].get_text()
            data_text = data_text.replace(" ","")
            data_text = data_text.replace("\n","")
            data_text = data_text.replace("\r","")
            DIC['Tamanho'] = len(lista_de_vendas);
            DIC['Data'] = data_text[data_text.find(',')+1:data_text.rfind(',')]
            for x in range(len(lista_de_compras)):

                moeda = lista_de_moedas[x].get_text()
                moeda = moeda.replace(' ','')
                moeda = moeda.replace('\n','')
                moeda = moeda.replace('\r','')

                compra = lista_de_compras[x].get_text()
                compra = compra.replace(' ','')
                compra = compra.replace('\n','')
                compra = compra.replace('\t','')

                venda = lista_de_vendas[x].get_text()
                venda = venda.replace(' ','')
                venda = venda.replace('\n','')
                venda = venda.replace('\t','')
                
                DIC[f'{x}'] = {
                    "Moeda":f"{moeda}",
                    "Compra":f"{compra}",
                    "Venda":f"{venda}"
                }
            return DIC
        except:
            return 400


    def BCI(self):
        #Banco de Comércio e Industruia
        try:
            DIC = {}
            DIC2 = {}

            indece = 0;

            link = 'https://ib.bci.ao/MDW-SI/api/internet/exchange/table?currency=AKZ'

            JSON = r.get(link)

            DIC2['Dados'] = j.loads(JSON.content)

            print()

            data_ = DIC2['Dados']['data']['lastUpdateDate']
            DIC['Data'] = data_[:10]

            for x in range(len(DIC2['Dados']['data']['exchangeTableEntryViewList'])):
                if(x%2 == 0):
                    DIC[f'{indece}'] = {
                        "Moeda":f"{DIC2['Dados']['data']['exchangeTableEntryViewList'][x]['currency']}",
                        "Compra":f"{DIC2['Dados']['data']['exchangeTableEntryViewList'][x]['sellValue']}",
                        "Venda":f"{DIC2['Dados']['data']['exchangeTableEntryViewList'][x]['buyValue']}"
                    }

                    indece += 1

            DIC['Tamanho'] = indece

            return DIC
        except:
            return 400


    def SOL(self):
        #Banco SOL
        try:
            DIC = {}
            DIC2 = {}

            indece = 0;

            link = 'https://solnet.ao/MDW-portal/internet/exchange/table?currency=AKZ&quotationDate=2022-12-30T23%3A33%3A17.422Z&noCacheHelper=1672443198825&clientApp=Web&appVersion=v1.2.13'

            JSON = r.get(link)

            DIC2['Dados'] = j.loads(JSON.content)

            data_ = DIC2['Dados']['data']['lastUpdateDate']
            DIC['Data'] = data_[:10]

            for x in range(len(DIC2['Dados']['data']['exchangeTableEntryViewList'])):
                if(x%2 == 0):
                    DIC[f'{indece}'] = {
                        "Moeda":f"{DIC2['Dados']['data']['exchangeTableEntryViewList'][x]['currency']}",
                        "Compra":f"{DIC2['Dados']['data']['exchangeTableEntryViewList'][x]['sellValue']}",
                        "Venda":f"{DIC2['Dados']['data']['exchangeTableEntryViewList'][x]['buyValue']}"
                    }

                    indece += 1

            DIC['Tamanho'] = indece

            return DIC
        except:
            return 400


    def BFA(self):
        #Banco de Fomento Angola
        try:
            DIC = {}
            
            DIC2 = {}

            indece = 0;

            link = 'https://www.bfa.ao/api/exchangerates/get/N'

            JSON = r.get(link)

            DIC2['Dados'] = j.loads(JSON.content)

            data_ = str(DIC2['Dados'][0]['Date'])
            data_ = data_[:8]

            DIC['Data'] = data_

            for x in range(len(DIC2['Dados'])):
                DIC[f'{indece}'] = {
                    "Moeda":f"{DIC2['Dados'][x]['Currency']}",
                    "Compra":f"{DIC2['Dados'][x]['Sell']}",
                        "Venda":f"{DIC2['Dados'][x]['Buy']}"
                }

                indece += 1

            DIC['Tamanho'] = indece

            return DIC
        except:
            return 400


    def BIC(self):
        #Banco Internacional de Angola
        try:
            DIC = {}
            DIC2 = {}

            indece = 0;

            link = 'https://www.bancobic.ao/CatalogSearchServices/ExchangeRatesService/ExchangeRates?currencyBase=AKZ&type=D&dateFrom=1672444361825'

            JSON = r.get(link)

            DIC2['Dados'] = j.loads(JSON.content)

            DIC['Data'] = 'None'

            for x in range(len(DIC2['Dados']['exchangeRates'])):
                DIC[f'{indece}'] = {
                    "Moeda":f"{DIC2['Dados']['exchangeRates'][x]['currencyTo']}",
                    "Compra":f"{DIC2['Dados']['exchangeRates'][x]['sell']}",
                    "Venda":f"{DIC2['Dados']['exchangeRates'][x]['buy']}"
                }

                indece += 1

            DIC['Tamanho'] = indece

            return DIC
        except:
            return 400





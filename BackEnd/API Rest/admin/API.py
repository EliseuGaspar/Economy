from flask import (Flask, request, jsonify)
from admin.packages.flask_cors import CORS
from admin.packages.Taxas.Taxas import Taxa
from admin.packages.Cambio.Cambio import Cambios
from admin.packages.Noticias.Noticias import Noticia
from admin.packages.Servicos.Servicos import Servico
from admin.packages.Impostos.Impostos import Imposto
from admin.packages.Conversor.Conversor import Conversor
from admin.packages.Servicos.Televisivos.Moveis import Movel_TVs
from admin.packages.Servicos.Telefonias.Moveis import Movel_Telephones
from admin.packages.Testes.Testes import Teste_


api = Flask(__name__)
cors = CORS(api, resources={r"/*":{"origins":"*"}})




@api.route('/')
def index():
    return {'msg':'API no ar!'}

@api.route('/cambio', methods=['POST'])
def Cambio_route():
    #   ....
    #   ....
    datas = request.json
    resposta = Cambios.POST(Cambios, datas)
    
    return jsonify(resposta)

@api.route('/cambio/<string:banco>')
def CambioGet_route(banco):
    #   ....
    #   ....
    resposta = Cambios.GET(Cambios, banco)
    
    return jsonify(resposta)

@api.route('/converter', methods=['POST'])
def Conversor_route():
    data = request.json
    resposta = Conversor.Converter(Conversor,data)
    return jsonify(resposta)

@api.route('/noticias',methods=['GET','POST'])
def Noticias_route():
    #   ....
    #   ....
    if(request.method == 'POST'):
        dados = request.json
        resposta = Noticia.POST(Noticia,dados)
    else:
        resposta = Noticia.GET(Noticia)
    
    return jsonify(resposta)

@api.route('/impostos', methods=['GET','POST'])
def Impostos_route():
    #   ....
    #   ....
    if request.method == 'POST':
        datas = request.json
        resposta = Imposto.POST(Imposto ,datas)
    else:
        resposta = Imposto.GET(Imposto)
    
    return jsonify(resposta)

@api.route('/taxas', methods=['GET','POST'])
def Taxas_route():
    #   ....
    #   ....
    if request.method == 'POST':
        datas = request.json
        resposta = Taxa.POST(Taxa ,datas)
    else:
        resposta = Taxa.GET(Taxa)
    
    return jsonify(resposta)

@api.route('/servicos', methods=['GET','POST'])
def Servicos_route():
    #   ....
    #   ....
    if (request.method == 'POST'):
        datas = request.json
        resposta = Servico.POST(Servico ,datas)
    else:
        resposta = Servico.GET(Servico)

@api.route('/servicos/telefonias',methods=['GET'])
def ServicoTelefonias_route():

    resposta = Movel_Telephones.GET(Movel_Telephones)

    return jsonify(resposta)

@api.route('/servicos/televisivos',methods=['GET'])
def ServicosTelevisivos_route():

    resposta = Movel_TVs.GET(Movel_TVs)

    return jsonify(resposta)

@api.route('/Teste',methods=['GET','POST'])
def Teste():
    #   ...
    #   ...
    if(request.method == 'POST'):
        datas = request.json
        print(datas)
        resposta = Teste_.POST(Teste_ ,datas)
    else:
        resposta = Teste_.GET(Teste_)
        print(resposta)
    
    return jsonify(resposta)




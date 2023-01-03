// Botões da página

let btn_back_page = document.getElementById("back-page")
let btn_next_page = document.getElementById("next-page")
let btn_menu = document.getElementById("__icone_menu")
let btn_back_menu = document.getElementById("back_menu")
let btn_cambio = document.getElementById("btn_cambio")
let titulo_cambio = document.querySelector("#cambio .titulo h2")
let btn_conversor = document.getElementById("btn_conversor")
let titulo_conversor = document.querySelector("#conversor .titulo h2")
let btn_impostos = document.getElementById("btn_impostos")
let titulo_impostos = document.querySelector("#impostos .titulo h2")
let btn_noticia = document.getElementById("btn_noticias")
let titulo_noticia = document.querySelector("#noticias .titulo h2")
let btn_configs = document.getElementById("configs")
let btn_back_configs = document.getElementById("configs_back")
let btn_converter = document.getElementById("btn_converter")

// Elementos sujeitos a eventos

var menu = document.getElementById("nav_body")
var cambio = document.getElementById("cambio")
var conversor = document.getElementById("conversor")
var impostos = document.getElementById("impostos")
var noticia = document.getElementById("noticias")
var configuracoes = document.getElementById("configuracoes")
var campo_cambio = document.querySelector("#cambio .ul_master div")
var campo_data_cambio = document.querySelector("#cambio .data")
var campo_banco_cambio = document.querySelector("#cambio .info .banco")
var campo_conversor = document.getElementById("valor")
var campo_resultado_conversor = document.getElementById("resultado")
var notificacao = document.getElementById("alert")
var notificacao_context = document.querySelector("#alert p")

// Selects da página

let select_cambio = document.getElementById("select_cambio")
let select_moeda1 = document.getElementById("moeda1")
let select_moeda2 = document.getElementById("moeda2")
let select_noticia = document.getElementById("noticia-item")

// Elementos do artigo noticias

let titulo_artigo = document.getElementById("noticia-titulo")
let imagem_noticia = document.getElementById("noticia-imagem")
let cabecario_noticia = document.getElementById("noticia-cabecario")
let corpo_noticia = document.getElementById("noticia-corpo")

// Variaveis Vazias

var Active;
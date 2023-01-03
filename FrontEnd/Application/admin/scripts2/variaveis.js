// Botões da página

let btn_open_menu = document.getElementById("open-menu")
let btn_exit_menu = document.getElementById("exit-menu")
let btn_conversor = document.getElementById("btn_conversor")
let btn_copy_conversor = document.getElementById("copy")
let btn_cslt_impostos = document.getElementById("btn-cslt-impostos")
let btn_exit_impostos = document.getElementById("impostos-exit")
let btn_cslt_nif = document.getElementById("btn-cslt-nif")
let btn_exit_nif = document.getElementById("NIF-exit")
let btns_app_invoc = [...document.querySelectorAll(".App-Icones")]

// Elementos sujeitos a eventos

var HeaderTitle = document.getElementById("App-name")
var MenuBar = document.getElementById("MenuBar")
var Cambio_App = document.getElementById("cambio")
var Conversor_App = document.getElementById("conversor")
var Noticias_App = document.getElementById("noticias")
var Consultas_App = document.getElementById("consultas")
var More_Apps = document.getElementById("more_apps")
var DashBoard = document.getElementById("dashboard")
var Impostos = document.getElementById("impostos")
var NIF = document.getElementById("NIF")

var campo_cambio = document.getElementById("ul_master")
var campo_data_cambio = document.getElementById("date-update")
var campo_conversao_resultado = document.querySelector(".resultado button:nth-of-type(2)")

// Selects da página

let Cambio_Select = document.getElementById('cambio-select')
let conversor_select = document.getElementById('conversor-select')
let conversor_select_moeda = document.getElementById('conversor-select-moeda')
let noticias_select = document.getElementById('noticia-option')

// Inputs da página

let valor_conversao = document.getElementById("valor1")


// Elementos do artigo noticias

let titulo_artigo = document.querySelector('#titulo-noticia h2')
let imagem_noticia = document.getElementById('imagem-noticia')
let cabecario_noticia = document.querySelector('#cabecario-noticia h4')
let corpo_noticia = document.getElementById('corpo-noticia')

// Awaits das Apps

var await_cambio = document.querySelector('#cambio .await')
var await_conversor = document.querySelector('#conversor .await')


// Variaveis Vazias

var Active;
let DATA;

function Preencher_SelectTemas(data)
{
    select_noticia.innerHTML = ''
    DATA = data;

    for(let ii = 0; ii < data['Tamanho']; ii++){
        select_noticia.innerHTML += `<option value="${ii}">${data[`${ii}`].Tema}</option>`
    }
}


select_noticia.addEventListener('change',async ()=>
{
    /*let url = DATA[`${select_noticia.value}`].url
    let img_url = DATA[`${select_noticia.value}`].url_img
    let conteudo = await Pegar_Conteudo_Noticias(url,img_url)*/
    Inserir_Artigo(DATA[`${select_noticia.value}`])
})


function Inserir_Artigo(data)
{
    titulo_artigo.innerHTML = data['Tema']
    imagem_noticia.style.backgroundImage = `url(${data['Imagem']})`
    cabecario_noticia.innerHTML = data['Cabeca']
    corpo_noticia.innerHTML = data['Corpo']
}
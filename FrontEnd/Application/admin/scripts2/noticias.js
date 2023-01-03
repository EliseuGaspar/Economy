let DATA;

function Preencher_SelectTemas(data)
{
    noticias_select.innerHTML = ''
    DATA = data;

    for(let ii = 1; ii < data['Tamanho']; ii++){
        noticias_select.innerHTML += `<option value="${ii}">${data[`${ii}`].Tema}</option>`
    }

    return DATA[`${noticias_select.value}`]
}


noticias_select.addEventListener('change',async ()=>
{
    Inserir_Artigo(DATA[`${noticias_select.value}`])
})


async function Inserir_Artigo(data)
{
    let image = await BackGroundImageArtigo(`${data['Imagem']}`)
    titulo_artigo.innerHTML = data['Tema']
    imagem_noticia.style.backgroundImage = image;
    cabecario_noticia.innerHTML = data['Cabeca']
    corpo_noticia.innerHTML = data['Corpo']
}

async function BackGroundImageArtigo(link)
{
    imagem_noticia.style.backgroundImage = `url(${link})`;
}


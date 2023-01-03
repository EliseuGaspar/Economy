async function Pegar_Cambios(bank)
{
    let promessa = await fetch(`http://localhost:1111/cambio/${bank}`)

    let conteudo = await promessa.json()

    await InserirCambio(conteudo)

    async function InserirCambio(data)
    {
        campo_cambio.innerHTML = '';

        for (let index = 1; index < data['Tamanho']; index++){
            campo_cambio.innerHTML += `\
            <ul>\
                <li>${data[index].Moeda}</li>\
                <li>${data[index].Compra}</li>\
                <li>${data[index].Venda}</li>\
            </ul>\
            `
            campo_data_cambio.innerHTML = data['Data']
        }
    }

    return conteudo
}

async function Converter_Valor(bank,valor,moeda)
{
    let promessa = await fetch('http://localhost:2010/converter_valores',{
        method:"POST",
        headers: {
            'Content-Type':'application/json'
        },
        body: JSON.stringify(
            {
                "banco":bank,
                "valor":valor,
                "moeda":moeda
            }
        )
    })

    let conteudo = await promessa.json()

    campo_resultado_conversor.innerHTML = ''
    campo_resultado_conversor.innerHTML = conteudo['valor']

    return conteudo['valor']
}

async function Pegar_Noticias()
{
    let promessa = await fetch('http://localhost:1111/noticias')

    let conteudo = await promessa.json()

    return conteudo
}

async function Pegar_Conteudo_Noticias(url,url_img)
{
    let promessa = await fetch('http://localhost:2010/conteudo_noticia',{
        method:"POST",
        headers: {
            'Content-Type':'application/json'
        },
        body: JSON.stringify(
            {
                "url":url,
                "url_img":url_img
            }
        )
    })

    let conteudo = await promessa.json()

    return conteudo
}
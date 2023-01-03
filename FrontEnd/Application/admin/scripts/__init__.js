
btn_menu.addEventListener('click',()=>
{
    if(menu.classList != 'active')
    {
        menu.classList.add('active')
        document.getElementById('nav_bars').classList.add('active')
    }
})

btn_back_menu.addEventListener('click',()=>
{
    menu.classList.remove('active')
    document.getElementById('nav_bars').classList.remove('active')
})

//  Câmbio 

btn_cambio.addEventListener('click',()=>
{
    if(cambio.classList != 'active')
    {
        cambio.classList.add('active')
        Active = cambio
        Pegar_Cambios('BAI')
    }
})

//titulo_cambio.addEventListener('mouseover',()=>
//{
//    titulo_cambio.innerHTML = '<i class="fas fa-arrow-left"></i> TCâmbio'
//})
//
//titulo_cambio.addEventListener('mouseout',()=>
//{
//    titulo_cambio.innerHTML = '<i class="fas fa-coins"></i> TCâmbio'
//})
//
//titulo_cambio.addEventListener('click',()=>
//{
//    cambio.classList.remove('active')
//    titulo_cambio.innerHTML = '<i class="fas fa-coins"></i> TCâmbio'
//})

//  Conversor

btn_conversor.addEventListener('click',async ()=>
{
    if(conversor.classList != 'active')
    {
        conversor.classList.add('active')
        Active = conversor
        let dados = await Pegar_Cambios('BAI')
        Preencher_Select2(dados)
    }
})

//titulo_conversor.addEventListener('mouseover',()=>
//{
//    titulo_conversor.innerHTML = '<i class="fas fa-arrow-left"></i> TConversor'
//})
//
//titulo_conversor.addEventListener('mouseout',()=>
//{
//    titulo_conversor.innerHTML = '<i class="fas fa-spinner"></i> TConversor'
//})
//
//titulo_conversor.addEventListener('click',()=>
//{
//    conversor.classList.remove('active')
//    titulo_conversor.innerHTML = '<i class="fas fa-spinner"></i> TConversor'
//})

//  Impostos

btn_impostos.addEventListener('click',()=>
{
    if(impostos.classList != 'active')
    {
        impostos.classList.add('active')
        Active = impostos
    }
})

//titulo_impostos.addEventListener('mouseover',()=>
//{
//    titulo_impostos.innerHTML = '<i class="fas fa-arrow-left"></i> TImpostos'
//})
//
//titulo_impostos.addEventListener('mouseout',()=>
//{
//    titulo_impostos.innerHTML = '<i class="fas fa-euro-sign"></i> TImpostos'
//})
//
//titulo_impostos.addEventListener('click',()=>
//{
//    impostos.classList.remove('active')
//    titulo_impostos.innerHTML = '<i class="fas fa-euro-sign"></i> TImpostos'
//})

//  Noticia

btn_noticia.addEventListener('click',async ()=>
{
    if(noticia.classList != 'active')
    {
        noticia.classList.add('active')
        Active = noticia
        let dados = await Pegar_Noticias()
        Preencher_SelectTemas(dados)
    }
})

//titulo_noticia.addEventListener('mouseover',()=>
//{
//    titulo_noticia.innerHTML = '<i class="fas fa-arrow-left"></i> TNotícias'
//})
//
//titulo_noticia.addEventListener('mouseout',()=>
//{
//    titulo_noticia.innerHTML = '<i class="fas fa-euro-sign"></i> TNotícias'
//})
//
//titulo_noticia.addEventListener('click',()=>
//{
//    noticia.classList.remove('active')
//    titulo_noticia.innerHTML = '<i class="fas fa-euro-sign"></i> TNotícias'
//})

//  Configurações

btn_configs.addEventListener('click',()=>
{
    configuracoes.classList.add('active')
})

btn_back_configs.addEventListener('click',()=>
{
    configuracoes.classList.remove('active')
})

btn_back_page.addEventListener('click',()=>
{
    Active.classList.remove('active');
})

btn_next_page.addEventListener('click',()=>
{
    Active.classList.add('active')
})

// Notificação

function Notificacao(msg)
{
    let inicio = setTimeout(()=>
    {
        notificacao_context.innerHTML = msg;
        notificacao.classList.add('active')

        let fim = setTimeout(()=>
        {
            notificacao.classList.remove('active')
            if(noticia.classList != 'active')
            {
                inicio = clearTimeout(inicio)
                fim = clearTimeout(fim)
            }
        },12000)
    },1000)
}
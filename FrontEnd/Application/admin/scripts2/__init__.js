
btn_open_menu.addEventListener('click',()=>
{
    MenuBar.classList.add('active')
})

btn_exit_menu.addEventListener('click',()=>
{
    MenuBar.classList.remove('active')
})

// Events scroll applications of Application-Master

btns_app_invoc[0].addEventListener('click',()=>
{
    if(Cambio_App.classList != 'active')
    {
        btns_app_invoc[1].classList.remove('active')
        btns_app_invoc[2].classList.remove('active')
        btns_app_invoc[3].classList.remove('active')
        btns_app_invoc[4].classList.remove('active')
        Conversor_App.classList.remove('active')
        Noticias_App.classList.remove('active')
        Consultas_App.classList.remove('active')
        More_Apps.classList.remove('active')
        DashBoard.classList.remove('active')
        //
        btns_app_invoc[0].classList.add('active')
        Cambio_App.classList.add('active')
        HeaderTitle.innerHTML = btns_app_invoc[0].value
        Pegar_Cambios(Cambio_Select.value)
    } else {
        DashBoard.classList.add('active')
        HeaderTitle.innerHTML = 'Inicio'
        btns_app_invoc[0].classList.remove('active')
        Cambio_App.classList.remove('active')
    }

})

btns_app_invoc[1].addEventListener('click',async ()=>
{
    if(Conversor_App.classList != 'active')
    {
        btns_app_invoc[0].classList.remove('active')
        btns_app_invoc[2].classList.remove('active')
        btns_app_invoc[3].classList.remove('active')
        btns_app_invoc[4].classList.remove('active')
        Cambio_App.classList.remove('active')
        Noticias_App.classList.remove('active')
        Consultas_App.classList.remove('active')
        More_Apps.classList.remove('active')
        DashBoard.classList.remove('active')
        //

        btns_app_invoc[1].classList.add('active')
        Conversor_App.classList.add('active')
        HeaderTitle.innerHTML = btns_app_invoc[1].value

        let value = conversor_select.value;
        value = await Pegar_Cambios(value)
        Preencher_Select2(value)
    } else {
        DashBoard.classList.add('active')
        HeaderTitle.innerHTML = 'Inicio'
        btns_app_invoc[1].classList.remove('active')
        Conversor_App.classList.remove('active')
    }
})

btns_app_invoc[2].addEventListener('click',async ()=>
{
    if(Noticias_App.classList != 'active')
    {
        btns_app_invoc[0].classList.remove('active')
        btns_app_invoc[1].classList.remove('active')
        btns_app_invoc[3].classList.remove('active')
        btns_app_invoc[4].classList.remove('active')
        Cambio_App.classList.remove('active')
        Conversor_App.classList.remove('active')
        Consultas_App.classList.remove('active')
        More_Apps.classList.remove('active')
        DashBoard.classList.remove('active')
        //
        btns_app_invoc[2].classList.add('active')
        Noticias_App.classList.add('active')
        HeaderTitle.innerHTML = btns_app_invoc[2].value
        let dados = Preencher_SelectTemas(await Pegar_Noticias())
        Inserir_Artigo(dados)
    } else {
        DashBoard.classList.add('active')
        HeaderTitle.innerHTML = 'Inicio'
        btns_app_invoc[2].classList.remove('active')
        Noticias_App.classList.remove('active')
    }
})

btns_app_invoc[3].addEventListener('click',()=>
{
    if(Consultas_App.classList != 'active')
    {
        btns_app_invoc[0].classList.remove('active')
        btns_app_invoc[2].classList.remove('active')
        btns_app_invoc[1].classList.remove('active')
        btns_app_invoc[4].classList.remove('active')
        Cambio_App.classList.remove('active')
        Noticias_App.classList.remove('active')
        Conversor_App.classList.remove('active')
        More_Apps.classList.remove('active')
        DashBoard.classList.remove('active')
        //
        btns_app_invoc[3].classList.add('active')
        Consultas_App.classList.add('active')
        HeaderTitle.innerHTML = btns_app_invoc[3].value
    } else {
        DashBoard.classList.add('active')
        HeaderTitle.innerHTML = 'Inicio'
        btns_app_invoc[3].classList.remove('active')
        Consultas_App.classList.remove('active')
    }
})

btns_app_invoc[4].addEventListener('click',()=>
{
    if(More_Apps.classList != 'active')
    {
        btns_app_invoc[0].classList.remove('active')
        btns_app_invoc[2].classList.remove('active')
        btns_app_invoc[3].classList.remove('active')
        btns_app_invoc[1].classList.remove('active')
        Cambio_App.classList.remove('active')
        Noticias_App.classList.remove('active')
        Consultas_App.classList.remove('active')
        Conversor_App.classList.remove('active')
        DashBoard.classList.remove('active')
        //
        btns_app_invoc[4].classList.add('active')
        More_Apps.classList.add('active')
        HeaderTitle.innerHTML = btns_app_invoc[4].value
    } else {
        DashBoard.classList.add('active')
        HeaderTitle.innerHTML = 'Inicio'
        btns_app_invoc[4].classList.remove('active')
        More_Apps.classList.remove('active')
    }
})
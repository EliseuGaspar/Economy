function Preencher_Select2(data)
{
    select_moeda2.innerHTML = '';

    for (let index = 1; index < data['Tamanho']; index++) {
        select_moeda2.innerHTML += `<option value="${data[`${index}`].Moeda}">${data[`${index}`].Moeda}</option>`
    }
}

select_moeda1.addEventListener('change',async ()=>
{
    let value = select_moeda1.value;
    value = await Pegar_Cambios(value)
    Preencher_Select2(value)
})

btn_converter.addEventListener('click',()=>
{
    if(campo_conversor.value == '')
    {
        Notificacao("É necessário um valor para efectuar a conversão!")
    } else {
        Converter_Valor(
            select_moeda1.value,
            campo_conversor.value,
            select_moeda2.value
        )
    }
})

campo_resultado_conversor.addEventListener('click',()=>
{
    campo_resultado_conversor.innerHTML = 'Sem nada ainda'
})
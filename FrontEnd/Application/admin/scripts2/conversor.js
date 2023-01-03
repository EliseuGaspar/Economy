function Preencher_Select2(data)
{
    conversor_select_moeda.innerHTML = '';

    for (let index = 0; index < data['Tamanho']; index++) {
        conversor_select_moeda.innerHTML += `<option value="${data[`${index}`].Moeda}">${data[`${index}`].Moeda}</option>`
    }
}

conversor_select.addEventListener('change',async ()=>
{
    let value = conversor_select.value;
    value = await Pegar_Cambios(value)
    Preencher_Select2(value)
})

btn_conversor.addEventListener('click',()=>
{
    if(valor_conversao.value == '')
    {
        alert('Insira um valor!')
    } else {
        Converter_Valor(
            conversor_select.value,
            valor_conversao.value,
            conversor_select_moeda.value
        )
    }
})

campo_conversao_resultado.addEventListener('click',()=>
{
    campo_conversao_resultado.innerHTML = '00.00'
})

btn_copy_conversor.addEventListener('click',()=>
{
    Copy(campo_conversao_resultado)
})
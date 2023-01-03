// Eventos com o câmbio

select_cambio.addEventListener('change',()=>
{
    let value = select_cambio.value;
    campo_banco_cambio.innerHTML = value
    Pegar_Cambios(value)
})
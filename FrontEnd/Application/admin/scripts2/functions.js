

function Copy(element){
    navigator.clipboard.writeText(element.value).then(()=>{})
}


async function LinkTest(link)
{

        let promessa = await fetch(link)

        alert(promessa.status)
        
        return 200
}
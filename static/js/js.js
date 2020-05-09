const sleep = ms => new Promise(res => setTimeout(res, ms));
async function checkcalc(){
    let isRunning = null
    console.log('befo running',isRunning)
    do{
        await sleep(500)
        fetch("/calcStatus", {
            method: 'get'
        })
        .then(response => response.json())
        .then(data => {
            console.log('checking', data);
            isRunning = data.status
            document.getElementById("resulttext").innerHTML = data.output;

            document.getElementById("combinations").innerHTML = data.combinations;
            document.getElementById("correctValuescount").innerHTML = data.correctValuesCount;
            console.log(document.getElementById("resulttext").scrollTop, document.getElementById("resulttext").scrollHeight-111)
            document.getElementById("resulttext").scrollTop = document.getElementById("resulttext").scrollHeight-111;
            return data.status;})
        }while(isRunning ==null || isRunning);
    console.log('calc done');
}
function runcalc() {
    var url = "/runCalc"
    const data = new URLSearchParams();
    for (const pair of new FormData(document.getElementById("runCalcForm"))) {
        data.append(pair[0], pair[1]);
    }
    promise = fetch(url, {
        method: 'post',
        body: data,
    })
    checkcalc()
    promise.then(response => {
        console.log('calc response',response);
        return response.json();})
    .then(response => {
    return response;})
    .then(data =>
    {
        var r = data;
        document.getElementById("resulttext").innerHTML = r.result;
        console.log('calc response 2nd',r);
        console.log('calc response 2nd',r.result);
        return;
    });

}
function updateeq(event) {
    var formElements = Array.from(document.getElementById("runCalcForm").elements);
    formElements.forEach(val=> {
        input = document.getElementById(val.id+"eq");
        if(input !=null)
            input.innerHTML = val.value;
        if(val.id.includes("Approximate")){
                    input.innerHTML = "("+val.id[0]+") ~"+val.value;
        }
        if(val.id.includes("xExchangeRate")){
             document.getElementById(val.id+"eqAprox").innerHTML = "("+val.id[0]+") ~"+val.value;
             document.getElementById(val.id+"eq1").innerHTML = val.value;
             document.getElementById(val.id+"eq2").innerHTML = val.value;
             }
    });
}
window.addEventListener('load', function() {
    updateeq(event);
    console.log('All assets are loaded')
document.querySelectorAll('#runCalcForm input').forEach(x =>
    x.addEventListener('change', (event) => {
    updateeq(event);
}));
})
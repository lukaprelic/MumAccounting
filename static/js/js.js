const sleep = ms => new Promise(res => setTimeout(res, ms));
let correctValues = []
function drawCorrectValues(){
    document.getElementById("correctValues").innerHTML=''
    for(value of correctValues){
        var row = document.createElement('div');
        row.className = 'row'
        var x = document.createElement('div');
                x.className = 'cell'
        var y = document.createElement('div');
                y.className = 'cell'
        var z = document.createElement('div');
                z.className = 'cell'
        var diff = document.createElement('div');
                diff.className = 'cell'
        x.innerHTML = 'x='+value['x'];
        y.innerHTML = 'y='+value['y'];
        z.innerHTML = 'z='+value['z'];
        diff.innerHTML = 'diff='+value['diff'];
        row.appendChild(x)
        row.appendChild(y)
        row.appendChild(z)
        row.appendChild(diff)
        document.getElementById("correctValues").appendChild(row)
    }
}
async function checkcalc(){
    let isRunning = null
    do{
        await sleep(500)
        fetch("/calcStatus", {
            method: 'get'
        })
        .then(response => response.json())
        .then(data => {
            isRunning = data.status
            document.getElementById("resulttext").innerHTML = data.output;
            document.getElementById("combinations").innerHTML = data.combinations;
            correctValues = data.correctValues;
            document.getElementById("correctValuescount").innerHTML = correctValues.length;
            document.getElementById("resulttext").scrollTop = document.getElementById("resulttext").scrollHeight;
                drawCorrectValues();
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
        return response.json();})
    .then(response => {
    return response;})
    .then(data =>
    {
        var r = data;
        document.getElementById("resulttext").innerHTML = r.result;
        return;
    });

}
function updateeq(event) {
    var formElements = Array.from(document.getElementById("runCalcForm").elements);
    formElements.forEach(val=> {
        input = document.getElementById(val.id+"eq");
        if(input !=null)
            input.innerHTML = val.value;
        if(val.id.includes("krouns"))
            input.innerHTML = "(Kc) "+val.value;
        if(val.id.includes("Approximate")){
                    input.innerHTML = "("+val.id[0]+") ~"+val.value;
        }
        if(val.id.includes("ExchangeRate")){
             //document.getElementById(val.id+"eqAprox").innerHTML = "("+val.id[0]+") ~"+val.value;
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
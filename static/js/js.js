function runcalc() {
    var url = "/runCalc"
    const data = new URLSearchParams();
    for (const pair of new FormData(document.getElementById("runCalcForm"))) {
        data.append(pair[0], pair[1]);
    }
    fetch(url, {
        method: 'post',
        body: data,
    })
    .then(response => {
        console.log(response);
        return response.json();})
    .then(response => {
    var element = document.createElement("div");
    element.setAttribute("id", "resulttext");
    document.getElementById("result").appendChild(element);
    return response;})
    .then(data =>
    {
        var r = data;
        document.getElementById("resulttext").innerHTML = r.result;
        console.log(r);
        console.log(r.result);
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
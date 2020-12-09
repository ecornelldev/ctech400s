function getTotal() {
    total = 0;
    totalThrough = document.getElementById("input").value;
    for (i=0; i < totalThrough; i++) {
      total += i;
    }  
    outputHTML = "The total is <b>" + total + "</b>";
    document.getElementById("output").innerHTML = outputHTML;
}

let myelement=document.createElement("div")
myelement.className="product"
console.log(myelement)
 seq=document.getElementById("res").textContent


for(let i=0;i<=seq.length;i++){
    console.log(seq[i])
    if (seq[i]=='A'){
        let myelement=document.createElement("div")
             myelement.className="product1"
             document.getElementById("result").appendChild(myelement)
    }    
    if (seq[i]=='T'){
        let myelement=document.createElement("div")
             myelement.className="product2"
             document.getElementById("result").appendChild(myelement)
    }    
    if (seq[i]=='C'){
        let myelement=document.createElement("div")
             myelement.className="product3"
             document.getElementById("result").appendChild(myelement)
    }    
    if (seq[i]=='G'){
        let myelement=document.createElement("div")
             myelement.className="product4"
             document.getElementById("result").appendChild(myelement)
    }    
}



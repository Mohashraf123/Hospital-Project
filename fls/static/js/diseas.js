let upload=document.getElementById('upload');
let output=document.getElementById('output');

upload.addEventListener('change',()=>{
    let fr=new FileReader();
    fr.readAsText(upload.files[0]);

    fr.onload=function(){
        output.innerHTML=fr.result;
    };
});


let upload2=document.getElementById('upload2');
let output2=document.getElementById('output2');

upload2.addEventListener('change',()=>{
    let fs=new FileReader();
    fs.readAsText(upload2.files[0]);

    fs.onload=function(){
        output2.innerHTML=fs.result;
    };
});

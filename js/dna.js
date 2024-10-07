let upload=document.getElementById('upload');
let output=document.getElementById('output');

upload.addEventListener('change',()=>{
    let fr=new FileReader();
    fr.readAsText(upload.files[0]);

    fr.onload=function(){
        output.innerHTML=fr.result;
    };
});

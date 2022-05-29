// function copy(){
//     var copyText = document.querySelector("#item");
//     copyText.select();
//     document.execCommand("copy");
// }

mylink=(element)=>{
    document.getElementById(element).select();
    document.execCommand("copy");
}
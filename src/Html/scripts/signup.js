window.addEventListener("load", init);
function init(){


const jumpinbutton = document.getElementById("jumpin");
console.log(jumpinbutton);
jumpinbutton.addEventListener("click", time);



function time() {
    console.log("time");
    timeout = setTimeout(redirect, 4750);

}

function redirect() {
    window.location.replace("http://example.com");
}
}
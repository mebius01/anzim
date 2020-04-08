
hljs.initHighlightingOnLoad();
hljs.initLineNumbersOnLoad();

var scrollA = document.getElementById('scrollA');
var scrollB = document.getElementById('scrollB');
var heightDoc;
window.addEventListener('scroll', function() {
    heightDoc = document.documentElement.scrollHeight - document.documentElement.clientHeight;
    if (document.documentElement.scrollTop > 30) {
        scrollA.style.display = "block";
        scrollB.style.display = "block";
    } else {
        scrollA.style.display = "none";
        scrollB.style.display = "none";
    }
    if (document.documentElement.scrollTop > heightDoc - 30) {
        scrollB.style.display = "none";
    }
    // console.log(document.documentElement.scrollHeight);
    // console.log(document.documentElement.clientHeight);
    // console.log(document.documentElement.scrollTop);
});
function topFunction() {
    document.body.scrollTop = 0;
    document.documentElement.scrollTop = 0;
}
function downFunction() {
    document.body.scrollTop = heightDoc;
    document.documentElement.scrollTop = heightDoc;
}

function leftToggleOn() {
    var body = document.getElementById('leftToggleOn');
    console.log("toggleOn");
    body.classList.toggle("aside-left--toggle-on");
    // body.classList.add("aside-left--toggle-off");
}
function rightToggleOn() {
    var body = document.getElementById('rightToggleOn');
    console.log("toggleOn");
    body.classList.toggle("aside-right--toggle-on");
    // body.classList.add("aside-right--toggle-off");
}



// http://shpargalkablog.ru/2014/12/tabletree.html
// https://codepen.io/anikey99/pen/GJLdrZ
function toggleUlOne() {
    var ulone = document.getElementById("showList");
    console.log("showList");
    ulone.classList.toggle('aside__list--toggle');
}
function toggleUlTwo() {
    var ulone = document.getElementById("showListTwo");
    console.log("showList");
    ulone.classList.toggle('aside__list--toggle');
}

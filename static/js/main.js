
hljs.initHighlightingOnLoad();
hljs.initLineNumbersOnLoad();

// top down and bottom up
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
});
function topFunction() {
    document.body.scrollTop = 0;
    document.documentElement.scrollTop = 0;
}
function downFunction() {
    document.body.scrollTop = heightDoc;
    document.documentElement.scrollTop = heightDoc;
}


// hide article list and tag list
function leftToggleOn() {
    var body = document.getElementById('leftToggleOn');
    console.log("toggleOn");
    body.classList.toggle("aside-left--toggle-on");
}
function rightToggleOn() {
    var body = document.getElementById('rightToggleOn');
    console.log("toggleOn");
    body.classList.toggle("aside-right--toggle-on");
}


var scrollA = document.getElementById('scrollA');
var scrollB = document.getElementById('scrollB');
var heightDoc = document.documentElement.scrollHeight - document.documentElement.clientHeight;

window.addEventListener('scroll', function() {
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
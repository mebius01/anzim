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
console.log();

function treeList() {
    var toggler = document.getElementsByClassName("plus");
    var i;
    function tic() {
        this.parentElement.querySelector(".list__nested").classList.toggle("list--active");
        // this.classList.toggle("caret-down");
    }
    for (i = 0; i < toggler.length; i++) {
        toggler[i].addEventListener("click", tic);
    }
}
function RootTreeList() {
    var tog = document.getElementsByClassName("rootUl");
    var i;
    for (i = 0; i < toggler.length; i++) {
        tog[i].addEventListener("click", treeList());
    }
}
treeList();
// function funT() {
//     console.log("TEST AddLisener");
// }
// var br = document.querySelector('.breadcrumbs__link--activ');
// br.addEventListener("click", funT());


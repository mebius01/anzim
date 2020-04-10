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
function c(x) {
    console.log(x);
}
function tic() {
    this.parentElement.querySelector(".list__nested").classList.toggle("list--active");
    // this.classList.toggle("caret-down");
    c(this.parentElement.querySelector(".list__nested"))

}
function treeList() {
    var toggler = document.getElementsByClassName("plus");
    var i;
    for (i = 0; i < toggler.length; i++) {
        toggler[i].addEventListener("click", tic);
    }
}
function RootTreeList() {
    var tog = document.getElementsByClassName("pluss");
    var i;
    for (i = 0; i < tog.length; i++) {
        tog[i].addEventListener("click", tic);
    }
}
// treeList();
// RootTreeList();

function triangle() {
    var s = "#######"
    // while (s.length >= 1) {
        
    // }
    c(s[s.length - 1:])
}
triangle()

function cons(x){
    console.log(x);
}

// https://eloquent-javascript.karmazzin.ru/chapter2#treugolnik-v-cikle
function triangle() {
    var s = "1234567";
    var ls = 0;
    while (s.length >= ls) {
        cons(s.slice(0, ls));
        ls = ls + 1;
    }
}
triangle();

// https://eloquent-javascript.karmazzin.ru/chapter2#fizzbuzz
function FizzBuzz(x) {
    var one = 1;
    while (one <= x) {
        if (one%3 == 0 && one%5 == 0) {
            cons(String(one) + ' = FizzBuzz - делится на 3 и на 5');
        } else {
            if (one%5 == 0 && one%3 != 0) {
                cons(String(one) + ' = Buzz - делется на 5 но не три');
            } else {
                if (one%3 == 0) {
                    cons(String(one) + ' = Fizz - делится на 3');
                }
            }
        }   
        one+=1;
    } 
}
FizzBuzz(17);

// https://eloquent-javascript.karmazzin.ru/chapter2#shakhmatnaya-doska
function chessBoard(x, y) {
    var lat = "#";
    var dot = "+";
    var rez = [];
    var zero = 0;
    while (zero <= 8) {
        rez.push(lat,dot);
        zero+=1;
        cons(rez);
    } 
}
chessBoard(12, 12);
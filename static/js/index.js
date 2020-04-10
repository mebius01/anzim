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
function FizzBuzz() {
    var one = 1;
    while (one <= 100) {
        // cons({'one%3':[one,one/3,one%3]});
        if (one%3 == 0) {
            cons('Fizz - делится на 3');
            cons(one);
        } else
        if (one%5 == 0 && one%3 != 0) {
            cons('Buzz - делется на 5 но не три');
            cons(one);
        } else
        if (one%3 == 0 && one%5 == 0) {
            cons('FizzBuzz - делится на 3 и на 5');
            cons(one);
        }
        // else cons(one);
        one+=1;
    } 
}

FizzBuzz()


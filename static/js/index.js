function cons(x){
    console.log(x);
}

// https://eloquent-javascript.karmazzin.ru/chapter2#treugolnik-v-cikle
function triangle() {
    var s = "12345678";
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
function chessBoard(x) {
    var lat = "#";
    var plus = " ";
    var inter_result = "";
    var final_result ="";
    var zero = 1;

    // Функция переворачивает строку
    String.prototype.reverse = function () {
        return this.split('').reverse().join('');
    };

    while (zero <= x) {
        var k;
        if (k === undefined) {
            k = lat;
        } else {
            if (k === lat) {
                k = plus;
            } else {
                if (k === plus) {
                    k = lat;
                }
            }
        }
        inter_result=inter_result+k;
        zero+=1;
    }
    final_result=inter_result+"\r\n"+inter_result.reverse()+"\r\n";

    cons(final_result.repeat(x/2));
}
chessBoard(8);

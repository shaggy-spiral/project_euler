// Project euler problem 12

var number = 0;
var increment = 0;
var divisors = 0;
var computing = true;
var i = 1;
var init = Date.now();

while(computing == true) { 
    number = i + increment;
    increment += i;
    divisors = 1;
    for(var j = 1; j < number/2; j++) {
        if(number % j == 0) {
            divisors++;
        }
    }
    if(divisors > 500) {
        computing = false;
    } else {
        computing = true;
    }
    i++;
}
console.log((Date.now() - init)/1000);
console.log(number);
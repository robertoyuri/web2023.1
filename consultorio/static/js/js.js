var a = 101;
let  b = 23;
const d = 2;

var soma = a + b;
var subt = a - b;
var multi = a * b;
var div = soma / d;
var resto = soma % d;

if(resto == 0 && soma > 0){
    console.log("par e positivo");
}else if(resto == 0 && soma < 0) {
    console.log("par e negativo");
}else if(resto == 0 && soma == 0) {
    console.log("par e neutro");
}else if(resto != 0 && soma < 0) {
    console.log("impar e positivo");
}else if(resto != 0 && soma > 0) {
    console.log("impar e negativo");
}else if(resto != 0 && soma == 0) {
    console.log("impar e neutro");
} else{
    console.log("Deu ruim!");
}

console.log(d);

function parouimpar(num){
    return (num%2)==0 ? "par" : "impar";
}

function posNegNeu(num){
    if(num == 0){
        return "neutro";
    }else if(num > 0){
        return "positivo";
    }else if(num < 0){
        return "negativo";
    }else{
        return "Deu Ruim"
    }
}

console.log(parouimpar(soma) + " e " + posNegNeu(soma));




switch (resto==0){
    case 0:
        console.log("par");
    case 1:
        console.log("impar");
    case 2:
        console.log("impar");
    case 3:
        console.log("impar");
}


let y = 0;
let k = 0;

while(y<100){
    k+=y; //Desafio
    y++; //100
}

for (let i = 0; i<100; i++){
    console.log(i);
}
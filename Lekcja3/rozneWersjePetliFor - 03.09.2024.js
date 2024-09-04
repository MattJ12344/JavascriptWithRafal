//Wersja 0 podstawowa

for (let i = 0; i < 5; i++) {
    console.log("i=" + i);
}

console.log('\n');
console.log('========================');
console.log('\n');

//Wersja 1 zmienna

let x = 5;
for (let i = 0; i < x; i++) {
    console.log("i=" + i);
}

console.log('\n');
console.log('========================');
console.log('\n');

//Wersja 2 funkcja 

function masc() {
    return 5;
}

for (let i = 0; i < masc(); i++) {
    console.log("i=" + i);
}

console.log('\n');
console.log('========================');
console.log('\n');

//Wersja 3 class i obiekt

class Ktos {
    cos() {
        return 5;
    }
}

for (let i = 0; i < new Ktos().cos(); i++) {
    console.log("i=" + i);
}

console.log('\n');
console.log('========================');
console.log('\n');

//Wersja 4 static

class Ktos1 {
    static cos1() {
        return 5;
    }
}

for (let i = 0; i < Ktos1.cos1(); i++) {
    console.log("i=" + i);
}

console.log('\n');
console.log('========================');
console.log('\n');

//Wersja 5  wyciąganie obiketu do zmiennej i klasa

class Ktos2 {
    cos2() {
        return 5;
    }
}
let lol = new Ktos2();
for (let i = 0; i < lol.cos2(); i++) {
    console.log("i=" + i);
}

i = 0; 0 < 5; i++=1
cos4()
i=0;

1 < 5; i++=2
cos4()
i=1;

2 < 5; i++=3
cos4()
i=2;

3 < 5; i++=4
cos4()
i=3;

4 < 5; i++=5
cos4()
i=4;

5 < 5; i++=6
cos4();
console.log('\n');
console.log('========================');
console.log('\n');

//Wersja 6 funkcja w zmiennej

let cos4 = function() {
    return 5;
}
for (let i = 0; i < cos4(); i++) {
    console.log("i=" + i);
}
//7 wersja 
let i2 = 0;
while (i2 < 5){
    i++;
    console.log("i2=" + i2);
}

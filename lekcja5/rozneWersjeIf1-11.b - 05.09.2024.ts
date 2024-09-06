// 0. wszystkie słówka z js
// 2.z boolean
// 3. wartosc z funkcji
// 4. z klasy z pola
// 5. z klasy z fukcji
// 6. z klasy fukcji statycznej
// 7. z funckji przypisana do zmiennej
// 8. 3, 4, 5, 6, 7 

//0. array - tablica
// number - numer,
// string - sznur
// loop - pętla
// boolean - wartość logiczna
// if - jeśli
// else - w przeciwnym razie
// else if - w przeciwnym razie
// (do) while - dopóki
// class - klasa
// function - funkcja
// const - stała
// let - pozwalać
// var - zmienna
// switch - zmieniać
// continue - kontynuować
// break - przerwać
// for - dla
// return - zwracać
// try - spróbować
// operators - operatory
// equals - równa się
// console -  konsola
// iteration - iteracja - jedno wykonanie pętli
// integer - liczba całkowita
// constructor - kostruktor
// static - statycznosc


//Wersja 1

if (4 < 10) {
  console.log('Cos 4');
}

//Wersja 2

if (true) {
  console.log('Cos 5');
}

//Wersja 3.a

function lol(): boolean {
    return 4 < 10;
}

if (lol()) {
  console.log('Cos 6');
}

//Wersja 3.b

function lol1(): boolean {
    return true;
}

if (lol1()) {
  console.log('Cos 7');
}

//Wersja 4.a

class Cos{
    constructor(name1: boolean ) {
        console.log("zalogować name=" + name1);
        this.name = name1;
    }
}

let liczadlo: Cos = new Cos(4 < 10);

if (liczadlo.name === true) {
  console.log('Cos 8');
}

// Wersja 4.b

class Cos1{
    constructor(name2: boolean ) {
        this.name = name2;
    }
}

let liczadlo1: Cos1 = new Cos1(true);

if (liczadlo.name === true) {
  console.log('Cos 9');
}

// Wersja 5.a

class Cos3{
    wykonywalZadanie() {
        return 4 < 10;
    }
}

if (new Cos3().wykonywalZadanie()) {
  console.log('Cos 10');
}

// Wersja 5.b

class Cos4{
    wykonywalZadanie1() {
        return true;
    }
}

if (new Cos4().wykonywalZadanie1()) {
  console.log('Cos 11');
}

// Wersja 6.a

class Cos5{
    static wykonywalZadanie2() {
        return 4 < 10;
    }
}

if (Cos5.wykonywalZadanie2() ) {
  console.log('Cos 12');
}

// Wersja 6.b

class Cos6{
    static wykonywalZadanie3() {
        return true;
    }
}

if (Cos6.wykonywalZadanie3() ) {
  console.log('Cos 13');
}

// Wersja 7.a

let lol6 = function() {
    return 4 < 10;
}

if (lol6()) {
  console.log('Cos 14');
}

// Wersja 7.b

let lol7 = function() {
    return true;
}

if (lol7()) {
  console.log('Cos 15');
}

//Wersja 8.a

function mentor(mati1: boolean): boolean {
    return mati1 ;
}

if (mentor(4 < 10)) {
  console.log('Oho1');
}

// //Wersja 8.b

function mimo(mat2: boolean): boolean {
    return mat2;
}

if (mimo(true)) {
  console.log('Oho2');
}

// Wersja 9.a

class Mem{
    olacLiczbe(oho: boolean): boolean {
        return oho;
    }
}

if (new Mem().olacLiczbe(4 < 10)) {
  console.log('Oho3');
}

// // Wersja 9.b

class Mem2{
    moment(oho1: boolean): boolean {
        return oho1;
    }
}

if (new Mem2().moment(true)) {
  console.log('Oho4');
}

// // Wersja 10.a

class Men{
    static olaBoga(oho2: boolean): boolean {
        return oho2;
    }
}

if (Men.olaBoga(4 < 10) ) {
  console.log('Men');
}

// // Wersja 10.b

class Sigma{
    static men(oho3: boolean): boolean {
        return oho3;
    }
}

if (Sigma.men(true) ) {
  console.log('Sigma');
}

// // Wersja 11.a

let alfa = function(sigma1: boolean): boolean {
    return sigma1;
}

if (alfa(4 < 10)) {
  console.log('Alfa');
}

// // Wersja 11.b

let beta = function(sigma2: boolean): boolean {
    return sigma2;
}

if (beta(true)) {
  console.log('Beta');
}


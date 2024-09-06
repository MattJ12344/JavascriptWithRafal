//Wersja 1
let a: number = 4
let b: number = 10
if (a < b) {
  console.log('Cos1');
}

//Wersja 2

function owen(c: number, d: number): boolean {
    return c < d;
}

if (owen(4, 10)) {
  console.log('Uhu');
}

//Wersja 3

class Sin{

    name: number;
    com: number;

    constructor(e: number, f: number)  {
        this.name = e;
        this.com = f;
    }
}

let liczadlo: Sin = new Sin(4, 10);

if (liczadlo.name < liczadlo.com) {
  console.log('mika');
}

// Wersja 4

class Sig{
    wina(g: number, h: number): boolean {
        return g < h;
    }
}

if (new Sig().wina(4, 10)) {
  console.log('Sig');
}

// Wersja 5

class Uni{
    static ramen(j: number, k:number): boolean {
        return j < k;
    }
}

if (Uni.ramen(4, 10) ) {
  console.log('Uni');
}

// Wersja 6

let momka = function(s: number, o: number): boolean {
    return s < o;
}

if (momka(4, 10)) {
  console.log('Momka');
}

//Wersja 7

function meh(r: number): number {
    return r;
}
function meh2(t: number ): number {
    return t;
}

if (meh(4) < meh2(10)) {
  console.log('meh');
}

// Wersja 8 klasa z construktorem i to fukcja ma zwrócić, wartość ma pochodzić z field

class Soo{

    lol: number;
    mol: number;

    constructor(n: number, m: number)  {
        this.lol = n;
        this.mol = m;
    }
    
   cosiek(): boolean {
        return this.lol < this.mol;
    }
}

let soo: Soo = new Soo(4, 10);
let duda: Soo = soo;
let trump: number = 5;
let kamala: number = trump;
let baiden: Soo = new Soo(4, 2)

if (duda.cosiek()) {
  console.log('ulu');
}
// Wersja 9 klasa z constructorem jedno pole, które typu array  

class Soo1{
    
    zbig: number[];

    constructor(gosc: number[])  {
        this.zbig = gosc;
    }

   cosiek2(): boolean {
        console.log("zbig=" + this.zbig[0]);
        console.log("zbig=" + this.zbig[1]);
        return this.zbig[0] < this.zbig[1];
    }
}

let soo1: Soo1 = new Soo1([4, 10]);

if (soo1.cosiek2() === true) {
  console.log('zbig');
}

// Wersja 10 Fuckja ma otryzmać jeden paramtr czyli tablica

class Soo2{
    //this. odnosi się do pól konstruktora danej klasy.
    //this. odnosi się też do fukcji danej klasy (ale nie daje dostępu funkcji z innej klasy)
   cosiek3(gosc1: number[]): boolean {
        return gosc1[0] < gosc1[1];
    }
}

let wiedzmin: Soo2 = new Soo2();

if (wiedzmin.cosiek3([4, 10])) {
  console.log('zbig2');
}

// wersja 11
let i: number = 4;
let l: number = 10
if(i < l){
    console.log('hahaha');
}

// wersja 12 jedna klasa 3 fukncje: 1. będzie zwracać 4 < 10, ale 4 i 10 pochodzą od innych funcji

class LeagueOfLegends{
    
    
    ashe(a: number) {
        return a;
    }
    velkoz(b: number){
        return b;
    }
    
   darius(): boolean {
        console.log("ashe=" + this.ashe(4));
        console.log("velkoz=" + this.velkoz(10));
        return this.ashe(4) < this.velkoz(10);
    }
}

let liga: LeagueOfLegends = new LeagueOfLegends();

if (liga.darius()) {
  console.log('Malazahar');
}

// 1. 177 jest dobrze i się nie zmieni
// 2. komputer ma zawsze racje i zawsze mówi prawdę
// 3. To ja Mateusz Jaszczyński często się mylę i to ja popełniam błędy


// wersja 13 jedna klasa 3 fukncje: 1. będzie zwracać 4 < 10, ale 4 i 10 pochodzą od innych funcji

class LeagueOfLegends1{
     
    anivia(): boolean {
        return this.mf() < this.kaisa(); // nie zmieniam
    }

    mf(): number {
        return 4;
    }

    kaisa(): number{
        return 10;
    }
   
}

let liga1: LeagueOfLegends1 = new LeagueOfLegends1();

if (liga1.anivia()) { // nie zmieniam
  console.log('Morgana');
}

// wersja 14 mf i kaisa

class LeagueOfLegends2{
    kwiat: Postacie = new Postacie();

    anivia(): boolean {
        return this.kwiat.mf1() < this.kwiat.kaisa1(); 
    }
   
}

class Postacie {
    mf1(): number {
        return 4;
    }

    kaisa1(): number{
        return 10;
    }
} 
let liga2: LeagueOfLegends2 = new LeagueOfLegends2();

if (liga2.anivia()) { 
  console.log('Zed');
}
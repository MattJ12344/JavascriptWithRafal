// Wersja 15

class LeagueOfLegends3{

    kwiat1: Postacie2;

    constructor() {
        this.kwiat1 = new Postacie2();
    }

    anivia1(): boolean {
        return this.kwiat1.mf2() < this.kwiat1.kaisa2(); 
    }
   
}

class Postacie2 {

    mf2(): number {
        return 4;
    }

    kaisa2(): number{
        return 10;
    }
} 

let liga3: LeagueOfLegends3 = new LeagueOfLegends3();

if (liga3.anivia1()) { 
  console.log('Zyra');
}

// Wersja 16

class LeagueOfLegends4{

    kwiat2: Postacie3;

    constructor(kwiat3: Postacie3) {
        this.kwiat2 = kwiat3;
    }

    ahri(): boolean {
        return this.kwiat2.jinx() < this.kwiat2.morgana(); 
    }
   
}

class Postacie3 {

    jinx(): number {
        return 4;
    }

    morgana(): number{
        return 10;
    }
} 

let kwiat2: Postacie3 = new Postacie3();
let liga4: LeagueOfLegends4 = new LeagueOfLegends4(kwiat2);

if (liga4.ahri()) { 
  console.log('Nunu');
}

// Wersja 17

class Lol5{

    ahri1(): boolean {
        return Characters.jinx1() <Characters.morgana1(); 
    }
   
}

class Characters {

    static jinx1(): number {
        return 4;
    }

    static morgana1(): number{
        return 10;
    }
} 

let liga5: Lol5 = new Lol5();

if (liga5.ahri1()) { 
  console.log('Trynda');
}
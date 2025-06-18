// 1 WERSJA zmienna
const tablica = [1, 23, 32423, 523];
 console.log(tablica);
 console.log(tablica[2]);
 let x = 2;
 console.log(tablica[x]);
 tablica[x] = x;
 console.log(tablica);


// 2 WERSJA funkcja
 function wartosc(){
   return 3;
 };

 let x2 = wartosc();
 console.log(tablica[wartosc()]);
 tablica[x2] = x2;
 console.log(tablica);
 tablica[wartosc()] = wartosc();
 console.log(tablica);

// 3 WERSJA class i obiekt
 class Wow{
  
   olaBoga() {
     return 1;
   }

 }

 let x3 = new Wow().olaBoga();
 console.log(tablica[new Wow().olaBoga()]);
 tablica[x3] = x3;
 console.log(tablica);
 tablica[new Wow().olaBoga()] = new Wow().olaBoga();
 console.log(tablica);


// 4 WERSJA Static

 class Wow1{
  
   static olaBoga() {
     return 1;
   }
 }

 let x4 = Wow1.olaBoga();
 console.log(tablica[Wow1.olaBoga()]);
 tablica[x4] = x4;
 console.log(tablica);
 tablica[Wow1.olaBoga()] =  Wow1.olaBoga();
 console.log(tablica);

//5 WERSJA wyciąganie obiketu do zmiennej i klasa

 class Wow2{
   olaBoga() {
     return 1;
   }

 }
 const obiekt = new Wow2();
 const x5 = obiekt.olaBoga();
 console.log(tablica[obiekt.olaBoga()]);
 tablica[x5] = x5;
 console.log(tablica);
 tablica[obiekt.olaBoga()] = obiekt.olaBoga();
 console.log(tablica);

//6. WERSJA funkcja w zmiennej

let wersja = function() {
  console.log("wersja=")
  return 3;
};

let wersja2 = function() {
  console.log("wersja2222222=")
  return 3;
};


let x2 = wersja();
console.log(tablica[wersja()]);
tablica[x2] = x2;
console.log(tablica);
tablica[wersja()] = wersja2();
console.log(tablica);











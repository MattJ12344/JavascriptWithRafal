console.log("Witamy w grze kółko i krzyżyk");



let firstPlayer = "X";


const tablica = [
    ['', '' , ''],
    ['', '', ''] , 
    ['', '', '']
    ];
console.log(tablica[0]);
console.log(tablica[1]);
console.log(tablica[2]);

//[1][0], [1][1], [1][2]
function sposobyWygrania(tablica){
    const wygrana = [
        [0, 1, 2 ],
        [3, 4, 5],
        [6, 7, 8],
        
    ];
}


let y = '1';
let x = '1';
tablica[x][y]= 'X';

console.log("\n");

console.log(tablica[0]);
console.log(tablica[1]);
console.log(tablica[2]);

let i = 0;
if(i === x && i === y ) {
    x = '';
    y = '';
} else {
    "Nie można zaznaczyć tego pola";
}

const input = prompt("What's employee name?");

console.log("input=" + input);


// tworze gracza
// x|o|x
// o|x|o
// x|o|o

//1.gracze x lub o, że x zaczyna pierwszy gracz, który ma x
//2.kółka i krzyżyków, nie mogą się na siebie nakładać, nie mają wyznaczonych miejsc
//3.różne wygrane, jak x zacznaczył w pole gracz to potem kółko zazncza jedno pole a potem z nowu x itd.
//4.Ogłoszenie zwycięscy.


// 1.Witamy w grze kolko i krzyzyk
// Wybrano Ci X albo O
// zaczyna gracz z X
//
// [][][]
// [][][]
// [][][]

//2.Gracz X zaznacza pole:
// x =
// 1
//  y =
// 1
//[][][]
//[][X][]
//[][][]

//3.Gracz O zaznacza pole:
//x= 
//0
//y= 
//0
//[O][][]
//[][X][]
//[][][]

//4.Gracz X zaznacza pole;
//x =
//0
//y = 
//2
//[O][][X]
//[][X][]
//[][][]

//5. Gracz O zanzacza pole:
//x = 
//2
//y = 
//0
//[O][][X]
//[][X][]
//[O][][]

//6. Gracz X zaznacza pole:
//x = 
//1
//y = 
//0
//[O][][X]
//[X][X][]
//[O][][]

//7. Gracz O zaznacza pole:
//x = 
//2
//y = 
//2
//[O][][X]
//[X][X][]
//[O][][O]

//8. Gracz X zaznacza pole:
//x = 
//1
//y = 
//2
//[O][][X]
//[X][X][X]
//[O][][O]

//9. WIN=X 
//LOSE=O



//1. Powitanie graccza
//3. Zaczyna gracz z X
//4. Gracz X zaznacza pole
//5. Potem gracz O zaznacz inne pole;
//6. Po zaznaczeniu wyznaczonych pól przechodzi kolej na gracza X  ,itd.
//7. Gracz X lub O wygrał przez zaznaczony wariant wygranej;

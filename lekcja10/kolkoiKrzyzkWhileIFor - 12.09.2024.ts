// const input = prompt("Pobieranie: ");

// console.log("input=" + input);
// 1.
console.log("1.");
console.log("Witamy w grze kółko i krzyżyk");
let firstPlayer: string = "X";
console.log("Wybrano Ci=" + firstPlayer);
console.log("Grę zaczyna=" + firstPlayer);
let secondPlayer: string = "O";

const tablica: string[][] = [
	['', '', ''],
	['', '', ''],
	['', '', '']
];
console.log(tablica[0]);
console.log(tablica[1]);
console.log(tablica[2]);

console.log("\n");
let wygrana = 0;
let tura = 0;
for (let k = 0; k < tablica.length; k++) {
	for (let j = 0; j < tablica.length; j++) {
		if (tablica[k][j] === firstPlayer || tablica[k][j] === secondPlayer) {
			tura++;
		}
	}
}
while (wygrana =) {
	if (tura >= 5) {
		for (let i = 0; i < 8; i++) {

			wygranaX = tablica[cos[i][0][0]][cos[i][0][1]] === firstPlayer &&
				tablica[cos[i][1][0]][cos[i][1][1]] === firstPlayer &&
				tablica[cos[i][2][0]][cos[i][2][1]] === firstPlayer;
			wygranaO = tablica[cos[i][0][0]][cos[i][0][1]] === secondPlayer &&
				tablica[cos[i][1][0]][cos[i][1][1]] === secondPlayer &&
				tablica[cos[i][2][0]][cos[i][2][1]] === secondPlayer;
		
			if (wygranaX === true || wygranaO === true) {
				break;
			}
		
		
		}
	}

}

//While, tablica x, y, sprawdzenie w każdej iteracji czy wygrał gracz
//2.
console.log("2.");
console.log("Gracz" + firstPlayer + "zaznacza pole:")
let x: number = 1;
let y: number = 1;
tablica[x][y] = firstPlayer;

console.log(tablica[0]);
console.log(tablica[1]);
console.log(tablica[2]);

// 3.
console.log("3.")
console.log("Gracz" + secondPlayer + "zaznacza pole:")
x = 0;
y = 0;
tablica[x][y] = secondPlayer;

console.log(tablica[0]);
console.log(tablica[1]);
console.log(tablica[2]);

//4.
console.log("4.");
console.log("Gracz" + firstPlayer + "zaznacza pole:")
x = 0;
y = 2;
tablica[x][y] = firstPlayer;

console.log(tablica[0]);
console.log(tablica[1]);
console.log(tablica[2]);

// 5.
console.log("5.")
console.log("Gracz" + secondPlayer + "zaznacza pole:")
x = 1;
y = 0;
tablica[x][y] = secondPlayer;

console.log(tablica[0]);
console.log(tablica[1]);
console.log(tablica[2]);

//6.
console.log("6.");
console.log("Gracz" + firstPlayer + "zaznacza pole:")
x = 0;
y = 1;
tablica[x][y] = firstPlayer;

console.log(tablica[0]);
console.log(tablica[1]);
console.log(tablica[2]);

// 7.
console.log("7.")
console.log("Gracz" + secondPlayer + "zaznacza pole:")
x = 2;
y = 2;
tablica[x][y] = secondPlayer;

console.log(tablica[0]);
console.log(tablica[1]);
console.log(tablica[2]);

//8.
console.log("8.");
console.log("Gracz" + firstPlayer + "zaznacza pole:")
x = 1;
y = 2;
tablica[x][y] = firstPlayer;

console.log(tablica[0]);
console.log(tablica[1]);
console.log(tablica[2]);

//9.
console.log("9.");
console.log("Gracz" + secondPlayer + "zaznacza pole:")
x = 2;
y = 0;
tablica[x][y] = secondPlayer;

console.log(tablica[0]);
console.log(tablica[1]);
console.log(tablica[2]);



const cos: number[][][] = [
	[[0, 1], [1, 1], [2, 1]],
	[[0, 0], [1, 0], [2, 0]],
	[[0, 2], [1, 2], [2, 2]], // wygrana i = 2;
	[[0, 0], [0, 1], [0, 2]],
	[[1, 0], [1, 1], [1, 2]],
	[[2, 0], [2, 1], [2, 2]],
	[[0, 0], [1, 1], [2, 2]],
	[[0, 2], [1, 1], [2, 0]]
];
let wygranaO: boolean = false;
let wygranaX: boolean = false;
for (let i = 0; i < 8; i++) {

	wygranaX = tablica[cos[i][0][0]][cos[i][0][1]] === firstPlayer &&
		tablica[cos[i][1][0]][cos[i][1][1]] === firstPlayer &&
		tablica[cos[i][2][0]][cos[i][2][1]] === firstPlayer;
	wygranaO = tablica[cos[i][0][0]][cos[i][0][1]] === secondPlayer &&
		tablica[cos[i][1][0]][cos[i][1][1]] === secondPlayer &&
		tablica[cos[i][2][0]][cos[i][2][1]] === secondPlayer;

	if (wygranaX === true || wygranaO === true) {
		break;
	}


}

// 10.
console.log("10.");
if (wygranaX) {
	console.log("WIN=" + firstPlayer);
	console.log("LOSE=" + secondPlayer);
} else if (wygranaO) {
	console.log("WIN=" + secondPlayer);
	console.log("LOSE=" + firstPlayer);
} else {
	console.log("Zacznij odnowa");
}

// tworze gracza
// x|o|x
// o|x|o
// x|o|o

//1.gracze x lub o, że x zaczyna pierwszy gracz, który ma x
//2.kółka i krzyżyków, nie mogą się na siebie nakładać, nie mają wyznaczonych miejsc
//3.różne wygrane, jak x zacznaczył w pole gracz to potem kółko zazncza jedno pole a potem z nowu x itd.
//4.Ogłoszenie zwycięscy.


// 1.Witamy w grze kolko i krzyzyk
// Wybrano Ci X
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


// 1. powitanie gracza
// 2. tworzenie tablicy
// 3. Gracz X zaznacza pole
// 4. Gracz O zaznacza pole
// 5. Gracz X wygrał na różne sposoby
// 6. Konsola pokazuje, że gracz X wygrał, a gracz O przegrał;

// Do zrobienia gracz O wygrał grę i konsola pokazuje kto wygrał
// 
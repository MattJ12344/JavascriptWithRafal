// const input = prompt("Pobieranie: ");

// console.log("input=" + input);
// 1.

// 7. Nowy klocek: gra po dziewięciu ruchach ma się zakończyć, nawet jak nikt nie wygrał;
console.log("Witamy w grze kółko i krzyżyk");
let firstPlayer: string = "X";
console.log("Wybrano Ci=" + firstPlayer);
console.log("Grę zaczyna=" + firstPlayer);
let secondPlayer: string = "O";

const resetTablicy = () => [
	['', '', ''],
	['', '', ''],
	['', '', '']
];

let tablica: string[][] = resetTablicy();
console.log(tablica[0]);
console.log(tablica[1]);
console.log(tablica[2]);

console.log("\n");
let wygranaO: boolean = false;
console.log("wygranaO=" + wygranaO)
let wygranaX: boolean = false;
console.log("wygranaX=" + wygranaX)
debugger;
let numerTury: number = 0;


while (true) {
	wygranaO = false;
	wygranaX = false;
	let numerTury = 0;

	while (wygranaO === false && wygranaX === false && numerTury < 9) {
		console.log("\n");

		console.log(numerTury + ".");

		console.log(tablica[0]);
		console.log(tablica[1]);
		console.log(tablica[2]);

		const koordynatyRuchow: number[][] = [
			[0, 1],
			[1, 1],
			[0, 2],
			[2, 2],
			[0, 0],
			[1, 0],
			[2, 0],
			[2, 1],
			[1]
		];

		let x: number;
		let y: number

		if (numerTury < koordynatyRuchow.length) {
			x = koordynatyRuchow[numerTury][0];
			console.log("x=" + x);
			y = koordynatyRuchow[numerTury][1];
			console.log("y=" + y);
		} else {

			const wolnePola: number[][] = [];
			for (let i = 0; i < 3; i++) {
				for (let j = 0; j < 3; j++) {
					if (tablica[i][j] === '') {
						wolnePola.push([i, j]);
					}
				}
			}

			if (wolnePola.length > 0) {
				const indeks = Math.floor(Math.random() * wolnePola.length);
				x = wolnePola[indeks][0];
				y = wolnePola[indeks][1];
				console.log("Losowe koordynaty: x=" + x + ", y=" + y);
			} else {
				console.error("Błąd: Brak wolnych pól");
				break;
			}
		}



		if (tablica[x][y] !== '') {
			console.error("Błąd: Pola (" + x + "," + y + ") jest zajęte. Wybierz inny ");

			let wolneMiejsce: boolean = false;
			for (let f: number = 0; f < 3; f++) {
				for (let g: number = 0; g < 3; g++) {
					if (tablica[f][g] === '') {
						x = f;
						y = g;
						wolneMiejsce = true;
						console.log("Wstaw nowy znak: (" + x + "," + y + ")")
						break;
					}
				}
				if (wolneMiejsce) break;
			}
		}

		if (numerTury % 2 === 0) {
			tablica[x][y] = secondPlayer;
			console.log("Gracz " + secondPlayer + " zaznacza pole:");
		} else {
			tablica[x][y] = firstPlayer;
			console.log("Gracz " + firstPlayer + " zaznacza pole:");
		}


		numerTury++;

		if (numerTury >= 5) {
			for (let i = 0; i < 8; i++) {
				const cos: number[][][] = [
					[[0, 1], [1, 1], [2, 1]],
					[[0, 0], [1, 0], [2, 0]],
					[[0, 2], [1, 2], [2, 2]],
					[[0, 0], [0, 1], [0, 2]],
					[[1, 0], [1, 1], [1, 2]],
					[[2, 0], [2, 1], [2, 2]],
					[[0, 0], [1, 1], [2, 2]],
					[[0, 2], [1, 1], [2, 0]]
				];

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

	console.log("\n");
	console.log(numerTury + ".");
	console.log(tablica[0]);
	console.log(tablica[1]);
	console.log(tablica[2]);

	// 10.
	if (wygranaX) {
		console.log("WIN=" + firstPlayer);
		console.log("LOSE=" + secondPlayer);
	} else if (wygranaO) {
		console.log("WIN=" + secondPlayer);
		console.log("LOSE=" + firstPlayer);
	} else if (numerTury >= 9) {
		console.log("Remis. Zacznij odnowa");
	}

	console.log("\n Nowa gra \n");
	tablica = resetTablicy();
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








// 6. Nowy klocek: sprawdzić czy nie wkładasz x i y na istniejący lub znak
// 7. Nowy klocek: gra po dziewięciu ruchach ma się zakończyć, nawet jak nikt nie wygrał;
// 8. Te kordynatyruchów co mam, ma się losowow wygenerować:
// a. wsprawdzić czy nie wygeneruje takich samych koordynatów
// 9. Tablica "cos" zawieracaja kombinacje koordyantów, ma zostać wygenerowana (prawie) auto

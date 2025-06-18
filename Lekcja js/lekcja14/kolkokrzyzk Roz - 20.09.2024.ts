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

let plansza: string[][] = resetTablicy();
console.log(plansza[0]);
console.log(plansza[1]);
console.log(plansza[2]);

console.log("\n");
let wygranaO: boolean = false;
console.log("wygranaO=" + wygranaO);
let wygranaX: boolean = false;
console.log("wygranaX=" + wygranaX);
let numerTury: number = 0;
let poprzednieRuchy: number[][] = [];

function generujWzoryWygranej(): number[][][] {
	let wzoryWygranej: number[][][] = [];


	for (let i = 0; i < plansza.length; i++) {
		let wiersz: number[][] = [];
		let kolumna: number[][] = [];

		for (let j = 0; j < plansza.length; j++) {

			wiersz.push([i, j]);
			kolumna.push([j, i]);
		}

		wzoryWygranej.push(wiersz);
		wzoryWygranej.push(kolumna);
	}

	let przekatna1: number[][] = [[0, 0], [1, 1], [2, 2]];
	let przekatna2: number[][] = [[0, 2], [1, 1], [2, 0]];
	wzoryWygranej.push(przekatna1);
	wzoryWygranej.push(przekatna2);

	return wzoryWygranej;
}

const wzoryWygranej = generujWzoryWygranej();

function czyMoznaWykonacRuch(x: number, y: number): boolean {
	return plansza[x][y] === '';
}

function dodajRuch(x: number, y: number, gracz: string) {
	plansza[x][y] = gracz;
}


let iloscGier: number = 0;
while (iloscGier < 5) {
	console.log("\n Nowa gra \n");

	wygranaO = false;
	wygranaX = false;
	numerTury = 0;
	poprzednieRuchy = [];

	while (wygranaO === false && wygranaX === false && numerTury < 9) {
		console.log("\n");

		console.log(numerTury + ".");
		console.log(plansza[0]);
		console.log(plansza[1]);
		console.log(plansza[2]);
		debugger;
		let x: number;
		let y: number;


		let ruch = losujWolnePole();
		x = ruch[0];
		y = ruch[1];

		while (!czyMoznaWykonacRuch(x, y)) {
			console.error("Koordynaty (" + x + "," + y + ") były już użyte. Wybierz inne.");
			ruch = losujWolnePole();
			x = ruch[0];
			y = ruch[1];

		}



	
		if (plansza[x][y] === '') {
			const currentPlayer = numerTury % 2 === 0 ? secondPlayer : firstPlayer;
			dodajRuch(x, y, currentPlayer);
			console.log(`Gracz ${currentPlayer} zaznacz pole: `)
		} else {
			console.error(`Błąd: Pola (${x}, ${y}) jest zajęte. Wybierz inne.`)
		}

		if (numerTury >= 4) {
			for (let i = 0; i < wzoryWygranej.length; i++) {
				wygranaX = plansza[wzoryWygranej[i][0][0]][wzoryWygranej[i][0][1]] === firstPlayer &&
					plansza[wzoryWygranej[i][1][0]][wzoryWygranej[i][1][1]] === firstPlayer &&
					plansza[wzoryWygranej[i][2][0]][wzoryWygranej[i][2][1]] === firstPlayer;
				wygranaO = plansza[wzoryWygranej[i][0][0]][wzoryWygranej[i][0][1]] === secondPlayer &&
					plansza[wzoryWygranej[i][1][0]][wzoryWygranej[i][1][1]] === secondPlayer &&
					plansza[wzoryWygranej[i][2][0]][wzoryWygranej[i][2][1]] === secondPlayer;

				if (wygranaX || wygranaO) {
					break;
				}
			}
		}

		numerTury++;
	}

	console.log("\n");
	console.log(numerTury + ".");
	console.log(plansza[0]);
	console.log(plansza[1]);
	console.log(plansza[2]);

	if (wygranaX) {
		console.log("WIN=" + firstPlayer);
		console.log("LOSE=" + secondPlayer);
	} else if (wygranaO) {
		console.log("WIN=" + secondPlayer);
		console.log("LOSE=" + firstPlayer);
	} else if (numerTury >= 9) {
		console.log("Remis. Zacznij od nowa");
	}

	plansza = resetTablicy();

	iloscGier++;
}

function losujWolnePole(): [number, number] {
	let x: number, y: number;

	do {
		x = Math.floor(Math.random() * plansza.length);
		y = Math.floor(Math.random() * plansza.length);
	} while (plansza[x][y] === '');

	return [x, y];
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


// 3. Może pomyśl o schowaniu funkcji w klasie/klasach
// 4. Przeglądnij wszystkie nazwy zmiennych i funkcji i zastanów się czy nie można je nazwać lepiej
// 5. Cała gra ma być zależna od zmiennej let wymiarGry: number =3; i za pomocą tej zmiennej ma grać cała gra
// (array.length ma dalej być używany w forach)
// github i powiedz Rafałowi
// 6. Kółko i krzyżyk 4x4

// 1. powitanie gracza
// 2. tworzenie tablicy
// 3. Gracz X zaznacza pole
// 4. Gracz O zaznacza pole
// 5. Gracz X wygrał na różne sposoby
// 6. Konsola pokazuje, że gracz X wygrał, a gracz O przegrał;

// Do zrobienia gracz O wygrał grę i konsola pokazuje kto wygrał
//



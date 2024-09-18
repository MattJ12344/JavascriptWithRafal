// const input = prompt("Pobieranie: ");

// console.log("input=" + input);
// 1.

// a. wsprawdzić czy nie wygeneruje takich samych koordynatów
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
console.log("wygranaO=" + wygranaO);
let wygranaX: boolean = false;
console.log("wygranaX=" + wygranaX);
debugger;
let numerTury: number = 0;
let poprzednieRuchy: number[][] = [];


const generujWzoryWygranej = (): number[][][] => {
	let wzoryWygranej: number[][][] = [];


	for (let i = 0; i < 3; i++) {
		let wiersz: number[][] = [[i, 0], [i, 1], [i, 2]];
		wzoryWygranej.push(wiersz);
	}


	for (let i = 0; i < 3; i++) {
		let kolumna: number[][] = [[0, i], [1, i], [2, i]];
		wzoryWygranej.push(kolumna);
	}


	let przekatna1: number[][] = [[0, 0], [1, 1], [2, 2]];
	let przekatna2: number[][] = [[0, 2], [1, 1], [2, 0]];
	wzoryWygranej.push(przekatna1);
	wzoryWygranej.push(przekatna2);

	return wzoryWygranej;
}

const wzoryWygranej = generujWzoryWygranej();

const czyRuchZrobiony = (x: number, y: number): boolean => {
	for (let i = 0; i < poprzednieRuchy.length; i++) {
		if (poprzednieRuchy[i][0] === x && poprzednieRuchy[i][1] === y) {
			return true;
		}
	}
	return false;
}

const dodajRuch = (x: number, y: number) => {
	poprzednieRuchy.push([x, y]);
}

const losujWolnePole = (): [number, number] => {
	let x: number, y: number;
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
	} else {
		console.error("Błąd: Brak wolnych pól");
		return [-1, -1];
	}

	return [x, y];
}

while (true) {
	wygranaO = false;
	wygranaX = false;
	numerTury = 0;
	poprzednieRuchy = [];

	while (wygranaO === false && wygranaX === false && numerTury < 9) {
		console.log("\n");

		console.log(numerTury + ".");
		console.log(tablica[0]);
		console.log(tablica[1]);
		console.log(tablica[2]);

		let x: number;
		let y: number;

		const ruch = losujWolnePole();
		x = ruch[0];
		y = ruch[1];

		if (czyRuchZrobiony(x, y)) {
				console.error("Koordynaty (" + x + "," + y + ") były już użyte. Wybierz inne.");
				continue;
		}

			dodajRuch(x, y);
			console.log("Wybrane koordynaty: x=" + x + ", y=" + y);


		if (tablica[x][y] !== '') {
			console.error("Błąd: Pola (" + x + "," + y + ") jest zajęte. Wybierz inne");
			continue;
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
			for (let i = 0; i < wzoryWygranej.length; i++) {
				wygranaX = tablica[wzoryWygranej[i][0][0]][wzoryWygranej[i][0][1]] === firstPlayer &&
					tablica[wzoryWygranej[i][1][0]][wzoryWygranej[i][1][1]] === firstPlayer &&
					tablica[wzoryWygranej[i][2][0]][wzoryWygranej[i][2][1]] === firstPlayer;
				wygranaO = tablica[wzoryWygranej[i][0][0]][wzoryWygranej[i][0][1]] === secondPlayer &&
					tablica[wzoryWygranej[i][1][0]][wzoryWygranej[i][1][1]] === secondPlayer &&
					tablica[wzoryWygranej[i][2][0]][wzoryWygranej[i][2][1]] === secondPlayer;

				if (wygranaX || wygranaO) {
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

	if (wygranaX) {
		console.log("WIN=" + firstPlayer);
		console.log("LOSE=" + secondPlayer);
	} else if (wygranaO) {
		console.log("WIN=" + secondPlayer);
		console.log("LOSE=" + firstPlayer);
	} else if (numerTury >= 9) {
		console.log("Remis. Zacznij od nowa");
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
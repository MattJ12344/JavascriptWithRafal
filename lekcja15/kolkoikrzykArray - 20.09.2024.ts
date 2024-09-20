class KolkoIKrzyzyk {
	firstPlayer: string;
	secondPlayer: string;
	plansza: string[][];
	wzoryWygranej: number[][][];
	wygranaX: boolean;
	wygranaO: boolean;
	numerTury: number;
	wymiarGry: number;

	constructor(wymiarGry: number) {
		this.firstPlayer = "X";
		this.secondPlayer = "O";
		this.wymiarGry = wymiarGry;
		this.plansza = this.resetTablicy();
		this.wzoryWygranej = this.generujWzoryWygranej();
		this.wygranaX = false;
		this.wygranaO = false;
		this.numerTury = 0;
	}


	resetTablicy(): string[][] {
		let plansza: string[][] = [];
		for (let i = 0; i < this.wymiarGry; i++) {
			plansza.push(Array(this.wymiarGry).fill(''));
		}
		return plansza;
	}

	generujWzoryWygranej(): number[][][] {
		let wzoryWygranej: number[][][] = [];


		for (let i = 0; i < this.wymiarGry; i++) {
			let wiersz: number[][] = [];
			let kolumna: number[][] = [];
			for (let j = 0; j < this.wymiarGry; j++) {
				wiersz.push([i, j]);
				kolumna.push([j, i]);
			}
			wzoryWygranej.push(wiersz);
			wzoryWygranej.push(kolumna);
		}

		let przekatna1: number[][] = [];
		let przekatna2: number[][] = [];
		for (let i = 0; i < this.wymiarGry; i++) {
			przekatna1.push([i, i]);
			przekatna2.push([i, this.wymiarGry - 1 - i]);
		}
		wzoryWygranej.push(przekatna1);
		wzoryWygranej.push(przekatna2);

		return wzoryWygranej;
	}

	czyMoznaWykonacRuch(x: number, y: number): boolean {
		return this.plansza[x][y] === '';
	}


	dodajRuch(x: number, y: number, gracz: string) {
		this.plansza[x][y] = gracz;
	}


	losujWolnePole(): [number, number] {
		let x: number, y: number;
		do {
			x = Math.floor(Math.random() * this.wymiarGry);
			y = Math.floor(Math.random() * this.wymiarGry);
		} while (!this.czyMoznaWykonacRuch(x, y));
		return [x, y];
	}

	sprawdzWygrana() {
		for (let i = 0; i < this.wzoryWygranej.length; i++) {
			this.wygranaX = this.wzoryWygranej[i].every(
				([x, y]) => this.plansza[x][y] === this.firstPlayer
			);
			this.wygranaO = this.wzoryWygranej[i].every(
				([x, y]) => this.plansza[x][y] === this.secondPlayer
			);

			if (this.wygranaX || this.wygranaO) {
				break;
			}
		}
	}
	pokazPlansze() {
		this.plansza.forEach(wiersz => console.log(wiersz));
	}
}


let wymiarGry: number = 3;
let iloscGier: number = 0;

while (iloscGier < 5) {
	console.log("\n Nowa gra \n");

	const gra = new KolkoIKrzyzyk(wymiarGry);

	while (!gra.wygranaO && !gra.wygranaX && gra.numerTury < wymiarGry * wymiarGry) {
		console.log(`\n Tura: ${gra.numerTury + 1}`);
		gra.pokazPlansze();

		let ruch = gra.losujWolnePole();
		let x = ruch[0];
		let y = ruch[1];

		const currentPlayer = gra.numerTury % 2 === 0 ? gra.secondPlayer : gra.firstPlayer;
		gra.dodajRuch(x, y, currentPlayer);
		console.log(`Gracz ${currentPlayer} zaznaczył pole (${x}, ${y})`);

		if (gra.numerTury >= (2 * wymiarGry - 1)) {
			gra.sprawdzWygrana();
		}

		gra.numerTury++;
	}

	console.log("\nKoniec gry.");
	gra.pokazPlansze();

	if (gra.wygranaX) {
		console.log("WIN=" + gra.firstPlayer);
		console.log("LOSE=" + gra.secondPlayer);
	} else if (gra.wygranaO) {
		console.log("WIN=" + gra.secondPlayer);
		console.log("LOSE=" + gra.firstPlayer);
	} else if (gra.numerTury >= wymiarGry * wymiarGry) {
		console.log("Remis. Zacznij od nowa");
	}

	iloscGier++;
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



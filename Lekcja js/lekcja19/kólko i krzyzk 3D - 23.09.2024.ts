// if else
// number, string, boolean, array
// while, for
// contine, break
// console.log
// array 1d, 2d, 3d
// function, class
// request, response, JSON



// 1. Ladniej wyswietlaj tablice w konsoli
// 

class KolkoIKrzyzyk {
	firstPlayer: string;
	secondPlayer: string;
	plansza: string[][][];
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

	resetTablicy(): string[][][] {
		let plansza: string[][][] = [];
		for (let z = 0; z < this.wymiarGry; z++) {

			let poziom: string[][] = [];

			for (let i = 0; i < this.wymiarGry; i++) {
				poziom.push(Array(this.wymiarGry).fill(' '));
			}
			plansza.push(poziom);
		}
		return plansza;
	}

	generujWzoryWygranej(): number[][][] {
		let wzoryWygranej: number[][][] = [];

		for (let z = 0; z < this.wymiarGry; z++) {
			for (let i = 0; i < this.wymiarGry; i++) {
				let wiersz: number[][] = [];
				let kolumna: number[][] = [];
				for (let j = 0; j < this.wymiarGry; j++) {
					wiersz.push([z, i, j]);
					kolumna.push([z, j, i]);
				}
				wzoryWygranej.push(wiersz);
				wzoryWygranej.push(kolumna);
			}
		}

		for (let z = 0; z < this.wymiarGry; z++) {
			let przekatna1: number[][] = [];
			let przekatna2: number[][] = [];
			for (let i = 0; i < this.wymiarGry; i++) {
				przekatna1.push([z, i, i]);
				przekatna2.push([z, i, this.wymiarGry - 1 - i]);
			}
			wzoryWygranej.push(przekatna1);
			wzoryWygranej.push(przekatna2);
		}

		for (let i = 0; i < this.wymiarGry; i++) {
			for (let j = 0; j < this.wymiarGry; j++) {
				let wierszZ: number[][] = [];
				for (let z = 0; z < this.wymiarGry; z++) {
					wierszZ.push([z, i, j]);
				}
				wzoryWygranej.push(wierszZ);
			}
		}

		let przekatna3D_1: number[][] = [];
		let przekatna3D_2: number[][] = [];
		let przekatna3D_3: number[][] = [];
		let przekatna3D_4: number[][] = [];

		for (let i = 0; i < this.wymiarGry; i++) {
			przekatna3D_1.push([i, i, i]);
			przekatna3D_2.push([i, i, this.wymiarGry - 1 - i]);
			przekatna3D_3.push([i, this.wymiarGry - 1 - i, i]);
			przekatna3D_4.push([i, this.wymiarGry - 1 - i, this.wymiarGry - 1 - i]);
		}

		wzoryWygranej.push(przekatna3D_1);
		wzoryWygranej.push(przekatna3D_2);
		wzoryWygranej.push(przekatna3D_3);
		wzoryWygranej.push(przekatna3D_4);

		return wzoryWygranej;
	}

	czyMoznaWykonacRuch(x: number, y: number, z: number): boolean {
		return this.plansza[z][x][y] === ' ';
	}

	dodajRuch(x: number, y: number, z: number, gracz: string) {
		this.plansza[z][x][y] = gracz;
	}

	losujWolnePole(): [number, number, number] {
		let x: number, y: number, z: number;
		do {
			x = Math.floor(Math.random() * this.wymiarGry);
			y = Math.floor(Math.random() * this.wymiarGry);
			z = Math.floor(Math.random() * this.wymiarGry);
		} while (!this.czyMoznaWykonacRuch(x, y, z));
		return [x, y, z];
	}

	sprawdzWygrana() {
		for (let wzor of this.wzoryWygranej) {
			this.wygranaX = wzor.every(([z, x, y]) => this.plansza[z][x][y] === this.firstPlayer);
			this.wygranaO = wzor.every(([z, x, y]) => this.plansza[z][x][y] === this.secondPlayer);

			if (this.wygranaX || this.wygranaO) {
				break;
			}
		}
	}

	pokazPlanszeLadnie() {
		for (let z = 0; z < this.wymiarGry; z++) {
			console.log(`Poziom ${z}:`);
			this.plansza[z].forEach(wiersz => console.log(wiersz));

		}
	}


}


let wymiarGry: number = 4;
let iloscGier: number = 0;
let wygranaX: number = 0;
let wygranaO: number = 0;


while (iloscGier < 5 && wygranaX < 3 && wygranaO < 3) {
	console.log("\nNowa gra\n");

	const gra = new KolkoIKrzyzyk(wymiarGry);

	while (!gra.wygranaO && !gra.wygranaX && gra.numerTury < wymiarGry * wymiarGry * wymiarGry) {
		console.log(`\nTura: ${gra.numerTury + 1}`);
		gra.pokazPlanszeLadnie();


		let ruch = gra.losujWolnePole();
		let x = ruch[0];
		let y = ruch[1];
		let z = ruch[2];


		const currentPlayer = gra.numerTury % 2 === 0 ? gra.secondPlayer : gra.firstPlayer;
		gra.dodajRuch(x, y, z, currentPlayer);
		console.log(`Gracz ${currentPlayer} zaznaczył pole (${x}, ${y}, ${z})`);


		if (gra.numerTury >= (2 * wymiarGry - 1)) {
			gra.sprawdzWygrana();
		}

		gra.numerTury++;
	}

	console.log("\n Koniec Gry.");
	gra.pokazPlanszeLadnie();


	if (gra.wygranaX) {
		console.log("WIN=" + gra.firstPlayer);
		console.log("LOSE=" + gra.secondPlayer);
		wygranaX++;
	} else if (gra.wygranaO) {
		console.log("WIN=" + gra.secondPlayer);
		console.log("LOSE=" + gra.firstPlayer);
		wygranaO++;
	} else if (gra.numerTury >= wymiarGry * wymiarGry * wymiarGry) {
		console.log("Remis. Zacznij od nowa");
	}
	iloscGier++;

	console.log(`Wynik: ${wygranaX}:${wygranaO}`);

}

if (wygranaX === 3) {
	console.log("Gracz X wygrał grę z wynikiem 3:" + wygranaO);
} else if (wygranaO === 3) {
	console.log("Gracz X wygrał grę z wynikiem 3:" + wygranaX)
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
// 6. Kółko i krzyżyk 4x4+






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



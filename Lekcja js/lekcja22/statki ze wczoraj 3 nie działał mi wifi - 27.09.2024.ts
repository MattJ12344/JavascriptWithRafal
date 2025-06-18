class Statki {

	planszaUstawienia: string[][];
	planszaAtakow: string[][];
	wymiarGry: number;
	iloscStatkow: number;
	constructor(wymiarGry: number) {
		this.wymiarGry = wymiarGry;
		this.planszaUstawienia = this.resetTablicy();
		this.planszaAtakow = this.resetTablicy();
		this.iloscStatkow = 3;
	}

	resetTablicy(): string[][] {
		let plansza: string[][] = [];
		for (let i = 0; i < this.wymiarGry; i++) {
			plansza.push(Array(this.wymiarGry).fill(' '));
		}
		return plansza;
	}


	ustawStatek(wspolrzedne: [number, number][]) {
		wspolrzedne.forEach(([x, y]) => {
			if (this.czyMoznaWykonacRuch(x, y)) {
				this.planszaUstawienia[x][y] = 'X';
			} else {
				console.log(`Nie można ustawić statku na pozycji (${x}, ${y}).`);
			}
		});
	}
	czyMoznaWykonacRuch(x: number, y: number): boolean {
		return this.planszaUstawienia[x][y] === ' ';
	}
	oddajStrzal(x: number, y: number, przeciwnik: Statki): string {
		if (przeciwnik.planszaUstawienia[x][y] === 'X') {
			this.planszaAtakow[x][y] = 'Z';
			przeciwnik.planszaUstawienia[x][y] = 'Z';
			console.log(`Trafiony statek na pozycji (${x}, ${y})!`);
			return 'Trafiony';
		} else if (this.planszaAtakow[x][y] === ' ') {
			this.planszaAtakow[x][y] = 'O';
			przeciwnik.planszaUstawienia[x][y] = 'O';
			console.log(`Pudło na pozycji (${x}, ${y}).`);
			return 'Pudło';
		} else {
			console.log(`Pole (${x}, ${y}) było już strzelane.`);
			return 'Ponowny strzał';
		}
	}
	sprawdzZatopienieStatkow(przeciwnik: Statki): boolean {
		let czyKoniec = true;
		for (let i = 0; i < this.wymiarGry; i++) {
			for (let j = 0; j < this.wymiarGry; j++) {
				if (przeciwnik.planszaUstawienia[i][j] === 'X') {
					czyKoniec = false;
				}
			}
		}
		return czyKoniec;
	}
	pokazPlanszeUstawienia() {
		console.log("Plansza Ustawień:");
		this.planszaUstawienia.forEach(wiersz => console.log(wiersz));
	}

	pokazPlanszeAtakow() {
		console.log("Plansza Ataków:");
		this.planszaAtakow.forEach(wiersz => console.log(wiersz));
	}

}

const wymiarGry = 3;
const gracz1 = new Statki(wymiarGry);
const gracz2 = new Statki(wymiarGry);

interface Punkt {
	x: number;
	y: number;
}

console.log("Gracz 1 ustawia statki.");
gracz1.ustawStatek([[0, 0], [0, 1], [0, 2]]);
gracz1.pokazPlanszeUstawienia();


console.log("Gracz 2 ustawia statki.");
gracz2.ustawStatek([[2, 0], [2, 1], [2, 2]]);
gracz2.pokazPlanszeUstawienia();


let ruchyGracza1 = [
	[2, 0],
	[0, 0],
];

let ruchyGracza2 = [
	[1, 1],
	[0, 2],
];


console.log("Gracz 1 atakuje:");
ruchyGracza1.forEach(([x, y]) => {
	gracz1.oddajStrzal(x, y, gracz2);
	gracz1.pokazPlanszeAtakow();
	if (gracz1.sprawdzZatopienieStatkow(gracz2)) {
		console.log("Gracz 1 wygrał! Zatopiono wszystkie statki Gracza 2.");
	}
});

console.log("Gracz 2 atakuje:");
ruchyGracza2.forEach(([x, y]) => {
	gracz2.oddajStrzal(x, y, gracz1);
	gracz2.pokazPlanszeAtakow();
	if (gracz2.sprawdzZatopienieStatkow(gracz1)) {
		console.log("Gracz 2 wygrał! Zatopiono wszystkie statki Gracza 1.");
	}
});
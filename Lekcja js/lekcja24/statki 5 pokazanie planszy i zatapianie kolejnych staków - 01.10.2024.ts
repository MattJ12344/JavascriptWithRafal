// ### ZADANIE OD RAFAŁA
// ZROUMIEĆ W PEŁNI gracz1/gracz2/aktualnyGracz i metody, które można wywołać na nich
// zdebuguj dokładnie okolice lini "this.aktualnyGracz.pokazPlanszeAtaku();"

// jeśli gracz trafi statek to wtedy gracz, który trafił może jeszce raz strzelić [trafiony zatopiny] (if), zmienić gracza, jeśli nie trafił (else)
// posprawdzaj za pomocą ctrl+spacja co możesz użyć np. this.aktualnyGracz.<ctrl+spacja>

// #### UMIESZCZANIE STATKÓW - ZROBIĆ NA SAMYM KOŃCU
// - Potem dodam rozszerzę tablice o 4x4 i dodam jednego 4, dwie 3, trzy 2 i cztery 1
// - jeśli mi to wyjdzie to wtedy, robię 10x10 tablice w statkach



// #### WYGRYWANIE - ZROBIĆ NA SAMYM KOŃCU
// - może zrobię wygraną jak w kółko i krzyżyk, że dopiero po 3 zwycięstwach jest


// MVP - Most Valuable Player
// MVP - Minimal Value Product

class Gracz {
	plansza: string[][];
	planszaAtaku: string[][];
	statki: number[];
	numerTury: number;
	zajetePola: [number, number][];
	nazwa: string;

	constructor(nazwa: string, statki: number[]) {
		this.plansza = this.utworzPustaPlansze(3);
		this.planszaAtaku = this.utworzPustaPlansze(3);
		this.statki = statki;
		this.numerTury = 0;
		this.zajetePola = [];
		this.nazwa = nazwa;

	}
	utworzPustaPlansze(rozmiar: number): string[][] {
		let plansza: string[][] = [];
		for (let i = 0; i < rozmiar; i++) {
			plansza.push(Array(rozmiar).fill(' '));
		}
		return plansza;
	}

	czyMoznaRozmiescicStatek(x: number, y: number, rozmiar: number, orientacja: string): boolean {

		if (orientacja === 'poziomo' && y + rozmiar > 3) return false;
		if (orientacja === 'pionowo' && x + rozmiar > 3) return false;


		for (let i = 0; i < rozmiar; i++) {
			let poleX = orientacja === 'pionowo' ? x + i : x;
			let poleY = orientacja === 'poziomo' ? y + i : y;

			if (this.plansza[poleX][poleY] !== ' ') return false;
			if (!this.czyPoleJestDostepneZOdstepem(poleX, poleY)) return false;
		}

		return true;
	}

	czyPoleJestDostepneZOdstepem(x: number, y: number): boolean {
		const kierunki: number[] = [-1, 0, 1];

		for (let sx of kierunki) {
			for (let sy of kierunki) {
				let zx: number = x + sx;
				let zy: number = y + sy;
				if (zx >= 0 && zx < 3 && zy >= 0 && zy < 3) {
					if (this.plansza[zx][zy] !== ' ') return false;
				}
			}
		}
		return true;
	}

	rozmiescStatek(rozmiar: number, x: number, y: number, orientacja: string): void {
		if (this.czyMoznaRozmiescicStatek(x, y, rozmiar, orientacja)) {
			for (let i = 0; i < rozmiar; i++) {
				let poleX = orientacja === 'pionowo' ? x + i : x;
				let poleY = orientacja === 'poziomo' ? y + i : y;
				this.plansza[poleX][poleY] = 'X';
				this.zajetePola.push([poleX, poleY]);
			}
		} else {
			console.log("Nie można umieścić statku w tej pozycji.");
		}
	}


	pokazPlansze(): void {
		console.log(`\n ${this.nazwa} - Plansza:`);
		this.plansza.forEach(wiersz => console.log(wiersz.join(' | ')));
	}

	pokazPlanszeAtaku(): void {
		console.log(`\n ${this.nazwa} - Plansza ataków:`);
		this.planszaAtaku.forEach(wiersz => console.log(wiersz.join(' | ')));
	}

	atakuj(przeciwnik: Gracz, x: number, y: number): boolean {
		console.log(`${this.nazwa} atakuje pozycję (${x}, ${y})`);
		if (przeciwnik.plansza[x][y] === 'X') {
			console.log("Trafiony!");
			this.planszaAtaku[x][y] = 'Z';
			przeciwnik.plansza[x][y] = 'Z';
			return true;
		} else {
			console.log("Pudło.");
			this.planszaAtaku[x][y] = 'O';
			return false;
		}
	}

	czyWszystkieStatkiZatopione(): boolean {
		return this.zajetePola.every(([x, y]) => this.plansza[x][y] === 'Z');
	}
}
class Statki {
	gracz1: Gracz;
	gracz2: Gracz;
	aktualnyGracz: Gracz;
	przeciwnik: Gracz;

	constructor(statkiGracz1: number[], statkiGracz2: number[]) {
		this.gracz1 = new Gracz("Gracz 1", statkiGracz1);
		this.gracz2 = new Gracz("Gracz 2", statkiGracz2);
		this.aktualnyGracz = this.gracz1;
		this.przeciwnik = this.gracz2;
	}


	zmienGracza(): void {
		[this.aktualnyGracz, this.przeciwnik] = [this.przeciwnik, this.aktualnyGracz];
	}

	wybierzStatekIUmiesc(): void {

		const testInputs1 = [
			{ rozmiar: 3, x: 0, y: 0, orientacja: 'poziomo' },
			{ rozmiar: 1, x: 2, y: 2, orientacja: 'poziomo' },
		];
		const testInputs2 = [
			{ rozmiar: 2, x: 0, y: 1, orientacja: 'pionowo' },
			{ rozmiar: 2, x: 1, y: 0, orientacja: 'poziomo' },
		];

		for (let input of testInputs1) {
			let { rozmiar, x, y, orientacja } = input;
			this.gracz1.rozmiescStatek(rozmiar, x, y, orientacja);
		}
		this.gracz1.pokazPlansze();

		for (let input of testInputs2) {
			let { rozmiar, x, y, orientacja } = input;
			this.gracz2.rozmiescStatek(rozmiar, x, y, orientacja);
		}
		this.gracz2.pokazPlansze();
	}

	grać(): void {
		console.log("Rozpoczynamy grę w statki!");

		this.wybierzStatekIUmiesc();

		const ataken = [
			{ x: 0, y: 0 }, // gracz1
			{ x: 0, y: 1 }, // gracz2 TRAFIONY
			{ x: 0, y: 0 }, // gracz2 
			{ x: 0, y: 2 },
			{ x: 2, y: 2 },
			{ x: 2, y: 2 }, // 
			{ x: 0, y: 1 }
		]

		let licznikAtakow = 0;

		while (licznikAtakow < ataken.length) {
			const { x, y } = ataken[licznikAtakow];

			console.log(`Tura gracza: ${this.aktualnyGracz.nazwa}, ruch numer ${this.aktualnyGracz.numerTury + 1}`);

			const trafiony = this.aktualnyGracz.atakuj(this.przeciwnik, x, y);
			this.aktualnyGracz.pokazPlanszeAtaku();

			if (this.przeciwnik.czyWszystkieStatkiZatopione()) {
				console.log(`${this.aktualnyGracz.nazwa} wygrywa!`);
				return;
			}

			if (!trafiony) {
				this.zmienGracza();
			} else {
				console.log(`${this.aktualnyGracz.nazwa} trafia i strzela ponownie!`);
			}

			this.aktualnyGracz.numerTury++;
			licznikAtakow++;
		}

		console.log("Koniec gry, nikt nie wygrał.");
	}
}

const statkiGracza1 = [3, 1];
const statkiGracza2 = [2, 2];

const gra = new Statki(statkiGracza1, statkiGracza2);
gra.grać();


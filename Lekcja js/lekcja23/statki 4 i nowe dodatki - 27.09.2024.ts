
// - potem dodam nowe statki: dwie 2 i cztery 1
// - Potem napiszę, żeby mi każdy statek nie był na skos tylko prostolinijnie
// - Potem dodam rozszerzę tablice o 4x4 i dodam jednego 4, dwie 3, trzy 2 i cztery 1
// - jeśli mi to wyjdzie to wtedy, robię 10x10 tablice w statkach
// - może zrobię wygraną jak w kółko i krzyżyk, że dopiero po 3 zwycięstwach jest 

class Statki {
	plansza: string[][];
	statki: number[];
	numerTury: number;
	zajetePola: [number, number][];

	constructor() {
		this.plansza = this.utworzPustaPlansze(3);
		this.statki = [3, 3, 2, 2, 1, 1, 1, 1];
		this.numerTury = 0;
		this.zajetePola = [];
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
			if (!this.czyPoleJestDostępneZOdstepem(poleX, poleY)) return false;
		}

		return true;
	}

	czyPoleJestDostępneZOdstepem(x: number, y: number): boolean {
		const kierunki = [-1, 0, 1];

		for (let sx of kierunki) {
			for (let sy of kierunki) {
				let zx = x + sx;
				let zy = y + sy;
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
	wybierzStatekIUmiesc(): void {

		const testInputs = [
			{ rozmiar: 3, x: 0, y: 0, orientacja: 'poziomo' },
			{ rozmiar: 2, x: 1, y: 1, orientacja: 'pionowo' },
			{ rozmiar: 1, x: 2, y: 2, orientacja: 'poziomo' },
			{ rozmiar: 1, x: 0, y: 1, orientacja: 'poziomo' }
		];

		let wybraneStatki = [...this.statki];
		for (let input of testInputs) {
			let { rozmiar, x, y, orientacja } = input;

			console.log(`Dostępne statki: ${wybraneStatki.join(', ')}`);
			console.log(`Wybieram statek o rozmiarze: ${rozmiar}`);
			console.log(`Ustawiam na pozycję: (${x}, ${y}), orientacja: ${orientacja}`);

			if (!wybraneStatki.includes(rozmiar)) {
				console.log("Niepoprawny wybór. Spróbuj ponownie.");
				continue;
			}

			this.rozmiescStatek(rozmiar, x, y, orientacja);
			wybraneStatki.splice(wybraneStatki.indexOf(rozmiar), 1);
		}
	}

	pokazPlansze(): void {
		console.log("\n Plansza:");
		this.plansza.forEach(wiersz => console.log(wiersz.join(' | ')));
	}

	grać(): void {
		console.log("Rozpoczynamy grę w statki!");
		this.wybierzStatekIUmiesc();
		this.pokazPlansze;
	}

}

const gra = new Statki();
gra.grać();


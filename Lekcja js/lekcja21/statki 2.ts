class Statki {
	wymiarPlanszy: number;
	planszaGracza1: string[][];
	planszaAtakowGracza1: string[][];
	planszaGracza2: string[][];
	planszaAtakowGracza2: string[][];
	numerTury: number;
	statki: { [key: number]: number[] };

	constructor(wymiarPlanszy: number) {
		this.wymiarPlanszy = wymiarPlanszy;
		this.planszaGracza1 = this.pustaPlanszaUtworz();
		this.planszaAtakowGracza1 = this.pustaPlanszaUtworz();
		this.planszaGracza2 = this.pustaPlanszaUtworz();
		this.planszaAtakowGracza2 = this.pustaPlanszaUtworz();
		this.numerTury = 0;
		this.statki = {
			1: [3, 2],
			2: [3, 2]
		};
	}

	pustaPlanszaUtworz(): string[][] {
		return Array.from({ length: this.wymiarPlanszy }, () => Array(this.wymiarPlanszy).fill(' '));
	}
	sprawdzicCzyMoznaUmiescStatek(gracz: number, pozycje: Punkt[]): boolean {
		const plansza = gracz == 1 ? this.planszaGracza1 : this.planszaGracza2;

		for (let { x, y } of pozycje) {
			if (x < 0 || x >= this.wymiarPlanszy || y < 0 || y >= this.wymiarPlanszy) {
				return false;
			}
			if (plansza[x][y] !== ' ') {
				return false;
			}

			const neighbors = [
				{ x: x - 1, y },
				{ x: x + 1, y },
				{ x, y: y - 1 },
				{ x, y: y + 1 },
				{ x: x - 1, y: y - 1 },
				{ x: x - 1, y: y + 1 },
				{ x: x + 1, y: y - 1 },
				{ x: x + 1, y: y + 1 },
			];

			for (let { x: zx, y: zy } of neighbors) {
				if (zx >= 0 && zx < this.wymiarPlanszy && zy >= 0 && y < this.wymiarPlanszy && plansza[zx][zy] === 'X') {
					return false;
				}
			}
		}

		return true;
	}


	umiescStatek(gracz: number, pozycje: Punkt[]) {
		if (!this.sprawdzicCzyMoznaUmiescStatek(gracz, pozycje)) {
			console.log(`Nie można umieśćić statku w tej lokalizacji!`);
			return;
		}

		const plansza = gracz === 1 ? this.planszaGracza1 : this.planszaGracza2;

		for (let { x, y } of pozycje) {
			plansza[x][y] = 'X';
		}
	}

	atakenStatek(gracz: number, x: number, y: number) {
		let planszaEnemy = gracz === 1 ? this.planszaGracza2 : this.planszaGracza1;
		let planszaAtaken = gracz === 1 ? this.planszaAtakowGracza2 : this.planszaAtakowGracza1;

		if (planszaAtaken[x][y] !== ' ') {
			console.log("To pole było już atakowane. Strzelaj gdzie indziej");
			return false;
		}

		if (planszaEnemy[x][y] === 'X') {
			planszaAtaken[x][y] = 'Z';
			planszaEnemy[x][y] = 'Z';
			console.log(`Gracz ${gracz} trafił w statek przeciwnika! `);
		} else {
			planszaAtaken[x][y] = 'O';
			console.log(`Gracz ${gracz} spudłował `);
		}

		this.numerTury++;
	}
	sprawdzWygrana(gracz: number): boolean {
		let planszaEnemy = gracz === 1 ? this.planszaGracza2 : this.planszaGracza1;
		return planszaEnemy.every(wiersz => wiersz.every(pole => pole !== 'X'));
	}

	pokazWszystkiePlansze() {
		console.log("\n Plansza gracza 1:");
		console.log("Plansza statków:");
		this.planszaGracza1.forEach(wiersz => console.log(wiersz.join(' | ')));
		console.log("Plansza atatków:");
		this.planszaAtakowGracza1.forEach(wiersz => console.log(wiersz.join(' | ')));

		console.log("\n Plansza gracza 2:");
		console.log("Plansza statków:");
		this.planszaGracza2.forEach(wiersz => console.log(wiersz.join(' | ')));
		console.log("Plansza atatków:");
		this.planszaAtakowGracza2.forEach(wiersz => console.log(wiersz.join(' | ')));
	}



	//wprowadzenie ręcznie ruchów v
	grać() {
		while (!this.sprawdzWygrana(1) && !this.sprawdzWygrana(2)) {

			console.log(`\nTura: ${this.numerTury + 1}`)

			this.pokazWszystkiePlansze();


			if (this.numerTury % 2 === 0) {
				console.log("Ruch gracza 1:");
				this.atakenStatek(1, Math.floor(Math.random() * 3), Math.floor(Math.random() * 3));
			} else {
				console.log("Ruch gracza 2:");
				this.atakenStatek(1, Math.floor(Math.random() * 3), Math.floor(Math.random() * 3))
			}
		}

		console.log("\n Koniec Gry.");

		this.pokazWszystkiePlansze();

		if (this.sprawdzWygrana(1)) {
			console.log("Zwycieca Gracz 1");
			return;
		} else {
			console.log("Zwycieca Gracz 2");
			return;
		}
	}
}

interface Punkt {
	x: number;
	y: number;
}

let gra = new Statki(3);

gra.umiescStatek(1, [{ x: 0, y: 0 }, { x: 0, y: 1 }, { x: 0, y: 2 }]);
gra.umiescStatek(2, [{ x: 1, y: 0 }, { x: 1, y: 1 }, { x: 1, y: 2 }]);


gra.grać();
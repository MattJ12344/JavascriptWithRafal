class Statki {
	wymiarPlanszy: number;
	planszaGracza1: string[][];
	planszaAtakowGracza1: string[][];
	planszaGracza2: string[][];
	planszaAtakowGracza2: string[][];
	numerTury: number;

	constructor(wymiarPlanszy: number) {
		this.wymiarPlanszy = wymiarPlanszy;
		this.planszaGracza1 = this.pustaPlanszaUtworz();
		this.planszaAtakowGracza1 = this.pustaPlanszaUtworz();
		this.planszaGracza2 = this.pustaPlanszaUtworz();
		this.planszaAtakowGracza2 = this.pustaPlanszaUtworz();
		this.numerTury = 0;
	}

	pustaPlanszaUtworz(): string[][] {
		let plansza: string[][] = [];
		for (let i = 0; i < this.wymiarPlanszy; i++) {
			plansza.push(Array(this.wymiarPlanszy).fill(' '));
		}
		return plansza;
	}

	umiescStatek(gracz: number, x: number, y: number) {
		if (gracz === 1) {
			if (this.planszaGracza1[x][y] === ' ') {
				this.planszaGracza1[x][y] = 'X';
			} else {
				console.log("Tu już jest statek!");
			}
		} else {
			if (this.planszaGracza2[x][y] === ' ') {
				this.planszaGracza2[x][y] = 'X';
			} else {
				console.log("Tu już jest statek!");
			}
		}
	}

	atakenStatek(gracz: number, x: number, y: number) {
		let planszaEnemy = gracz === 1 ? this.planszaGracza2 : this.planszaGracza1;
		let planszaAtaken = gracz === 1 ? this.planszaAtakowGracza2 : this.planszaAtakowGracza1;

		if (planszaAtaken[x][y] !== ' ') {
			console.log("To pole było już atakowane. Strzelaj gdzie indziej");
			return;
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

	sprawdzWygrana(gracz: number) {
		let planszaEnemy = gracz === 1 ? this.planszaGracza1 : this.planszaGracza2;
		return planszaEnemy.every(wiersz => wiersz.every(pole => pole !== 'X'));
	}

	pokazPlansze(gracz: number) {
		let planszaAtaken = gracz === 1 ? this.planszaAtakowGracza2 : this.planszaAtakowGracza1;
		console.log(`Plansza ataków gracza ${gracz}:`);
		planszaAtaken.forEach(wiersz => console.log(wiersz.join(' 	')));
	}

	pokazPlanszeGracza(gracz: number) {
		let plansza = gracz === 1 ? this.planszaGracza2 : this.planszaGracza1;
		console.log(`Plansza statków gracza ${gracz}:`);
		plansza.forEach(wiersz => console.log(wiersz.join(' ')));
	}

	//wprowadzenie ręcznie ruchów v
	grać() {
		while (!this.sprawdzWygrana(1) && !this.sprawdzWygrana(2)) {

			console.log(`\nTura: ${this.numerTury + 1}`)
			this.pokazPlansze(1);
			this.pokazPlansze(2);

			if (this.numerTury % 2 === 0) {
				console.log("Ruch gracza 1:");
				this.atakenStatek(1, 0, 0);
			} else {
				console.log("Ruch gracza 2:");
				this.atakenStatek(2, 1, 1);
			}
		}

		console.log("\n Koniec Gry.");

		if (this.sprawdzWygrana(1)) {
			console.log("Zwycieca Gracz 2");
		} else {
			console.log("Zwycieca Gracz 1");
		}
	}
}

let gra = new Statki(3);

gra.umiescStatek(1, 0, 0);
gra.umiescStatek(1, 1, 2);
gra.umiescStatek(1, 2, 2);

gra.umiescStatek(2, 0, 0);
gra.umiescStatek(2, 1, 2);
gra.umiescStatek(2, 2, 2);

gra.pokazPlanszeGracza(1);
gra.pokazPlanszeGracza(2);

gra.grać();
Zmienne, parametry i pola są podobne do siebie, ale jednak się różnią.
1. Zmienne - definujemy:
let nazwaZmiennej: TypZmiennej = wartośćZmiennej;
zmienne mogą być w środku funkcji, w sródku pętli, w środku contructora

function nazwaFunkcji() {
      let zmienna = 3;
}

2. Parametry - to jest INPUT, który przekazujemy w funkcjach albo constructorach

function nazwaFunkcji(parametr1: TypParametru): TypOutputu {
}

contructor(parametr2: TypParametru) {
}

3. Pole - to w dużym uproszczeniu "zmienna na poziomie klasy"

class NazwaKlasy {
     nazwaPola: TypPola = 3;
}

możemy do niej mieć dostęp w klasie za pomocą this.nazwaPola
tak samo jak do funkcji, która należy do klasy np
this.jakasFunkcja()
ale TEŻ TYLKO W KLASIE
po za klasa bedzie
let jakisObiekt: JakasKlasa = new JakasKlasa()

jakisObiekt.jakasFunkcja();
albo
jakisObiekt.jakiesPole;
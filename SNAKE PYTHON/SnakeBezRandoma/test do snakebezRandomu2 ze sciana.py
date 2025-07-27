from SnakeBezRandomu2ZeSciana import Snake
from typing import List

def test1():
    gra = Snake(3)
    gra.wygenerujPlansze()
    gra.wygenerujSnake(0, 0)
    gra.dodajPrzeszkodeNaSrodek()
    gra.postawOwoc(0, 2)

    poczatkowaPlansza1: str = (
            "[1][ ][O]\n"
            "[ ][#][ ]\n"
            "[ ][ ][ ]\n"
          
        )

    # print(gra.planszaNaString())
    # print(poczatkowaPlansza1)

    assert gra.planszaNaString() == poczatkowaPlansza1

    ruchyDoWykonania: List[str] = ["d", "d", "D", "S"]
    gra.wykonajRuchy(ruchyDoWykonania)

    spodziewanaPlansza1: str = (
            "[2][ ][ ]\n"
            "[1][#][ ]\n"
            "[ ][ ][ ]\n"
        )

    print("gra.planszaNaString() \n", gra.planszaNaString())
    print("spodziewanaPlansza1 \n", spodziewanaPlansza1)

    assert gra.planszaNaString() == spodziewanaPlansza1 , "Planasza zgadza się z spodziewaną"
    assert gra.ileZjedzonychOwockow() == 1


def test2():
    gra = Snake(5)
    gra.wygenerujPlansze()
    gra.wygenerujSnake(0, 0)
    gra.dodajPrzeszkodeNaSrodek()
    gra.postawOwoc(4, 4)

    poczatkowaPlansza2: str = (
            "[2][1][ ][ ][ ]\n"
            "[ ][ ][ ][ ][ ]\n"
            "[ ][ ][#][ ][ ]\n"
            "[ ][ ][ ][ ][ ]\n"
            "[ ][ ][ ][ ][O]\n"
            
        )

    # print(gra.planszaNaString())
    # print(poczatkowaPlansza2)

    assert gra.planszaNaString() == poczatkowaPlansza2

    ruchyDoWykonania: List[str] = ["d", "d", "s", "s", "s", "s", "d", "d", "w", "W"]
    gra.wykonajRuchy(ruchyDoWykonania)

    spodziewanaPlansza2: str = (
            "[ ][ ][ ][ ][ ]\n"
            "[ ][ ][ ][ ][ ]\n"
            "[1][ ][#][ ][ ]\n"
            "[2][ ][ ][ ][ ]\n"
            "[3][ ][ ][ ][ ]\n"
        )

    print("gra.planszaNaString() \n", gra.planszaNaString())
    print("spodziewanaPlansza2 \n", spodziewanaPlansza2)

    assert gra.planszaNaString() == spodziewanaPlansza2 , "Planasza zgadza się z spodziewaną"
    assert gra.ileZjedzonychOwockow() == 1


def test3():
    gra = Snake(3)
    gra.wygenerujPlansze()
    gra.wygenerujSnake(0, 0)
    gra.dodajPrzeszkodeNaSrodek()
    gra.postawOwoc(0, 2)

    poczatkowaPlansza1: str = (
        "[1][ ][O]\n"
        "[ ][#][ ]\n"
        "[ ][ ][ ]\n"

    )

    # print(gra.planszaNaString())
    # print(poczatkowaPlansza1)

    assert gra.planszaNaString() == poczatkowaPlansza1


    gra.zczytywanieZTerminala()d

    spodziewanaPlansza1: str = (
        "[Z][ ][ ]\n"
        "[Z][#][ ]\n"
        "[ ][ ][ ]\n"
    )

    print("gra.planszaNaString() \n", gra.planszaNaString())
    print("spodziewanaPlansza1 \n", spodziewanaPlansza1)

    assert gra.planszaNaString() == spodziewanaPlansza1, "Planasza zgadza się z spodziewaną"
    assert gra.ileZjedzonychOwockow() == 1


# test1()
# test2()
test3()

from SnakeBezRandomu import Snake
from typing import List

#---Test1---
#początkowy snake
def test1():
    print("TEST 1")
    waz1: Snake = Snake(3)
    waz1.wygenerujPlansze()
    waz1.wygenerujSnake(0, 0)
    waz1.postawOwoc(0, 2)

    poczatkowaPlansza1: str = (
        "[1][ ][O]\n"
        "[ ][ ][ ]\n"
        "[ ][ ][ ]\n"
    )

    # print(waz1.planszaNaString())
    # print(poczatkowaPlansza1)

    assert waz1.planszaNaString() == poczatkowaPlansza1

    ruchyDoWykonania: List[str] = ["d", "d"]
    waz1.wykonajRuchy(ruchyDoWykonania)

    spodziewanaPlansza1: str = (
        "[ ][2][1]\n"
        "[ ][ ][ ]\n"
        "[ ][ ][ ]\n"
    )

    print(waz1.planszaNaString())
    print(spodziewanaPlansza1)

    assert waz1.planszaNaString() == spodziewanaPlansza1 , "Planasza zgadza się z spodziewaną"
    assert waz1.ileZjedzonychOwockow() == 1

#==============================================================================================================
#nowa gra2
#---Test2---
def test2():

    print("TEST 2")
    waz2: Snake = Snake(3)
    waz2.wygenerujPlansze()
    waz2.wygenerujSnake(0, 0)
    waz2.postawOwoc(2, 0)
    waz2.postawOwoc(2, 1)



    poczatkowaPlansza2: str = (
        "[1][ ][ ]\n"
        "[ ][ ][ ]\n"
        "[O][O][ ]\n"
    )

    assert waz2.planszaNaString() == poczatkowaPlansza2

    ruchyDoWykonania2: List[str] = ["s", "s", "d"]
    waz2.wykonajRuchy(ruchyDoWykonania2)

    spodziewanaPlansza2: str = (
        "[ ][ ][ ]\n"
        "[3][ ][ ]\n"
        "[2][1][ ]\n"
    )


    print(waz2.planszaNaString())
    print(spodziewanaPlansza2)

    assert waz2.planszaNaString() == spodziewanaPlansza2 , "Planasza zgadza się z spodziewaną"
    assert waz2.ileZjedzonychOwockow() == 2

#==============================================================================================================
#nowa gra3
#---Test3---
# tu będzie długi snake

def test3():
    print("TEST 3")

    waz3: Snake = Snake(3)
    waz3.wygenerujPlansze()
    waz3.wygenerujSnake(0, 0)
    waz3.postawOwoc(1, 2)
    waz3.postawOwoc(2, 0)
    waz3.postawOwoc(1, 0)
    waz3.postawOwoc(1, 1)



    poczatkowaPlansza3: str = (
        "[1][ ][ ]\n"
        "[O][O][O]\n"
        "[O][ ][ ]\n"
    )

    assert waz3.planszaNaString() == poczatkowaPlansza3

    ruchyDoWykonania3: List[str] = ["d", "d", "s", "s", "a", "a", "w", "d"]
    waz3.wykonajRuchy(ruchyDoWykonania3)

    spodziewanaPlansza3: str = (
        "[ ][ ][ ]\n"
        "[2][1][ ]\n"
        "[3][4][5]\n"
    )


    print(waz3.planszaNaString())
    print(spodziewanaPlansza3)

    assert waz3.planszaNaString() == spodziewanaPlansza3 , "Planasza zgadza się z spodziewaną"
    assert waz3.ileZjedzonychOwockow() == 4

#==============================================================================================================
#Nowa gra 4
#---Test4---
#wąż wpada w ścianę

def test4():
    print("TEST 4")

    waz4: Snake = Snake(3)
    waz4.wygenerujPlansze()
    waz4.wygenerujSnake(0, 0)
    waz4.postawOwoc(1, 2)


    poczatkowaPlansza4: str = (
        "[1][ ][ ]\n"
        "[ ][ ][O]\n"
        "[ ][ ][ ]\n"
    )

    assert waz4.planszaNaString() == poczatkowaPlansza4

    ruchyDoWykonania4: List[str] = ["d", "d", "d"]
    waz4.wykonajRuchy(ruchyDoWykonania4)

    spodziewanaPlansza4: str = (
        "[ ][ ][Z]\n"
        "[ ][ ][O]\n"
        "[ ][ ][ ]\n"
    )


    print(waz4.planszaNaString())
    print(spodziewanaPlansza4)

    assert waz4.planszaNaString() == spodziewanaPlansza4 , "Planasza zgadza się z spodziewaną"
    assert waz4.koniecGry == True
    assert waz4.ileZjedzonychOwockow() == 0

#==============================================================================================================
#Nowa gra 5
#---Test5---
#wąż wpada w siebie
def test5():
        
    print("TEST 5")
    waz5: Snake = Snake(3)
    waz5.wygenerujPlansze()
    waz5.wygenerujSnake(0, 0)
    waz5.postawOwoc(0, 1)
    waz5.postawOwoc(0, 2)
    waz5.postawOwoc(1, 2)

    poczatkowaPlansza5: str = (
        "[1][O][O]\n"
        "[ ][ ][O]\n"
        "[ ][ ][ ]\n"
    )

    assert waz5.planszaNaString() == poczatkowaPlansza5

    ruchyDoWykonania5: List[str] = ["d", "d", "s", "s", "a", "w", "d"]
    waz5.wykonajRuchy(ruchyDoWykonania5)

    spodziewanaPlansza5: str = (
        "[ ][ ][ ]\n"
        "[ ][Z][Z]\n"
        "[ ][Z][Z]\n"
    )

    print(waz5.planszaNaString())
    print(spodziewanaPlansza5)

    assert waz5.planszaNaString() == spodziewanaPlansza5 , "Planasza zgadza się z spodziewaną"
    assert waz5.koniecGry == True
    assert waz5.ileZjedzonychOwockow() == 3
    
    
def test6():
    print("TEST 1")
    waz1: Snake = Snake(3)
    waz1.wygenerujPlansze()
    waz1.wygenerujSnake(0, 0)
    waz1.postawOwoc(0, 2)

    poczatkowaPlansza1: str = (
        "[1][ ][O]\n"
        "[ ][ ][ ]\n"
        "[ ][ ][ ]\n"
    )

    # print(waz1.planszaNaString())
    # print(poczatkowaPlansza1)

    assert waz1.planszaNaString() == poczatkowaPlansza1

    ruchyDoWykonania: List[str] = ["e", "d"]
    waz1.wykonajRuchy(ruchyDoWykonania)

    spodziewanaPlansza1: str = (
        "[ ][2][1]\n"
        "[ ][ ][ ]\n"
        "[ ][ ][ ]\n"
    )

    print(waz1.planszaNaString())
    print(spodziewanaPlansza1)

    assert waz1.planszaNaString() == spodziewanaPlansza1 , "Planasza zgadza się z spodziewaną"
    assert waz1.ileZjedzonychOwockow() == 1 
    
    
    
test1()
test2()
test3()
test4()
test5()
test6()
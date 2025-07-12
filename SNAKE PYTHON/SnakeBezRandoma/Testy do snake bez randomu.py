from SnakeBezRandomu import Snake
from typing import List

#---Test1---
#początkowy snake
def test1():
    print("TEST 1")
    waz1: Snake = Snake(5)
    waz1.wygenerujPlansze()
    waz1.wygenerujSnake(0, 0)
    waz1.postawOwoc(0, 2)

    poczatkowaPlansza1: str = (
        "[2][1][O][ ][ ]\n"
        "[ ][ ][ ][ ][ ]\n"
        "[ ][ ][ ][ ][ ]\n"
        "[ ][ ][ ][ ][ ]\n"
        "[ ][ ][ ][ ][ ]\n"
        
    )

    # print(waz1.planszaNaString())
    # print(poczatkowaPlansza1)

    assert waz1.planszaNaString() == poczatkowaPlansza1

    ruchyDoWykonania: List[str] = ["d", "d"]
    waz1.wykonajRuchy(ruchyDoWykonania)

    spodziewanaPlansza1: str = (
        "[ ][3][2][1][ ]\n"
        "[ ][ ][ ][ ][ ]\n"
        "[ ][ ][ ][ ][ ]\n"
        "[ ][ ][ ][ ][ ]\n"
        "[ ][ ][ ][ ][ ]\n"
    )

    print("waz1.planszaNaString() \n", waz1.planszaNaString())
    print("spodziewanaPlansza1 \n", spodziewanaPlansza1)

    assert waz1.planszaNaString() == spodziewanaPlansza1 , "Planasza zgadza się z spodziewaną"
    assert waz1.ileZjedzonychOwockow() == 1

#=====================================================================================================
#nowa gra2
#---Test2---
def test2():
    
    print("TEST 2")
    waz2: Snake = Snake(5)
    waz2.wygenerujPlansze()
    waz2.wygenerujSnake(0, 0)
    waz2.postawOwoc(2, 0)
    waz2.postawOwoc(2, 1)



    poczatkowaPlansza2: str = (
        "[2][1][ ][ ][ ]\n"
        "[ ][ ][ ][ ][ ]\n"
        "[O][O][ ][ ][ ]\n"
        "[ ][ ][ ][ ][ ]\n"
        "[ ][ ][ ][ ][ ]\n"
    )

    assert waz2.planszaNaString() == poczatkowaPlansza2

    ruchyDoWykonania2: List[str] = ["s", "s", "a"]
    waz2.wykonajRuchy(ruchyDoWykonania2)

    spodziewanaPlansza2: str = (
        "[ ][4][ ][ ][ ]\n"
        "[ ][3][ ][ ][ ]\n"
        "[1][2][ ][ ][ ]\n"
        "[ ][ ][ ][ ][ ]\n"
        "[ ][ ][ ][ ][ ]\n"
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

    waz3: Snake = Snake(5)
    waz3.wygenerujPlansze()
    waz3.wygenerujSnake(0, 0)
    waz3.postawOwoc(1, 3)
    waz3.postawOwoc(2, 1)
    waz3.postawOwoc(3, 4)
    waz3.postawOwoc(4, 0)



    poczatkowaPlansza3: str = (
        "[2][1][ ][ ][ ]\n"
        "[ ][ ][ ][O][ ]\n"
        "[ ][O][ ][ ][ ]\n"
        "[ ][ ][ ][ ][O]\n"
        "[O][ ][ ][ ][ ]\n"
    )
    
    # print("waz3.planszaNaString(): \n", waz3.planszaNaString())
    
    # print("poczatkowaPlansza3: \n", poczatkowaPlansza3)


    assert waz3.planszaNaString() == poczatkowaPlansza3

    ruchyDoWykonania3: List[str] = ["d", "d", "s", "s", "a", "a", "s", "d", "d", "d", "s", "a", "a", "a", "a"]
    waz3.wykonajRuchy(ruchyDoWykonania3)

    spodziewanaPlansza3: str = (
        "[ ][ ][ ][ ][ ]\n"
        "[ ][ ][ ][ ][ ]\n"
        "[ ][ ][ ][ ][ ]\n"
        "[ ][ ][ ][ ][6]\n"
        "[1][2][3][4][5]\n"
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

    waz4: Snake = Snake(5)
    waz4.wygenerujPlansze()
    waz4.wygenerujSnake(0, 0)
    waz4.postawOwoc(1, 2)


    poczatkowaPlansza4: str = (
        "[2][1][ ][ ][ ]\n"
        "[ ][ ][O][ ][ ]\n"
        "[ ][ ][ ][ ][ ]\n"
        "[ ][ ][ ][ ][ ]\n"
        "[ ][ ][ ][ ][ ]\n"
    )

    assert waz4.planszaNaString() == poczatkowaPlansza4

    ruchyDoWykonania4: List[str] = ["d", "d", "d", "d"]
    waz4.wykonajRuchy(ruchyDoWykonania4)

    spodziewanaPlansza4: str = (
        "[ ][ ][ ][Z][Z]\n"
        "[ ][ ][O][ ][ ]\n"
        "[ ][ ][ ][ ][ ]\n"
        "[ ][ ][ ][ ][ ]\n"
        "[ ][ ][ ][ ][ ]\n"
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
    waz5: Snake = Snake(5)
    waz5.wygenerujPlansze()
    waz5.wygenerujSnake(0, 0)
    waz5.postawOwoc(0, 2)
    waz5.postawOwoc(0, 3)
    waz5.postawOwoc(1, 4)

    poczatkowaPlansza5: str = (
        "[2][1][O][O][ ]\n"
        "[ ][ ][ ][ ][O]\n"
        "[ ][ ][ ][ ][ ]\n"
        "[ ][ ][ ][ ][ ]\n"
        "[ ][ ][ ][ ][ ]\n"
    )

    assert waz5.planszaNaString() == poczatkowaPlansza5

    ruchyDoWykonania5: List[str] = ["d", "d", "d", "s", "a", "w"]
    waz5.wykonajRuchy(ruchyDoWykonania5)

    spodziewanaPlansza5: str = (
        "[ ][ ][Z][Z][Z]\n"
        "[ ][ ][ ][Z][Z]\n"
        "[ ][ ][ ][ ][ ]\n"
        "[ ][ ][ ][ ][ ]\n"
        "[ ][ ][ ][ ][ ]\n"
    )

    print(waz5.planszaNaString())
    print(spodziewanaPlansza5)

    assert waz5.planszaNaString() == spodziewanaPlansza5 , "Planasza zgadza się z spodziewaną"
    assert waz5.koniecGry == True
    assert waz5.ileZjedzonychOwockow() == 3



test1()
test2()
test3()
test4()
test5()
from SnakeBezRandomu import Snake
from typing import List

#---Test1---
#początkowy snake
def test1():
    print("TEST 1")
    waz1: Snake = Snake(10)
    waz1.wygenerujPlansze()
    waz1.wygenerujSnake(0, 0)
    waz1.postawOwoc(0, 7)

    poczatkowaPlansza1: str = (
        "[3][2][1][ ][ ][ ][ ][O][ ][ ]\n"
        "[ ][ ][ ][ ][ ][ ][ ][ ][ ][ ]\n"
        "[ ][ ][ ][ ][ ][ ][ ][ ][ ][ ]\n"
        "[ ][ ][ ][ ][ ][ ][ ][ ][ ][ ]\n"
        "[ ][ ][ ][ ][ ][ ][ ][ ][ ][ ]\n"
        "[ ][ ][ ][ ][ ][ ][ ][ ][ ][ ]\n"
        "[ ][ ][ ][ ][ ][ ][ ][ ][ ][ ]\n"
        "[ ][ ][ ][ ][ ][ ][ ][ ][ ][ ]\n"
        "[ ][ ][ ][ ][ ][ ][ ][ ][ ][ ]\n"
        "[ ][ ][ ][ ][ ][ ][ ][ ][ ][ ]\n"        
    )

    # print(waz1.planszaNaString())
    # print(poczatkowaPlansza1)

    assert waz1.planszaNaString() == poczatkowaPlansza1

    ruchyDoWykonania: List[str] = ["d", "d", "d", "d", "d"]
    waz1.wykonajRuchy(ruchyDoWykonania)

    spodziewanaPlansza1: str = (
        "[ ][ ][ ][ ][4][3][2][1][ ][ ]\n"
        "[ ][ ][ ][ ][ ][ ][ ][ ][ ][ ]\n"
        "[ ][ ][ ][ ][ ][ ][ ][ ][ ][ ]\n"
        "[ ][ ][ ][ ][ ][ ][ ][ ][ ][ ]\n"
        "[ ][ ][ ][ ][ ][ ][ ][ ][ ][ ]\n"
        "[ ][ ][ ][ ][ ][ ][ ][ ][ ][ ]\n"
        "[ ][ ][ ][ ][ ][ ][ ][ ][ ][ ]\n"
        "[ ][ ][ ][ ][ ][ ][ ][ ][ ][ ]\n"
        "[ ][ ][ ][ ][ ][ ][ ][ ][ ][ ]\n"
        "[ ][ ][ ][ ][ ][ ][ ][ ][ ][ ]\n"                  
    )

    print("waz1.planszaNaString():\n", waz1.planszaNaString())
    print("spodziewanaPlansza1:\n", spodziewanaPlansza1)

    assert waz1.planszaNaString() == spodziewanaPlansza1 , "Planasza zgadza się z spodziewaną"
    assert waz1.ileZjedzonychOwockow() == 1
    
    
#==============================================================================================================
#nowa gra2
#---Test2---    
def test2():
    print("TEST 2")
    waz2: Snake = Snake(10)
    waz2.wygenerujPlansze()
    waz2.wygenerujSnake(0, 0)
    waz2.postawOwoc(3, 2)
    waz2.postawOwoc(2, 6)

    poczatkowaPlansza2: str = (
        "[3][2][1][ ][ ][ ][ ][ ][ ][ ]\n"
        "[ ][ ][ ][ ][ ][ ][ ][ ][ ][ ]\n"
        "[ ][ ][ ][ ][ ][ ][O][ ][ ][ ]\n"
        "[ ][ ][O][ ][ ][ ][ ][ ][ ][ ]\n"
        "[ ][ ][ ][ ][ ][ ][ ][ ][ ][ ]\n"
        "[ ][ ][ ][ ][ ][ ][ ][ ][ ][ ]\n"
        "[ ][ ][ ][ ][ ][ ][ ][ ][ ][ ]\n"
        "[ ][ ][ ][ ][ ][ ][ ][ ][ ][ ]\n"
        "[ ][ ][ ][ ][ ][ ][ ][ ][ ][ ]\n"
        "[ ][ ][ ][ ][ ][ ][ ][ ][ ][ ]\n"        
    )

    # print(waz1.planszaNaString())
    # print(poczatkowaPlansza1)

    assert waz2.planszaNaString() == poczatkowaPlansza2

    ruchyDoWykonania: List[str] = ["s", "s", "s", "d", "d", "d", "D", "W"]
    waz2.wykonajRuchy(ruchyDoWykonania)

    spodziewanaPlansza2: str = (
        "[ ][ ][ ][ ][ ][ ][ ][ ][ ][ ]\n"
        "[ ][ ][ ][ ][ ][ ][ ][ ][ ][ ]\n"
        "[ ][ ][ ][ ][ ][ ][1][ ][ ][ ]\n"
        "[ ][ ][ ][5][4][3][2][ ][ ][ ]\n"
        "[ ][ ][ ][ ][ ][ ][ ][ ][ ][ ]\n"
        "[ ][ ][ ][ ][ ][ ][ ][ ][ ][ ]\n"
        "[ ][ ][ ][ ][ ][ ][ ][ ][ ][ ]\n"
        "[ ][ ][ ][ ][ ][ ][ ][ ][ ][ ]\n"
        "[ ][ ][ ][ ][ ][ ][ ][ ][ ][ ]\n"
        "[ ][ ][ ][ ][ ][ ][ ][ ][ ][ ]\n"                  
    )

    print("waz2.planszaNaString():\n", waz2.planszaNaString())
    print("spodziewanaPlansza2:\n", spodziewanaPlansza2)

    assert waz2.planszaNaString() == spodziewanaPlansza2 , "Planasza zgadza się z spodziewaną"
    assert waz2.ileZjedzonychOwockow() == 2
    
#==============================================================================================================
#nowa gra3
#---Test3---
# tu będzie długi snake
def test3():
    print("TEST 3")
    waz3: Snake = Snake(10)
    waz3.wygenerujPlansze()
    waz3.wygenerujSnake(0, 0)
    waz3.postawOwoc(0, 6)
    waz3.postawOwoc(3, 1)
    waz3.postawOwoc(5, 8)
    waz3.postawOwoc(6, 3)
    waz3.postawOwoc(9, 7)
    

    poczatkowaPlansza3: str = (
        "[3][2][1][ ][ ][ ][O][ ][ ][ ]\n"
        "[ ][ ][ ][ ][ ][ ][ ][ ][ ][ ]\n"
        "[ ][ ][ ][ ][ ][ ][ ][ ][ ][ ]\n"
        "[ ][O][ ][ ][ ][ ][ ][ ][ ][ ]\n"
        "[ ][ ][ ][ ][ ][ ][ ][ ][ ][ ]\n"
        "[ ][ ][ ][ ][ ][ ][ ][ ][O][ ]\n"
        "[ ][ ][ ][O][ ][ ][ ][ ][ ][ ]\n"
        "[ ][ ][ ][ ][ ][ ][ ][ ][ ][ ]\n"
        "[ ][ ][ ][ ][ ][ ][ ][ ][ ][ ]\n"
        "[ ][ ][ ][ ][ ][ ][ ][O][ ][ ]\n"        
    )

    # print(waz1.planszaNaString())
    # print(poczatkowaPlansza1)

    assert waz3.planszaNaString() == poczatkowaPlansza3
    
    ruchyDoWykonania: List[str] = ["d", "D", "d", "D", "S", "S", "S", "a", "a", "a", "a", "a", "S", "s", "S", "D", "D", "d", "d", "d", "d", "W", "D", "d", "S", "s", "S", "S", "a", "a"]
    waz3.wykonajRuchy(ruchyDoWykonania)

    spodziewanaPlansza3: str = (
        "[ ][ ][ ][ ][ ][ ][ ][ ][ ][ ]\n"
        "[ ][ ][ ][ ][ ][ ][ ][ ][ ][ ]\n"
        "[ ][ ][ ][ ][ ][ ][ ][ ][ ][ ]\n"
        "[ ][ ][ ][ ][ ][ ][ ][ ][ ][ ]\n"
        "[ ][ ][ ][ ][ ][ ][ ][ ][ ][ ]\n"
        "[ ][ ][ ][ ][ ][ ][ ][ ][8][7]\n"
        "[ ][ ][ ][ ][ ][ ][ ][ ][ ][6]\n"
        "[ ][ ][ ][ ][ ][ ][ ][ ][ ][5]\n"
        "[ ][ ][ ][ ][ ][ ][ ][ ][ ][4]\n"
        "[ ][ ][ ][ ][ ][ ][ ][1][2][3]\n"                  
    )

    print("waz3.planszaNaString():\n", waz3.planszaNaString())
    print("spodziewanaPlansza3:\n", spodziewanaPlansza3)

    assert waz3.planszaNaString() == spodziewanaPlansza3 , "Planasza zgadza się z spodziewaną"
    assert waz3.ileZjedzonychOwockow() == 5
    
    
    
    
    
    
#==================================================================================================    
test1()
test2()
test3()
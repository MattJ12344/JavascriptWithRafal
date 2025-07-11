from typing import List

lista1:List[int] = [1, 2, 3, 4]

lista2:List[int] = [1, 2, 3, 4]

lista3:List[int] = [1, 2, 3, 4]

lista1.pop(1)

assert lista1 == [1, 3, 4]

lista2.remove(3)

assert lista2 == [1, 2, 4]

lista3.pop()

assert lista3 == [1, 2, 3]

#-------------------------------------------------------------------------------------------------
lista11:List[List[int]] = [
    [1, 2, 3, 4],
    [5, 6, 7, 8]
    ]

lista22:List[List[int]] = [
    [1, 2, 3, 4],
    [5, 6, 7, 8]
    ]

lista33:List[List[int]] = [
    [1, 2, 3, 4],
    [5, 6, 7, 8]
    ]

cos1:List[int] = lista11.pop(1)

assert lista11 == [
    [1, 2, 3, 4]
    ]

assert cos1 == [5, 6, 7, 8]

lista22.remove([1, 2, 3, 4])

assert lista22 == [
    [5, 6, 7, 8]
    ]



lista33.pop()

assert lista33 == [
    [1, 2, 3, 4]
    ]

cos2:List[int] = lista33.pop()

assert cos2 == [1, 2, 3, 4]


#===============================

class Snake:
    def sth():
        print("1")

liscik: List[Snake] = [
    Snake(),
    Snake(),
]

liscik.pop()
liscik.remove()
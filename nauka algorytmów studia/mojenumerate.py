from typing import List, Tuple, Any

def mojEnumerate(lista: List) -> List[Tuple]:
    print(f"Input lista {lista}")

    wynik: List[Tuple] = []

    cos:int = len(lista)

    for i in range(cos):
        elemnt = lista[i]
        para: Tuple = (i, elemnt)
        wynik.append(para)

    print(f"Wynik mojenumerate: {wynik}")
    print("")
    return wynik

lista1: List = ["a"]
wynik1: List[Tuple] = [(0, "a")]
assert mojEnumerate(lista1) == wynik1
assert mojEnumerate(lista1) == list(enumerate(lista1))

lista2: List = ["a", "b", "c"]
wynik2: List[Tuple] = [(0, "a"), (1, "b"), (2, "c")]
assert mojEnumerate(lista2) == wynik2
assert mojEnumerate(lista2) == list(enumerate(lista2))

lista3: List = [1, 2, 3]
wynik3: List[Tuple] = [(0, 1), (1, 2), (2, 3)]
assert mojEnumerate(lista3) == wynik3
assert mojEnumerate(lista3) == list(enumerate(lista3))

lista4: List = []
wynik4: List[Tuple] = []
assert mojEnumerate(lista4) == wynik4
assert mojEnumerate(lista4) == list(enumerate(lista4))

lista5: List = [1.0, 2.2, 3.65, 54.364]
wynik5: List[Tuple] = [(0, 1.0), (1, 2.2), (2, 3.65), (3, 54.364)]
assert mojEnumerate(lista5) == wynik5
assert mojEnumerate(lista5) == list(enumerate(lista5))

lista6: List = [[1], [2], [3], [4]]
wynik6: List[Tuple] = [(0, [1]), (1, [2]), (2, [3]), (3, [4])]
assert mojEnumerate(lista6) == wynik6
assert mojEnumerate(lista6) == list(enumerate(lista6))

lista7: List = [{"jeden": 1}, {"dwa": 2}, {"trzy": 3}]
wynik7: List[Tuple] = [(0, {"jeden": 1}), (1, {"dwa": 2}), (2, {"trzy": 3})]
assert mojEnumerate(lista7) == wynik7
assert mojEnumerate(lista7) == list(enumerate(lista7))

lista8: List = [1, "dwa", 3.0, [4], {"piec": 5}]
wynik8: List[Tuple] = [(0, 1), (1, "dwa"), (2, 3.0), (3, [4]), (4, {"piec": 5})]
assert mojEnumerate(lista8) == wynik8
assert mojEnumerate(lista8) == list(enumerate(lista8))

lista2D: List[List[int]] = [[1, 2], [3, 4], [5, 6]]
wynik9: List[Tuple[int, List[int]]] = [
    (0, [1, 2]),
    (1, [3, 4]),
    (2, [5, 6])
]
assert mojEnumerate(lista2D) == wynik9
assert mojEnumerate(lista2D) == list(enumerate(lista2D))

lista3D: List[List[List[int]]] = [
    [[1, 2], [3, 4]],
    [[5, 6], [7, 8]],
    [[9, 10], [11, 12]]
]

wynik10: List[Tuple[int, List[List[int]]]] = [
    (0, [[1, 2], [3, 4]]),
    (1, [[5, 6], [7, 8]]),
    (2, [[9, 10], [11, 12]])
]

assert mojEnumerate(lista3D) == wynik10
assert mojEnumerate(lista3D) == list(enumerate(lista3D))


listaMix: List = [[1], "abc", {"x": 1}, [2, 3], 999]
wynik11: List[Tuple[int, object]] = [
    (0, [1]),
    (1, "abc"),
    (2, {"x": 1}),
    (3, [2, 3]),
    (4, 999)
]

assert mojEnumerate(listaMix) == wynik11
assert mojEnumerate(listaMix) == list(enumerate(listaMix))




print("Nuda")
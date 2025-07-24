from typing import List, Tuple

def implementowanieZipa(words3: List, words4: List) -> List[Tuple]:
    print(f"words3: ${words3},   words4 ${words4}")
    
    listaKtoraZWroce: List[Tuple] = []

    lenka: int = len(words3)
    lenka2: int  = len(words4)

    # if lenka2 < lenka:
    #     mos = lenka2
    # else:
    #     mos = lenka

    mos = lenka2 if lenka2 < lenka else lenka

    for i in range(mos):
        # sth1: bool = i == lenka
        # sth2: bool = i == lenka2
        # if sth1 or sth2:
        #     break
            
        
        slowo = words3[i]    
        slowo2 = words4[i]
        
        # czy dany i jest w liście
        
        opakowanie: Tuple = (slowo, slowo2)
        listaKtoraZWroce.append(opakowanie)
          
    
    # zmiennaMatiego: List[Tuple[List]] = [(listaKtoraZWroce)]
    print(f"listaKtoraZWroce: ${listaKtoraZWroce}")
    print("")
    return listaKtoraZWroce

# 1. wyciagnac pierwszy element z pierwszej listy i drugiej listy $
# 2. opakowujemy te 2 elementy w Tuple $
# 3. dodajemy tego Tupla do listy $
# 4. wykonujemy dla kazdego nastepnego elementu jak w krokach 1-3 $
# 5. Zwrocenie powstales listy z tuplami $
# 6. chcemy aby były pary w elementach, ale jeśli będzie jeden element nie będzie miał pary to nie dodajemy to Tuply

    

words: List[str] = ["app1", "app3", "app5"]
words2: List[str] = ["app2", "app4", "app6"]
zip1 = zip(words, words2)
zastepstwoZaZip1 = zip(words, words2)

wynik: List[Tuple[str, str]] =[("app1", "app2"), ("app3", "app4"), ("app5", "app6")]
assert list(zip1) == wynik

assert implementowanieZipa(words, words2) == wynik

assert list(zastepstwoZaZip1) == implementowanieZipa(words, words2)

words5: List[str] = ["app7", "app9", "app11"]
words6: List[str] = ["app8", "app10", "app12", "okjuh"]

wynik2: List[Tuple[str, str]] = [("app7", "app8"), ("app9", "app10"), ("app11", "app12")]
zip2: List[Tuple[str, str]] = implementowanieZipa(words5, words6)
assert zip2 == wynik2

assert zip2 == list(zip(words5, words6))

wynik3: List[Tuple[str, str]] = [("app8", "app7"), ("app10", "app9"), ("app12", "app11")]
mojZip3: List[Tuple[str, str]] = implementowanieZipa(words6, words5)
assert mojZip3 == wynik3

listaIntow1: List[int] = [1, 2, 3]
listaIntow2: List[int] = [4, 5, 6]
wynik4: List[Tuple[int, int]] = [(1, 4), (2, 5), (3, 6)]
mojZip4: List[Tuple[str, str]] = implementowanieZipa(listaIntow1, listaIntow2)
assert mojZip4 == wynik4

assert mojZip4  == list(zip(listaIntow1, listaIntow2))

mieszanaLista1: List = [1, "lol", 2, "lolka"]
mieszanaLista2: List = ["mom", 3, 4, "lel"]
wynik5: List[Tuple] = [(1, "mom"), ("lol", 3), (2, 4), ("lolka", "lel")]
mojZip5: List[Tuple] = implementowanieZipa(mieszanaLista1, mieszanaLista2)
assert mojZip5 == wynik5

assert mojZip5 == list(zip(mieszanaLista1, mieszanaLista2))

pustaLista1: List = []
pustaLista2: List = []
wynik6: List[Tuple] = []
mojZip6: List[Tuple] = implementowanieZipa(pustaLista1, pustaLista2)
assert mojZip6 == wynik6

assert mojZip6 == list(zip(pustaLista1, pustaLista2))


jakasLista: List = ["lol", "cosiek"]
wynik7: List[Tuple] = []
mojZip7: List[Tuple] = implementowanieZipa(pustaLista1, jakasLista)
assert mojZip7 == wynik7

assert mojZip7 == list(zip(jakasLista, pustaLista1))

lista2D1: List[List] = [[1, 2], [3, 4], [5, 6]]
lista2D2: List[List] = [[7, 8], [9, 10], [11, 12]]

mojzip8: List[Tuple] = [
    ([1, 2], [7, 8]),
    ([3, 4], [9, 10]),
    ([5, 6], [11, 12])
]

assert implementowanieZipa(lista2D1, lista2D2) == mojzip8
assert implementowanieZipa(lista2D1, lista2D2) == list(zip(lista2D1, lista2D2))

lista2D3: List[List] = [[1, 2], [3, 4], [5, 6]]
lista2D4: List[List] = [[7, 8], [9, 10]]

mojzip9: List[Tuple] = [
    ([1, 2], [7, 8]),
    ([3, 4], [9, 10])
]

assert implementowanieZipa(lista2D3, lista2D4) == mojzip9
assert implementowanieZipa(lista2D3, lista2D4) == list(zip(lista2D3, lista2D4))

lista3D1: List[List[List]] = [
    [[1, 2], [3, 4]],
    [[5, 6], [7, 8]],
    [[9, 10], [11, 12]]
]

lista3D2: List[List[List]] = [
    [[13, 14], [15, 16]],
    [[17, 18], [19, 20]],
    [[21, 22], [23, 24]]
]

wynik3D: List[Tuple] = [
    (
        [[1, 2], [3, 4]],
        [[13, 14], [15, 16]]
    ),
    (
        [[5, 6], [7, 8]],
        [[17, 18], [19, 20]]
    ),
    (
        [[9, 10], [11, 12]],
        [[21, 22], [23, 24]]
    )
]

assert implementowanieZipa(lista3D1, lista3D2) == wynik3D
assert implementowanieZipa(lista3D1, lista3D2) == list(zip(lista3D1, lista3D2))

mieszana1: List = [[1, 2], "hello", {"klucz": "wartosc"}]
mieszana2: List = [["a", "b"], 123, {"x": "y"}]

wynikMix: List[Tuple] = [
    ([1, 2], ["a", "b"]),
    ("hello", 123),
    ({"klucz": "wartosc"}, {"x": "y"})
]

assert implementowanieZipa(mieszana1, mieszana2) == wynikMix
assert implementowanieZipa(mieszana1, mieszana2) == list(zip(mieszana1, mieszana2))

print("Nuda")


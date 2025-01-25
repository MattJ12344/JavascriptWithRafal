with open("nieparzysta.txt", "r") as file:
    zestawy = [int(line.strip()) for line in file.readlines()]

nowe_zestawy = []

for karty in zestawy:
    if karty % 2 == 1: 
        nowe_zestawy.append(karty * 5)
    else: 
        nowe_zestawy.append(karty // 2)

print("; ".join(map(str, nowe_zestawy)))
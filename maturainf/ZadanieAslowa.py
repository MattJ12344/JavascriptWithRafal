wynik = 0

with open("slowa.txt", "r", encoding='utf-8') as f:
    for line in f:
        if line.count("a") > 3:
            wynik += 1

print (wynik)
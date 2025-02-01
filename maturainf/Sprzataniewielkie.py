with open("out.txt", "w", encoding='utf-8') as w:
    with open("wielkie_sprzatanie.txt", "r", encoding='utf-8') as f:
        for line in f:
            l = [x.strip() for x in line.split()]
            imie = l[0].capitalize()
            prezent = " ".join(l[1:-1]).capitalize()
            cena = l[-1].replace("_", "")
            w.write(imie + ": " + prezent + ", " + cena + "\n")
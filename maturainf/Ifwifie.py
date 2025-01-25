def sprawdz_liczbe(x):
    if x < 40:
        if x % 4 == 0:
            return "Jestem mała i dzielę się przez 4"
        else:
            return "Jestem mała i nie dzielę się przez 4"
    else:
        if x % 4 == 0:
            return "Jestem duża i dzielę się przez 4"
        else:
            return "Jestem duża i nie dzielę się przez 4"

wyniki = [sprawdz_liczbe(8894), sprawdz_liczbe(36)]

print("; ".join(wyniki))
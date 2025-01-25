def oblicz_ocene(p, k):

    w = (p / 100) ** k

    if w >= 0.95:
        return 6
    elif w >= 0.85:
        return 5
    elif w >= 0.75:
        return 4
    elif w >= 0.5:
        return 3
    elif w >= 0.4:
        return 2
    else:
        return 1
        
dane = [
    (20, 0.5),
    (31, 0.3),
    (49, 0.2),
    (89, 1.5)
]

oceny = [str(oblicz_ocene(p, k)) for p, k in dane]

print("; ".join(oceny))
with open("gwiazda_czy_plus.txt", "w") as file:
    file.write("1 3\n787 28\n394 21\n-1 -4\n123 35")

with open("gwiazda_czy_plus.txt", "r") as file:
    lines = file.readlines()

pairs = [list(map(int, line.split())) for line in lines]
maxima = [max(x + 10, y ** 2) for x, y in pairs]

result = ";".join(map(str, maxima))
print(result)
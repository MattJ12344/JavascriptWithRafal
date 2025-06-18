def loop_division(dividend, divisor):
    if divisor == 0:
        print("dzielenie przez 0 nie jest możliwe")
        return
    quotient = 0
    while dividend >= divisor:
        dividend -= divisor
        quotient += 1
    return quotient

with open("Danedozdebugowania.txt", "r") as f:
    content = f.read()

lines = content.split("\n")
pairs = []
for pair in lines:
    pairs.append(pair.split())
pairs.pop()

for pair in pairs:
    dividend = int(pair[0])
    divisor = int(pair[1])
    print(dividend, divisor, loop_division(dividend, divisor))
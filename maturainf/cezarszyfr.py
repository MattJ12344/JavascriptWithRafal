klucz = 5

zaszyfrowany = "hjefw"
oryginalny = ""

for i in zaszyfrowany:
    odl_od_a = (ord(i) - ord('a') - klucz + 26) % 26
    oryginalny += chr(ord('a') + odl_od_a)
    
print(oryginalny)
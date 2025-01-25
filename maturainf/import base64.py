import base64

klucz_hex = "584b51f48bca9572acd08d378362"
zaszyfrowana_hex = "2e2e3f9dabbcfc16c5f0fb5ee00b"

klucz = int(klucz_hex, 16)
zaszyfrowana = int(zaszyfrowana_hex, 16)

wynik = klucz ^ zaszyfrowana

wynik_hex = hex(wynik)[2:].upper()


if len(wynik_hex) % 2 != 0:
    wynik_hex = '0' + wynik_hex

odszyfrowana_wiadomosc = base64.b16decode(wynik_hex)

odszyfrowana_wiadomosc.decode("utf-8")

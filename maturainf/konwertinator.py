def konwertinator():
    with open('liczby.txt', 'r') as file:
        numbers = [line.strip() for line in file if line.strip()]

    hex_num = hex(int(numbers[0].strip()))[2:].upper()
    
    octal_num = oct(int(numbers[1].strip()))[2:]
    
    binary_num = bin(int(numbers[2].strip()))[2:]

    return f"{hex_num};{octal_num};{binary_num}"

print(konwertinator())
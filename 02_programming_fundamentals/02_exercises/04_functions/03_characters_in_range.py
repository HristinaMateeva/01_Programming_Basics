def characters_in_range(symbol_1, symbol_2):
    for index in range(ord(first_symbol) + 1, ord(second_symbol)):
        result.append(chr(index))
    print(" ".join(result))


first_symbol = input()
second_symbol = input()

result = []

characters_in_range(first_symbol, second_symbol)

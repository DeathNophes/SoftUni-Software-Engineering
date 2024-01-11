text = input()
unique_symbols = set(text)
for symbol in sorted(unique_symbols):
    count = text.count(symbol)
    print(f"{symbol}: {count} time/s")
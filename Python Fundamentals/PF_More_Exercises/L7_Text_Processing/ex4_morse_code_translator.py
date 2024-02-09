morse_code = {
    ".-": 'A', "-...": "B", "-.-.": "C",
    "-..": "D", ".": "E", "..-.": "F",
    "--.": "G", "....": "H", "..": "I",
    ".---": "J", "-.-": "K", ".-..": "L",
    "--": "M", "-.": "N", "---": "O",
    ".--.": "P", "--.-": "Q", ".-.": "R",
    "...": "S", "-": "T", "..-": "U",
    "...-": "V", ".--": "W", "-..-": "X",
    "-.--": "Y", "--..": "Z"
}

output = ""

text = input().split(" | ")
for current_word in text:
    symbols = current_word.split()
    for symbol in symbols:
        output += morse_code[symbol]
    output += " "

print(output)
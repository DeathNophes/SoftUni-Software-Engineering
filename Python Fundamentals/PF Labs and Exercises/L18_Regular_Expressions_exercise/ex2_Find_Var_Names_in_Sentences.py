import re

sentence = input()
pattern = r'\b_{1}([A-Za-z]+)\b'

result = re.findall(pattern, sentence)
print(",".join(result))

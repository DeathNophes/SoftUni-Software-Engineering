import re

text = input()

title_pattern = r"<title>([^<>]*)</title>"
title = re.findall(title_pattern, text)
title = ''.join(title)
print(f"Title: {title}")

body_pattern = r"<body>.*<\/body>"
body = re.findall(body_pattern, text)
body = ''.join(body)

content_pattern = r">([^><]*)<"
content = re.findall(content_pattern, body)
content = ''.join(content)

print(f"Content: {content}")
n = int(input())
for i in range(0, n):
    for j in range(0, n):
        for k in range(0, n):
            print(f"{chr(97 + i)}"
                  f"{chr(97 + j)}"
                  f"{chr(97 + k)}")

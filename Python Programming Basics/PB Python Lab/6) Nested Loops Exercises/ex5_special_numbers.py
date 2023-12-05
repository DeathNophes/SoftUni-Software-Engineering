n = int(input())
                            # 1111 -> 9999
for i in range(1, 10):
    for j in range(1, 10):
        for k in range(1, 10):
            for l in range(1, 10):
                is_valid = n % i == 0 and n % j == 0 and n % k == 0 and n % l == 0
                # правим булева променлива, за да разберем кои числа са специални
                if is_valid:
                    print(f"{i}{j}{k}{l}", end=" ")
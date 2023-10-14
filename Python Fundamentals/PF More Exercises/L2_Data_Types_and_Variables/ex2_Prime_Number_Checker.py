def is_prime(some_number: int):
    prime_counter = 0
    for i in range(1, some_number + 1):
        if some_number % i == 0:
            prime_counter += 1
    if prime_counter == 2:
        return True
    return False


number = int(input())
print(is_prime(number))
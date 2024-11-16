def odd(n):
    odd_numbers = []
    for i in range(1, n + 1):
        if i % 2 != 0:
            odd_numbers.append(i)
    return odd_numbers

def even(n):
    even_numbers = []
    for i in range(1, n + 1):
        if i % 2 == 0:
            even_numbers.append(i)
    return even_numbers

def prime_number(n):
    prime = []
    for i in range(2, n + 1):
        is_prime = True
        for j in range(2, int(i ** 0.5) + 1):
            if i % j == 0:
                is_prime = False
                break
        if is_prime:
            prime.append(i)
    return ', '.join(map(str, prime))



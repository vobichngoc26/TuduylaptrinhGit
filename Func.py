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
    prime_numbers = []
    for i in range(1,n+ 1):
        if is_prime(i):
            prime_numbers.append(i)
    return prime_numbers

def is_prime(n):
    if n<= 1:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n% i == 0:
            return False
    return True

# https://projecteuler.net/problem=16

def sum_of_digits(n: int) -> int:
    sum = 0
    while n != 0:
        last = n % 10
        sum += last
        n //= 10
    return sum

print(sum_of_digits(2**1000))
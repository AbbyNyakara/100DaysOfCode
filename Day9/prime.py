# Write a program that takes a number as an input and checks whether its a prime/no

def prime_checker(num):
    is_prime = True
    for i in range(2, num):
        if num % i == 0:
            is_prime = False
    if is_prime:
        print(f"{num} is prime")
    else:
        print(f"{num} is not prime")


prime_checker(6)

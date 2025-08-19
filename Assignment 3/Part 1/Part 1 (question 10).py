def is_prime(number):
    if number <= 1:
        return False
    for i in range(2, int(number ** 0.5) + 1):
        if number % i == 0:
            return False
    return True
print(is_prime(2))   # Output: True
print(is_prime(15))  # Output: False
print(is_prime(17))  # Output: True
print(is_prime(1))   # Output: False

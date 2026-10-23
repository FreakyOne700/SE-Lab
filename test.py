def is_prime(num):
    if num < 2:
        return False
    if num == 2:
        return True
    if num % 2 == 0:
        return False

    divisor = 3
    while divisor * divisor <= num:
        if num % divisor == 0:
            return False
        divisor += 2
    return True


def nth_prime(n):
    if n < 1:
        raise ValueError("n must be a positive integer")

    count = 0
    candidate = 2

    while True:
        if is_prime(candidate):
            count += 1
            if count == n:
                return candidate
        candidate += 1


if __name__ == "__main__":
    user_input = int(input("Enter n: "))
    print(f"The {user_input}th prime number is {nth_prime(user_input)}")

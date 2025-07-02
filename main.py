def is_prime(n):
    if n <= 1:
        return False
    if n == 2:
        return True
    if n % 2 == 0:
        return False
    for i in range(3, int(n ** 0.5) + 1, 2):
        if n % i == 0:
            return False
    return True

# a function that gets a divisor and returns a function that checks if a number is divisible by that divisor
def is_divisible_by(divisor):
    def check_divisibility(n):
        return n % divisor == 0
    return check_divisibility

if __name__ == "__main__":
    num = int(input("Enter a number: "))
    if is_prime(num):
        print(f"{num} is a prime number.")
    else:
        print(f"{num} is not a prime number.")
    for i in range(2, int(num/2) + 1):
        divisible_by_i = is_divisible_by(i)
        if divisible_by_i(num):
            print(f"{num} is divisible by {i}.")
        else:
            print(f"{num} is not divisible by {i}.")
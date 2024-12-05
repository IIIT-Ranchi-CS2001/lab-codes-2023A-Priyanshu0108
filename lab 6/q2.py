import random
import math
import matplotlib.pyplot as plt

def generate_random_numbers(k, n):
    """Generate a list of k random numbers within the range 1 to n."""
    return random.sample(range(1, n+1), k)

def is_prime(num):
    """Check if a number is prime."""
    if num < 2:
        return False
    for i in range(2, int(math.sqrt(num)) + 1):
        if num % i == 0:
            return False
    return True

def separate_numbers(numbers):
    """Separate the numbers into prime and composite lists."""
    primes = [num for num in numbers if is_prime(num)]
    composites = [num for num in numbers if not is_prime(num) and num > 1]
    return primes, composites

# User inputs
k = int(input("Enter the number of random numbers (minimum 10): "))
n = int(input("Enter the upper limit for random numbers: "))
if k < 10:
    raise ValueError("Minimum value for K is 10.")

# Generate random numbers
random_numbers = generate_random_numbers(k, n)

# Separate into primes and composites
primes, composites = separate_numbers(random_numbers)

# Calculate squares of primes and square roots of composites
prime_squares = [num ** 2 for num in primes]
composite_roots = [math.sqrt(num) for num in composites]

# Plotting
fig, axes = plt.subplots(1, 2, figsize=(12, 6))

# Prime numbers vs their squares
axes[0].scatter(primes, prime_squares, color='blue', label='Prime Squares')
axes[0].set_title("Prime Numbers vs Their Squares")
axes[0].set_xlabel("Prime Numbers")
axes[0].set_ylabel("Squares")
axes[0].legend()

# Composite numbers vs their square roots
axes[1].scatter(composites, composite_roots, color='green', label='Composite Square Roots')
axes[1].set_title("Composite Numbers vs Their Square Roots")
axes[1].set_xlabel("Composite Numbers")
axes[1].set_ylabel("Square Roots")
axes[1].legend()

plt.tight_layout()
plt.show()

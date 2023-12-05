import math

def compute_pi(n):
    """Compute n digits of Pi using a series expansion."""
    pi_estimate = sum(1/math.factorial(i) * math.factorial(2 * i) / (2**(2 * i + 1) * math.factorial(i)**2) for i in range(n))
    return pi_estimate * 2

def main():
    # Ask the user for the number of terms to use in the computation
    num_terms = int(input("Enter the number of terms for Pi computation: "))

    # Compute Pi
    pi_estimate = compute_pi(num_terms)

    # Print the result
    print(f"Pi estimated with {num_terms} terms is: {pi_estimate}")

if __name__ == "__main__":
    main()

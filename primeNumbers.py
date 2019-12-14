# A prime number is only evenly divisible by itself and 1.

# Note that 1 is not a prime number.
# create a function that generates prime numbers.


def is_prime_num(num):
	"""Checks whether a number is a prime number"""
	div_count = 0

	for i in range(1, num+1):
		if num%i == 0:
			div_count += 1

	if div_count == 2:
		return True

	return False


def primeNumbers(end):
	if type(end) not in [int]:
		raise TypeError("Only integers apply")

	return [i for i in range(end+1) if is_prime_num(i)]

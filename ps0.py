# 0. Write a boolean function that takes in a positive integer or zero as a parameter and 
#    returns whether the number is odd or even.

def even_or_odd(integer):
	
	"""Returns if integer is even or odd"""
	
	if integer % 2 == 0:
		return True
	else:
		return False	


# 1. Write a function that takes a non-negative integer as a parameter and returns the 
#    number of digits in it.
#	"""Returns number of digits"""
def number_digits(integer):

	"""Returns number of digits in integer"""

	
	digits = 0
	while integer >= 1:
		digits += 1
		integer = integer/10
	return digits
	
	


# 2. Write a function that takes a non-negative integer as a parameter and returns the 
#    sum of its digits.

"""Returns the sum of its digits."""

def sum_digits(integer):

	r = 0 
	while integer:
		r += integer % 10
		integer //= 10
	return r


# 3.  Write a function that takes a non-negative integer as a parameter and returns the 
#     sum of all the integers that are less than the given number.
#     For example: sum_less_ints(3) → 3, which is 1 + 2
#     sum_less_ints(5) → 10, which is 1 + 2 + 3 + 4

def sum_less(integer):
	
	count = 0
	while count < integer:
		count+=1
		adding += count



# 4  Write a function that takes a non-negative integer as a parameter and returns its factorial.
#    For example: factorial(3) → 6, which is 3!
#    factorial(5) → 120, which is 5!

def factorial(n):
    number = 1
    while n >= 1:
        number = number * n
        n = n - 1
    return number

# 5  Write a boolean function that takes two positive integers as parameters and figures 
# out whether the second number is a factor the first. In other words, returns true if 
# the second number divides into the first number evenly, and false otherwise.

def find_factor(bigger, smaller):

	return bigger % smaller == 0



# 6  Write a boolean function that takes a positive integer as a parameter and returns 
#    whether the number is a prime.

def is_prime(number):

	count = 2
	while count < number:
		if number % count == 0:
			return False
		count += 1
	return True
		


# 7  Write a boolean function that takes a positive integer as a parameter and returns 
#    whether the number is perfect. A perfect number is a number that equals the sum of 
#    proper its proper factors. A proper factor is any factor except the number itself.  
#    For example: isPerfect(6) → True, because 6 = 1 + 2 + 3.

def is_perfect(number):

	total = 0
	for item in range(1, number):
		if number % item == 0:
			total += item
	return number == total
			

# 8  Write a boolean function that takes a positive integer as a parameter and returns 
#    true if the sum of the digits of the number divides evenly into the number, false 
#    otherwise. You MUST call the sumDigits function you wrote in question 2 to define 
#    this function

def sum_divisible (number):

	sum = sum_digits(number)
	return number % sum == 0
	



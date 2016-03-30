import ps0

#0 - even or odd
#DONE
print("The number 7 is even: {} ".format(ps0.even_or_odd(7)))
print("The number 8 is even: {} ".format(ps0.even_or_odd(8)))
print("The number 0 is even: {} ".format(ps0.even_or_odd(0)))

#1 - number of digits
#DONE
print("0 has {} digits".format(ps0.number_digits(0)))
print("3 has {} digits".format(ps0.number_digits(3)))
print("34 has {} digits".format(ps0.number_digits(34)))
print("345 has {} digits".format(ps0.number_digits(345)))

#2 - sum of digits
#DONE

print("The sum of the digits of 0 is {}".format(ps0.sum_digits(0)))
print("The sum of the digits of 1 is {}".format(ps0.sum_digits(1)))
print("The sum of the digits of 12 is {}".format(ps0.sum_digits(12)))
print("The sum of the digits of 123 is {}".format(ps0.sum_digits(123)))
print("The sum of the digits of 1239 is {}".format(ps0.sum_digits(1239)))


#3 - sum of preceeding
#TODO

print("The sum of all integers less than 14 is {}".format(ps0.sum_less(14)))
print("The sum of all integers less than 17 is {}".format(ps0.sum_less(17)))
print("The sum of all integers less than 0 is {}".format(ps0.sum_less(0)))
print("The sum of all integers less than 3 is {}".format(ps0.sum_less(3)))




#4 - factorial
#DONE
print("The factorial of 5 is {}".format(ps0.factorial(5)))
print("The factorial of 4 is {}".format(ps0.factorial(4)))



#5 - factor
#DONE
print("3 is a factor of 18: {}".format(ps0.find_factor(18, 3)))
print("4 is a factor of 18: {}".format(ps0.find_factor(18, 4)))

#6 - prime
#DONE

print("9 is prime: {}".format(ps0.is_prime(6)))
print("13 is prime: {}".format(ps0.is_prime(13)))

#7 - perfect
#DONE

print("6 is perfect: {}".format(ps0.is_perfect(6)))
print("7 is perfect: {}".format(ps0.is_perfect(7)))
print("8 is perfect: {}".format(ps0.is_perfect(8)))



#8 - sum divisible
#DONE

print("The number 18 is divisible by {}. {}".format(ps0.sum_digits(18), ps0.sum_divisible(18)))
print("The number 35 is divisible by {}. {}".format(ps0.sum_digits(35), ps0.sum_divisible(35)))

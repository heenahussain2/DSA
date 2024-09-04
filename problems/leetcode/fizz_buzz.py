"""
Challenge: Fizz Buzz
write a program that counts from 1 to 100.
For each number:
If the number is a multiple of 3, print "Fizz".
If the number is a multiple of 5, print "Buzz".
If the number is a multiple of both 3 and 5, print "FizzBuzz".
Otherwise, print the number itself.
"""
for i in range(1, 101):
    if i % 3 == 0 and i % 5 == 0:
        print("Fizz Buzz", end=", ")
    elif i % 3 == 0:
        print("Fizz", end=", ")
    elif i % 5 == 0:
        print("Buzz", end=", ")
    else:
        print(i, end=", ")

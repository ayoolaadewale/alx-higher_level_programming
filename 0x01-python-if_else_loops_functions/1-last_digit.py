#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)

num_converted = str(number)

if number < 0:
    last = int(num_converted[len(num_converted)-1]) * -1
else:
    last = int(num_converted[len(num_converted)-1])

if last < 6 and last != 0:
    print('Last digit of', number, 'is', last, 'and is less than 6 and not 0')
elif last == 0:
    print('Last digit of', number, 'is', last, 'and is 0')
else:
    print('Last digit of', number, 'is', last, 'and is greater than 5')

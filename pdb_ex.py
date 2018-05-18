import sys
import pdb
from random import choice

random1 = list(range(1, 13))
random2 = list(range(1, 13))

while True:
    print("To exit this game type 'exit'")

    pdb.set_trace()

    num1 = choice(random1)
    num2 = choice(random2)

    answer = int(input("Product of {} times {}: ".format(num1, num2)))

    product = num1 * num2

    if answer == 'exit':
        print("Exiting game!")
        sys.exit()
    elif answer == product:
        print("Correct!")
    else:
        print("Wrong!")

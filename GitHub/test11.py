# print()
# input()
# len()
# type()

# for
# while

# if, elif, else

# import random

# x = random.randint(1,100)

# print(x)

import random
botThrow = random.randint(1,6)
yourThrow = random.randint(1,6)
print(botThrow)
print(yourThrow)
if botThrow > yourThrow:
    print("You lost")
elif botThrow == yourThrow:
    print("Draw")
else:
    print("You won")
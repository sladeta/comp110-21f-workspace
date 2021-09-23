"""Program that outputs one of at least four random, good fortunes."""

__author__ = "730236019"

# The randint function is imported from the random library so that
# you are able to generate integers at random.
# 
# Documentation: https://docs.python.org/3/library/random.html#random.randint
#
# For example, consider the function call expression: randint(1, 100)
# It will evaluate to an int value >= 1 and <= 100. 
from random import randint
i: int = int(randint(1, 4))
print("Your fortune cookie says...")
if i == 4: 
    print("A beautiful, smart, and loving person will be coming into your life.")
else:
    if i == 3:
        print("A lifetime of happiness lies ahead of you.")
    else:
        if i == 2:
            print("A light heart carries you through all the hard times. ")
        else:
            print("A smile is your personal welcome mat.")
print("Now, go spread positive vibes!")
"""An exercise in remainders and boolean logic."""

__author__ = "730236019"

n: int = int(input("Enter an int: "))


if ((n % 2 == 0) and (n % 7 == 0)):
    print("TAR HEELS")
else:
    if n % 2 == 0:
        print("TAR")
    else:
        if n % 7 == 0:
            print("HEELS")
        else:
            print("CAROLINA")
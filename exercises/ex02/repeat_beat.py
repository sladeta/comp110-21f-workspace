"""Repeating a beat in a loop."""

__author__ = "730236019"

beat: str = input("What beat do you want to repeat? ")
times: int = int(input("How many times do you want to repeat it? "))
i: int = 0
str_print: str = ""


if times <= 0:
    print("No beat...")
else:
    while i < times: 
        str_print = str_print + beat
        if i < times - 1:
            str_print = str_print + " "
        i = i + 1
    print(str_print)
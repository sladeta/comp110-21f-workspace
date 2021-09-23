"""Counting letters in a string."""

__author__ = "730236019"

letter: str = str(input("What letter do you want to search for?: "))
word: str = str(input("Enter a word: "))
i: int = 0
v: int = len(word)
count: int = 0

while i < v:
    if word[i] == letter:
        count = count + 1
    i = i + 1
print("Count: " + str(count))
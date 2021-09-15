"""Finding duplicate letters in a word."""

__author__ = "730236019"

word: str = input("Enter a word: ")
i: int = 0
h: int = 0
answer: bool = False
ch: str

while i < len(word):
    ch = word[i]
    while ((h < len(word)) and (i != h)): 
        if(ch == word[i]):  
            response = True
        h += 1
    h = 0
    i += 1
final_answer: str = str(answer)

print("Found Duplicate: " + final_answer)
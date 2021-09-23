"""Finding duplicate letters in a word."""

__author__ = "730236019"

word: str = input("Enter a word: ")
i: int = 0
answer: bool = False
ch: str

while i < len(word):
    ch = word[i]
    h: int = 0
    while ((h < len(word)) and (h != i)): 
        if(ch == word[h]):  
            answer = True
        h += 1
    i += 1
final_answer: str = str(answer)

print("Found duplicate: " + final_answer)
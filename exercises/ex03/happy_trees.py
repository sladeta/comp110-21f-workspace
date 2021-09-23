"""Drawing forests in a loop."""

__author__ = "730236019"

# The string constant for the pine tree emoji
TREE: str = '\U0001F332'
depth: int = int(input("Depth: "))
i: int = 0
str_print: str = ""

while(depth > 0 and depth != i):
    if i < depth: 
        str_print = TREE + str_print
        print(str_print)
    i += 1
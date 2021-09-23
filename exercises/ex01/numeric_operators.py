"""Program evaluates different numeric operators."""

__author__ = "730236019"

left_hand_side: int = int(input("Left-hand side: "))
right_hand_side: int = int(input("Right-hand side: "))
power: int = left_hand_side ** right_hand_side
division: float = left_hand_side / right_hand_side
floor_division: int = left_hand_side // right_hand_side
percentage: int = left_hand_side % right_hand_side

print(str(left_hand_side) + " ** " + str(right_hand_side) + " is " + str(power))
print(str(left_hand_side) + " / " + str(right_hand_side) + " is " + str(division))
print(str(left_hand_side) + " // " + str(right_hand_side) + " is " + str(floor_division))
print(str(left_hand_side) + " % " + str(right_hand_side) + " is " + str(percentage))
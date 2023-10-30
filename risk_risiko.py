import random
print("Red dices:")
red=[random.randint(1,6), random.randint(1,6), random.randint(1,6)]
red.sort()
print(str(red[0]) + "(N)")
print(str(red[1]) + "(M)")
print(str(red[2]) + "(O)")

print("Blue dices:")
blue=[random.randint(1,6), random.randint(1,6), random.randint(1,6)]
blue.sort()
print(str(blue[0]) + "(N)")
print(str(blue[1]) + "(M)")
print(str(blue[2]) + "(O)")

print("  R    B")
print("N " + str(red[0]) + " vs " + str(blue[0]) + " => " + ("red " if red[0] > blue [0] else "blue") + " wins")
print("M " + str(red[1]) + " vs " + str(blue[1]) + " => " + ("red " if red[1] > blue [1] else "blue") + " wins")
print("O " + str(red[2]) + " vs " + str(blue[2]) + " => " + ("red " if red[2] > blue [2] else "blue") + " wins")
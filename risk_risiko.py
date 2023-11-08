import random
MIN_NUMBER=1
MAX_NUMBER=6
DICE = ['N','M','O']

def Dice_roll() -> int: #Generate the random int
    return random.randint(MIN_NUMBER,MAX_NUMBER)

def print_army(army:list) -> None: #print the army
    for i in range (0,3):
        print(f"{army[i]} ({DICE[i]})")

def compare(red:int,blue:int) -> str: #Decide the winner
    return ("red" if red > blue else "blue")
    
def battle(red:list,blue:list) -> None: #print the result
    print("  R    B")
    for i in range (0,3):
        out = f"{DICE[i]} {red[i]} vs {blue[i]} => {compare(red[i],blue[i])} wins"
        print(out)

def print_battle(red:list,blue:list) -> None:
    red.sort()
    print("Red dices:") 
    print_army(red)
    
    blue.sort()
    print("Blue dices:") 
    print_army(blue)
    
    battle(red,blue)

def main():
    #red army
    red = [Dice_roll(), Dice_roll(), Dice_roll()]

    #blue army
    blue = [Dice_roll(), Dice_roll(), Dice_roll()]

    print_battle(red,blue)

if __name__ == "__main__":
    main()
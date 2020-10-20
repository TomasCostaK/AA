import random

def choose_number(lower_value,high_value) -> int:
    return random.randint(lower_value,high_value)

def play_game(lower_value: int=0, high_value:int=100) -> int:
    number = choose_number(lower_value,high_value)
    count = 1
    correct_number = False
    while not correct_number:

        guess = int(input("New number: "))
        assert( type(guess)==int )

        if guess==number:
            print("You got it right with %d tries!" % (count))
            return count

        elif guess > number:
            print("Too High")

        else: 
            print("Too low")

        count+=1

if __name__ == "__main__":
    count = play_game()
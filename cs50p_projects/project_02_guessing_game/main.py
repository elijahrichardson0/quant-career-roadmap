import random as r

def main():
    # Start the game
    while True:
        play = input("Welcome to my guessing game! Type 'play' to begin.")
        if play not in ["play"]:
            print("Please enter a valid input.")
        else:
            break

    # Pick a number between 1 and 100
    num = r.randint(1,100)
    print("I have picked a number between 1 and 100.")

    # Compare player guess to chosen number
    guessCount = 0
    while True:
        try:
            guess = int(input("What's my number?"))
            if guess not in range(1,101):
                print("Please enter a number between 1 and 100.")
            elif guess > num:
                guessCount += 1
                print("Too High!")
            elif guess < num:
                guessCount += 1
                print("Too low!")
            else:
                guessCount += 1
                print(f"Congratulations! You guessed my number, it was {num}. It took you {guessCount} guesses.")
                break
        except:
            print("Please enter a valid number.")
        
        

main()
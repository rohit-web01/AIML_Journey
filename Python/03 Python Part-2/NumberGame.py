magic_number = 7

while True :
    num = int(input("Enter your guess : "))
    if num < magic_number :
        print("Too Low! Try Again.")
    elif num > magic_number :
        print("Too High! Try Again.")
    else :
        print("Congratulations! You guessed it right.")
        break
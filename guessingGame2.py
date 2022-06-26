import random

random_number=random.randint(1,9)

guess_number=0




    
while guess_number != random_number:
    guess_number = int(input("Please guess the number between 1 and 9 : "))

    if(random_number < guess_number):
        print("The number is smaller than your number")
    elif(random_number > guess_number):
        print("The number is grater than your number")
    else:
        print("YOU WON!")   

chances =1
while chances < 5:
    print(chances)
    chances += 1

    if not chances < 5:
        print("YOU LOSE!!! The number was ", random_number)
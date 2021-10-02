import random

# r = random.randrange(-5, 11) #you cant get *10* here, if you wanna output 10 you do (-1,11)
# r = random.randint(-5, 10) here you can get 10
#print(r)

top = input("Type a number: ")

guesses = 0

if top.isdigit():
    top=int(top)
    if top <= 0:
        print("Please type a number larger than 0 next time! ")
        quit()
else:
    print("Please type a digit next time. ")
    quit()

r = random.randint(1, top)

while True:
    guesses += 1
    guess = input("Make a guess: ")
    if guess.isdigit():
        guess=int(guess)
    else:
        print("Please type a digit next time. ")
        continue

    if guess == r:
        print("You got it right! ")
        break
    else:
        hint = input("You got it wrong, Do you want a hint? Type yes or no: ")
        if hint.lower()=="yes":
            if guess < r:
                print("You were below the number! ")
            else:
                print("You were above the number! ")
        else:
            continue
print("You got it in", guesses ,"guesses! ")


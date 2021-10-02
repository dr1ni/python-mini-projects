print("Welcome to the quiz game!\n")

playing = input("Do you want to play? Type yes or no: ")

if playing.lower() != "yes":
    quit()
else:
        score = 0
        print("Okay! Lets play :) ")
        answer = input("What does CPU stand for? ")
        if answer.lower() == "central processing unit":
            print('Correct')
            score += 1
        else: 
            print('Incorrect')

        answer = input("What does GPU stand for? ")
        if answer.lower() == "graphics processing unit":
            print('Correct')
            score += 1
        else: 
            print('Incorrect')
        answer = input("What does PC stand for? ")
        if answer.lower() == "personal computer":
            print('Correct')
            score += 1
        else: 
            print('Incorrect')

        answer = input("What does RAM stand for? ")
        if answer.lower() == "random access memory":
            print('Correct')
            score += 1
        else: 
            print('Incorrect')
        if str(score) == "0":
            print("You got " + str(score) + " questions right :( ")
        else:
            print("You got " + str(score) + " questions right! ") 
print("Welcome to my quiz !")

playing = input("Do you want to play? Y/N: ")
if playing.upper() !='Y':
    quit()

print("Okay! Let's play ;)")
score = 0

answer = input("What does EU stand for? ")
if answer.lower() == "european union":
    print("Correct!")
    score += 1
else:
    print("Incorrect!")

answer = input("What is the currency of the European union ?")
if answer.lower() == "euro":
    print("Correct!")
    score += 1
else:
    print("Incorrect!")

answer = input("How many countries are EU members? ")
if answer == "27":
    print("Correct!")
    score += 1

print("Thank you for playing!!!")
print(f"You got {score} questions correct!")
print(f"You got {(score / 3) * 100}%.")
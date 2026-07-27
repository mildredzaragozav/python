print("Welcome to quiz game!")
playing = input("Do you want to play? ")

if playing.casefold() != "yes":
    print("Bye!")
    quit()

print("Ok, let's play!")

score = 0;

answer = input("What does CPU stand for? ").casefold()
if answer == "central processing unit" : 
    print("Correct!")
    score += 1
else:
    print("Incorrect!")

answer = input("What does GPU stand for? ").lower()
if answer == "graphics processing unit" : 
    print("Correct!")
    score += 1
else:
    print("Incorrect!")

answer = input("What does RAM stand for? ").lower()
if answer == "random access memory" : 
    print("Correct!")
    score += 1
else:
    print("Incorrect!")

answer = input("What does PSU stand for? ").lower()
if answer == "power supply" : 
    print("Correct!")
    score += 1
else:
    print("Incorrect!")


print(f"Your score: {score}/4")
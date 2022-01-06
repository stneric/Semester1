import random


#every letter in the alphabet is guessable until it has already been guessed
everyletter = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]
guessable = []
alreadyguessed = ["a"]

#add letter to alreadyguessed
for i in range(0,len(everyletter)):
    check = everyletter[i]
    if check in alreadyguessed:
        i = i+1

    else:
        guessable.append(everyletter[i])

# print(guessable) check, if it worked
        
letter = random.choice(guessable)

print(f"is {letter} in the word?")
choice = input("y/n\n")

if choice == str("y"):
    
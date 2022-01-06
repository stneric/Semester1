import random

def cpuwins(life):
    print("I've won!!")
    #backtomenu

def cpuloses(life):
    print("I've lost :(")
    #backtomenu


def cpuguess(everyletter,guessable,alreadyguessed,progress,life):

    print(f"Life: {life}")

    if life == 0:
        cpuloses(life)
    
    else:
        pass

    #add letter to alreadyguessed
    for i in range(0,len(everyletter)):
        check = everyletter[i]
        if check in alreadyguessed:
            i = i+1

        else:
            guessable.append(everyletter[i])

    print(guessable) #check, if it worked
            
    letter = random.choice(guessable)

    print(f"is {letter} in the word?\n")
    choice = input("y/n\n")

    if choice == str("y"):
        alreadyguessed.append(letter)
        #check where the letter stands
        for i in range(0,len(tobeguessed)):
            if tobeguessed[i] == letter:
                progress[i] = letter

    elif choice == str("n"):
        alreadyguessed.append(letter)
        life = life-1


    print(f"so far: {progress}")

    if progress == tobeguessed:
        cpuwins(life)

    else:
        guessable = []  #set to empty again, for repopulation
        cpuguess(everyletter,guessable,alreadyguessed,progress,life)



guess = input("What word should be guessed?\n")
tobeguessed = list(guess)

#every letter in the alphabet is guessable until it has already been guessed
everyletter = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]
guessable = []
alreadyguessed = []
progress = ["_"] * len(tobeguessed)
life = 6

cpuguess(everyletter,guessable,alreadyguessed,progress,life)

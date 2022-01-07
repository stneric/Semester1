import random

def cpuwins(life, cpuguess, everyletter, guessable, alreadyguessed, progress):
    print(f"I've won!! with {life} lives remaining!")
    cpuguess(everyletter,guessable,alreadyguessed,progress,life)

def cpuloses(life, cpuguess, everyletter, guessable, alreadyguessed, progress):
    print("I've lost :(")
    cpuguess(everyletter,guessable,alreadyguessed,progress,life)

def errcheck(letter, life, alreadyguessed, tobeguessed, progress, cpuguess, everyletter, guessable):

    print(f"is {letter} in the word?\n")
    choice = input("y/n\n")

    if choice == str("y"):
        alreadyguessed.append(letter)
        #check where the letter is located
        for i in range(0,len(tobeguessed)):
            if tobeguessed[i] == letter:
                progress[i] = letter

    elif choice == str("n"):
        alreadyguessed.append(letter)
        life = life-1
        cpuguess(everyletter,guessable, alreadyguessed, progress, life)

    else:
        print("Invalid input!")
        return errcheck(letter, life, alreadyguessed, tobeguessed, progress, cpuguess, everyletter, guessable)


def logik(letter, life, alreadyguessed, tobeguessed, progress, cpuguess, everyletter, guessable):

    # 1 erster Buchstabe ist e
    # 2 wenn e nicht drin dann erratte n weil zweit haeufigster buchstabe
    # 3 wenn e und n nicht drin dann erratte i weil zweit haeufigster buchstabe
    # 4 wenn e und n und i drin ist, dann erratte r weil dritt haeufigster Buchstabe
    # 6 wenn e und n und i und t nicht drin sind, dann errate s weil fuenf haeufisgter Buchstabe
    

    # def ersteBuchtsbaenraten():
    #       while e, n i t r s der buchstabe e nicht drin dann nachster
    #       if eins von denen drin dann check mit der Bibliothek
    #       sgaen wenn input y dann check den buchtsabe und die STelle und dann 
    #       Moegliche Woerter  = [] wenn buchstabe an stelle dann append das in moegliche woerter
    #       


    letter = "e"
    errcheck(letter, life, alreadyguessed, tobeguessed, progress, cpuguess, everyletter, guessable)

    if letter in tobeguessed:
        
    check = input("is e part of your word? (y/n)")

    if check == str("y"):


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

    #print(guessable) #check, if it worked

    
    
    logik(letter)

   

    

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
life = 10

cpuguess(everyletter,guessable,alreadyguessed,progress,life)

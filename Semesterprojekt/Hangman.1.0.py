# 21.11.2021

# cloned

import random #random picks something from a list at random
import time
import os 

def intro():
    os.system('cls||clear')
    print("""\\  

    Welcome to 
    _                                             
    | |                                            
    | |__   __ _ _ __   __ _ _ __ ___   __ _ _ __  
    | '_ \ / _` | '_ \ / _` | '_ ` _ \ / _` | '_ \ 
    | | | | (_| | | | | (_| | | | | | | (_| | | | |
    |_| |_|\__,_|_| |_|\__, |_| |_| |_|\__,_|_| |_|
                        __/ |                      
                       |___/    Semesterprojekt Eric Stein

                 (1) Start Game
                 (2) Documentation                      
    """)

    eingabewahl()

def gamerules():
    print("\n")

    choice = (input("(1) Easy mode \t (2) Hard mode\n"))

    if choice == str(1):
        print("The Rules:\n")
        print("You've got 6 lives. Every time you guess wrong, one life is \n dedacted.\n If your lives reach zero, you lose\n Are you ready?\n")
        wahl = (input("(1) Yes (2) No\n"))
        life = 6


        if wahl == str(1):
            cpuvsyou(choice, life)

        else:
            gamerules()

    elif choice == str(2):
        print("The Rules:\n")
        print("You've got 4 lives. Every time you guess wrong, one life is \n dedacted.\n If your lives reach zero, you lose\n Are you ready?\n")
        wahl = (input("(1) Yes (2) No\n"))
        life = 4

        if wahl == str(1):
            cpuvsyou(choice, life)

        else:
            gamerules()

    else:
        print("Please pick one of the two options.")
        gamerules()

    
    #cpuvsyou(choice, life)

def youvscpu():

    alphabet = ["a"],["b"],["c"],["d"],["e"],["f"],["g"],["h"],["i"],["j"],["k"],["l"],["m"],["n"],["o"],["p"],["q"],["r"],["s"],["t"],["u"],["v"],["w"],["x"],["y"],["z"]

    word = input("Word to be guessed:")
    print(f"To be guessed: {word}")

    wordarr = list(word)

    guessin = []*len(word)

    wrong = []

    buchstabe = random.choice(alphabet)

    while guessin != wordarr:
    
        while buchstabe in wrong or buchstabe in wordarr and len(wrong) != len(alphabet):
            buchstabe = random.choice(alphabet)

        print("Is",buchstabe, "present in your word?")

        choose = (input("(1) Yes or (0) No?\n"))

        if choose == str(1):

            for i in range(0,len(word)):
                if wordarr[i] == buchstabe:

                    guessin[i] = buchstabe

            print(f"{guessin}")

        elif choose == str(0):
            wrong.append(buchstabe)
            print(f"wrong {wrong}")
                 
    print("You didn't choose an english word, did you?")
    
def cpuvsyou(choice, life):
    os.system('cls||clear')
    length = ""
    counter = 0

    

    if choice == str(1):
        words = ("pizza", "honig", "tastatur")

    elif choice == str(2):
        words = ("extravagant", "superkalefragelisischexpialidetisch")


    wort = random.choice(words)
    tobeguessed = wort

    tobeguessedarr = list(tobeguessed) #in ein array umwandeln um es lesbar zu machen mit buchstaben
    
    for i in tobeguessed:
        length = length + "_"
        counter = counter+1

    
    print("Word has", counter, "letters: ", length)
    #print(tobeguessedarr)       #weg machen 

    emptyarr = [""]*len(tobeguessed)

    guessing(tobeguessed, life, tobeguessedarr, length, emptyarr)     #6 Leben

def guessing(tobeguessed, life, tobeguessedarr,length, emptyarr):

       

    
        if life > 0:
            
            print("\n")
            guess = input("Pick a letter:")
            print("\n")

        else:
            gameover()

        #tobeguessed = []
        if guess == tobeguessed:
            celebration(life)

        else:
            pass

        

        if guess in tobeguessed:

            for i in range(0,len(tobeguessedarr)):
                
                if guess == tobeguessedarr[i]:
                    
                    # an der Stelle i soll emptyarr = buchstabe sein. 
                    # emptyarr[i] = guess
                    # print(emptyarr)
                    # ausserdem muss geprueft werden ob der buchstabe
                    # schon erraten wurde
                    # if guess in emptyarr: print("you've already got this one")
                    
                    print(guess, "is letter ", i+1)

                    buchstabe = tobeguessedarr[i]

                    if buchstabe in emptyarr[i]:
                        print("You've already guessed that one!")


                    else:
                        emptyarr[i] += buchstabe

                

            if emptyarr == tobeguessedarr:
                print("\n")
                print(emptyarr)
                print("\n")
                celebration(life)

            else:
                print(emptyarr)
                guessing(tobeguessed,life,tobeguessedarr, length, emptyarr)



    #    elif guess == tobeguessedarr:
    #        print(guess, "!!!")            wenn das ganze Wort erraten wird
    #        celebration(life)

        else:
            print(guess, "is not in the word")
            life = life-1
            print("Your current Health:\n", life)
            guessing(tobeguessed, life, tobeguessedarr, length, emptyarr)

def celebration(life):
    
    print("\n\t You Won!!\n")
    print("\tRemaining lives:", life)
    print("\n")

    backtomenu()
    
def backtomenu():
    wahl = str(input("...Press enter to return to main menu"))

    print("Returning\n")
    time.sleep(1)

    intro()

def spielstart():
    
    print("\n")

    wichtype = int(input("(1) CPU GUESSES \t (2) YOU GUESS\n"))

    if wichtype == 1:
        youvscpu()

    elif wichtype == 2:
        gamerules()

    else:
        print("Please pick one of the two options.\n")
        spielstart()

def dokumentation():
    os.system('cls||clear')
    print("Das gesamte Semesterprojekt finden Sie als PDF unter:")
    target = "https://www.eric-stein.de\n"
    print(target)

    backtomenu()

def eingabewahl():

    # Eingabe ueberpruefen, falls nicht 1 oder 2, erneut eingabe
    # abfragen
        
        wahl = (input(""))

        if wahl == str(1):
            return spielstart()


        elif wahl == str(2):
            return dokumentation()


        else:
            print("Please pick one of the two options.\n")
            eingabewahl()

def gameover():

    os.system('cls||clear')
    print("You've lost!")
    backtomenu()

intro()
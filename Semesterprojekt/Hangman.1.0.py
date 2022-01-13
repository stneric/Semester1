
import random #zufallsprinzip bei der Wahl von Worten
import time #um 
import os #fuer "clear" im Terminal 
import re #regex



def intro():
    os.system('cls||clear')
    print("""\


    Welcome to 
     _                                             
    | |                                            
    | |__   __ _ _ __   __ _ _ __ ___   __ _ _ __  
    | '_ \ / _` | '_ \ / _` | '_ ` _ \ / _` | '_  \ 
    | | | | (_| | | | | (_| | | | | | | (_| | | | |
    |_| |_|\__,_|_| |_|\__, |_| |_| |_|\__,_|_| |_|
                        __/ |                      
                       |___/    Semesterprojekt Eric Stein

                 (1) Start Game
                 (2) Documentation                      
    """)

    eingabewahl()

def gamerules():

    os.system('cls||clear')

    print("\n")

    choice = (input("(1) german mode \t (2) english mode\n"))

    if choice == str(1):
        print("\n")
        print("The Rules:\n")
        print("You've got 7 lives. Every time you guess wrong,")
        print("one life is dedacted.")
        print("If your lives reach zero, you lose.")
        print("\n")
        print("Are you ready?")
        
        wahl = (input("(1) Yes (2) No\n"))
        life = 7


        if wahl == str(1):
            cpuvsyou(choice, life)

        else:
            gamerules()

    elif choice == str(2):
        print("\n")
        print("The Rules:\n")
        print("You've got 9 lives. Every time you guess wrong,")
        print("one life is dedacted.")
        print("If your lives reach zero, you lose.")
        print("\n")
        print("Are you ready?")

        wahl = (input("(1) Yes (2) No\n"))
        life = 9

        if wahl == str(1):
            cpuvsyou(choice, life)

        else:
            gamerules()

    else:
        print("Please pick one of the two options.")
        gamerules()

    
    #cpuvsyou(choice, life)

def cpuwins(life):
    os.system('cls||clear')
    print("I've won!!")
    backtomenu()

def cpuloses(life):
    os.system('cls||clear')
    print("I've lost :(")
    backtomenu()

def cpuguess(everyletter,guessable,alreadyguessed,progress,life,tobeguessed):

    os.system('cls||clear')
    print(f"Lives remaining: {life}\n")

    #check, how many lives are left. If lives reach below 1, the CPU lost
    if life == 0:
        cpuloses(life)
    
    else:
        pass

    #check, 
    for i in range(0,len(everyletter)):
        check = everyletter[i]
        if check in alreadyguessed:
            i = i+1

        else:
            guessable.append(everyletter[i])


    # print(guessable) #check, if it worked (it did :D)       
    letter = random.choice(guessable)

    print(f"so far: {progress}")

    # question the user as to if the guessed letter is part of the word, they chose
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


    if progress == tobeguessed:
        cpuwins(life)

    else:
        guessable = []  #set to empty again, for repopulation
        cpuguess(everyletter,guessable,alreadyguessed,progress,life,tobeguessed)

def youvscpu():

    os.system('cls||clear')

    guess = str(input("What GERMAN word should be guessed?\n"))
    tobeguessed = list(guess)

    if len(guess) >= 16 or len(guess) < 3:
        print("\nPlease only put in a word. \n Only 3 to 15 letter words are allowed!\n (no umlauts please)\n")
        w = input("press Enter to try again, or press (m) to return to menu.")

        if w == str("m"):
            backtomenu()
        else:
            pass

        os.system('cls||clear')
        youvscpu()
    
    else:
        pass

    #every letter in the alphabet is guessable until it has already been guessed
    everyletter = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]
    guessable = []
    alreadyguessed = []
    progress = ["_"] * len(tobeguessed)
    life = 6

    cpuguess(everyletter,guessable,alreadyguessed,progress,life,tobeguessed)
 
def cpuvsyou(choice, life):
    os.system('cls||clear')
    length = ""
    counter = 0

    

    if choice == str(1):
        #german wordlist https://theworld.com/~reinhold/diceware_german.txt

        file = open('Semesterprojekt/GermanWords.txt', 'r')
        # .lower() returns a version with all upper case characters replaced with lower case characters.
        text = file.read().lower()

        #close the file
        file.close()

        # replaces anything that is not a lowercase letter, a space, or an apostrophe with a space:
        text = re.sub('[^a-z\ \']+', " ", text)
        words = list(text.split())

        #only be able to choose words above 5 and under 10 characters
        morethanfive = []
        for i in words:
            if len(i) >= 5 and len(i) < 10:     
                morethanfive.append(i)

        # print(morethanfive) - check if it worked


    elif choice == str(2):
        # english wordlist https://gist.github.com/deekayen/4148741

        #might not work when just opening the file. PATH HAS TO BE REPLACED!
        file = open('Semesterprojekt/EnglishWords.txt', 'r')
        # .lower() returns a version with all upper case characters replaced with lower case characters.
        text = file.read().lower()

        #close the file
        file.close()

        # replaces anything that is not a lowercase letter, a space, or an apostrophe with a space:
        text = re.sub('[^a-z\ \']+', " ", text)
        words = list(text.split())

        #only be able to choose words above 5 characters
        morethanfive = []
        for i in words:
            if len(i) >= 5 and len(i) < 10:
                morethanfive.append(i)
        


    wort = random.choice(morethanfive)
    tobeguessed = wort

    tobeguessedarr = list(tobeguessed) #in ein array umwandeln um es lesbar zu machen mit buchstaben
    
    for i in tobeguessed:
        length = length + "_"
        counter = counter+1

    
    print("Word has", counter, "letters: ", length)
    #print(tobeguessedarr)       #weg machen 

    emptyarr = [""]*len(tobeguessed)
    alrguessed = []

    guessing(tobeguessed, life, tobeguessedarr, length, emptyarr, alrguessed)     #6 Leben

def guessing(tobeguessed, life, tobeguessedarr,length, emptyarr, alrguessed):

        if life > 0:
            print("\n")
            print(f"Guessed wrong: {alrguessed}")
            print("Your current Health: ", life)
            print("\n")
            guess = str(input("Pick a letter: "))

            
            if len(guess) != 1:         # eine Zahl oder einen Umlaut zu raten ist nicht falsch und schadet nur
                print("please only put one letter in!") # dem Spieler. 
                time.sleep(2)
                guessing(tobeguessed, life, tobeguessedarr,length,emptyarr,alrguessed)

            print("\n")

        else:
            gameover(tobeguessed)

        #tobeguessed = []
        if guess == tobeguessed:
            celebration(life)

        else:
            pass
   

        if guess in tobeguessed:


            for i in range(0,len(tobeguessedarr)):
                
                if guess == tobeguessedarr[i]:
                    
                    print(guess, "is letter ", i+1)

                    buchstabe = tobeguessedarr[i]

                    if buchstabe in emptyarr[i] or guess in alrguessed:
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
                guessing(tobeguessed,life,tobeguessedarr, length, emptyarr, alrguessed)

        elif guess in alrguessed:
            print("Already guessed that one!")
            guessing(tobeguessed,life,tobeguessedarr, length, emptyarr, alrguessed)


        else:
               
            print(guess, "is not in the word\n")
            print(emptyarr)
            life = life-1
            alrguessed.append(guess)
            
            guessing(tobeguessed, life, tobeguessedarr, length, emptyarr, alrguessed)

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

def gameover(tobeguessed):

    os.system('cls||clear')
    print("You've lost!\n")
    print(f"The word you were looking for was {tobeguessed}")
    print("\n")
    backtomenu()

intro()

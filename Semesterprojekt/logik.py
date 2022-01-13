
import re

def beginning(alrguessed, wortarr, sofar, estored, nstored, istored, tstored, rstored, sstored, everythingstored, anfangsbuchstaben):

    anfangsbuchstaben = ["e", "n", "i", "t", "r", "s"]

    for i in range(0,5):
        print(f"is {anfangsbuchstaben[i]} part of your word?")
        choice = input("(y/n)")
        var = anfangsbuchstaben[i]

        if choice == str("y"):
            for j in range (0, len(wortarr)):
                if wortarr[j] == var:
                    sofar[j] += var

                    print(sofar)
                    alrguessed.append(anfangsbuchstaben[i])
                
        elif choice == str("n"):
            print(sofar)
            alrguessed.append(anfangsbuchstaben[i])

    # save, where a letter is
    
    for i in range(0,len(sofar)):
        if sofar[i] == "e":
            estored = i

        elif sofar[i] == "n":
            nstored = i

        elif sofar[i] == "i":
            istored = i

        elif sofar[i] == "t":
            tstored = i

        elif sofar[i] == "r":
            rstored = i

        elif sofar[i] == "s":
            sstored = i
        
        else:
            pass

    #I know this is ugly, leave me alone

    #print(estored, nstored, istored, tstored, rstored, sstored)
    

    everythingstored[0] = estored
    everythingstored[1] = nstored
    everythingstored[2] = istored
    everythingstored[3] = tstored
    everythingstored[4] = rstored
    everythingstored[5] = sstored


    #print(everythingstored)

def mechanik(wort, sofar, wortarr, alrguessed):

    anfangsbuchstaben = []

    everythingstored = [1,2,3,4,5,6]

    #store value to compare to. 1000 index is obviously too high -> 1000 = letter not in word, therefore has no index

    estored = 1000
    nstored = 1000
    istored = 1000
    tstored = 1000
    rstored = 1000
    sstored = 1000

    beginning(alrguessed, wortarr, sofar, estored, nstored, istored, tstored, rstored, sstored, everythingstored, anfangsbuchstaben)

    file = open('Semesterprojekt/GermanWords.txt', 'r')
    # .lower() returns a version with all upper case characters replaced with lower case characters.
    text = file.read().lower()

    #close the file
    file.close()

    # replaces anything that is not a lowercase letter, a space, or an apostrophe with a space:
    text = re.sub('[^a-z\ \']+', " ", text)
    everything = list(text.split())
    words = []

    for i in everything:
        if len(i) >= 3:
            words.append(i)


    possible = []
 

    #very inefficient but just want it to work before I optimize

    searching = []

    for i in range(0,len(everythingstored)):
        if everythingstored[i] == 1000:
            pass
        else:
            searching.append(everythingstored[i])

    #filter list for length 

    filtered = []

    for word in words:
        if len(word) == len(sofar):
            filtered.append(word)

    superfilter = []

    for i in range(0,len(searching)):
        if everythingstored == 1000:
            pass
        else:
            if i == 0:
                for word in filtered:
                    for i in range(0, len(word)):
                        if word[i] == "e":
                            superfilter.append(word)
        
            if i == 1:
                for word in filtered:
                    for i in range(0, len(word)):
                        if word[i] == "n":
                            superfilter.append(word)

            if i == 2:
                for word in filtered:
                    for i in range(0, len(word)):
                        if word[i] == "i":
                            superfilter.append(word)

            if i == 3:
                for word in filtered:
                    for i in range(0, len(word)):
                        if word[i] == "t":
                            superfilter.append(word)

            if i == 4:
                for word in filtered:
                    for i in range(0, len(word)):
                        if word[i] == "r":
                            superfilter.append(word)

            if i == 5:
                for word in filtered:
                    for i in range(0, len(word)):
                        if word[i] == "s":
                            superfilter.append(word)

    print("superfilter:",superfilter)
    # superfilter stimmt nicht ganz, da auch Worte drin sind, die nicht drin sein dürften

def start():

    wort = input("Type in your word: (3 letters minimum)\n")

    if len(wort) < 3:
        print("Please put at least a 3 letter word!")
        start()

    else:
        wortarr = list(wort)
        sofar = [""]*len(wortarr)
        alrguessed = []
        mechanik(wort, sofar, wortarr, alrguessed)


start()

 


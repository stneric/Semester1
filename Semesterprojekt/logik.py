import re


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

    file = open('Semesterprojekt\GermanWords.txt', 'r')
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
 

    #append words that could be it

    eisthere = 0
    nisthere = 0
    iisthere = 0
    tisthere = 0
    risthere = 0
    sisthere = 0

    if estored != 1000:
        for word in words:
            if word[estored] == "e":
                possible.append(word)
                eisthere = 1
            else:
                eisthere = 0

    if nstored != 1000:
        for word in words:
            if word[nstored] == "n":
                possible.append(word)
                nisthere = 1
            else:
                nisthere = 0

    if istored != 1000:
        for word in words:
            if word[istored] == "i":
                iisthere = 1
                possible.append(word)
            else:
                iisthere = 0
    
    if tstored != 1000:
        for word in words:
            if word[tstored] == "t":
                tisthere = 1
                possible.append(word)
            else:
                tisthere = 0

    if rstored != 1000:
        for word in words:
            if word[rstored] == "r":
                risthere = 1
                possible.append(word)
            else:
                risthere = 0

    if sstored != 1000:
        for word in words:
            if word[sstored] == "s":
                sisthere = 1
                possible.append(word)
            else:
                sisthere = 0

    actualwords = []
    tobesearched = []


    #very inefficient but just want it to work before I optimize

    for word in possible:
        for i in range(0):
            wo = everythingstored[i]
            if wo != 1000 and word[wo] == anfangsbuchstaben[i]:
                i = i+1
                wo = everythingstored[i]
                if wo != 1000 and word[wo] == anfangsbuchstaben[i]:
                    i = i+1
                    wo = everythingstored[i]
                    if wo != 1000 and word[wo] == anfangsbuchstaben[i]:
                        i = i+1
                        wo = everythingstored[i]
                        if wo != 1000 and word[wo] == anfangsbuchstaben[i]:
                            i = i+1
                            wo = everythingstored[i]
                            if wo != 1000 and word[wo] == anfangsbuchstaben[i]:
                               i = i+1
                               wo = everythingstored[i]
                               if wo != 1000 and word[wo] == anfangsbuchstaben[i]:
                                   i = i+1
                                   wo = everythingstored[i]
                                   if wo != 1000 and word[wo] == anfangsbuchstaben[i]:
                                       actualwords.append(word)

    print(actualwords)





    

# everything below this line doesn't work

    #make string

    # possible = [""]*len(sofar)
    # possiblestr = ""

    # for i in range (0,len(sofar)):
    #     if sofar[i] == "":
    #         possible[i] = "="   # muss ersetzt werden mit jedem buchstaben?? string in einzelne buchstaben
    #                             # einteilen und worte nach den buchstaben suchen die an der gleiche stelle sind
    #                             # danach filtern und raussuchen, wo die Buchstaben alle an den richtigen stellen
    #                             # vorkommen. 
    #     else:
    #         possible[i] = sofar[i]

    # for i in range(0,len(sofar)):
    #     possiblestr += possible[i]

    # print(possiblestr)

    # #only be able to choose words that have the already guessed letters in them, in the same order
    
    # sorted = []

    # for i in range(0,len(words)): 
    #     s=words[i].lower()
    #     if possiblestr in s: 
    #         sorted.append(words[i])

    # print(sorted)
    


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

 


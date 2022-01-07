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


def beginning(alrguessed, wortarr, sofar):

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



def mechanik(wort, sofar, wortarr, alrguessed):

    beginning(alrguessed, wortarr, sofar)

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

 


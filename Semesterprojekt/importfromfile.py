import re

file = open('Semesterprojekt\GermanWords.txt', 'r')
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
    if len(i) >= 5:
        morethanfive.append(i)

# print(morethanfive) - check if it worked
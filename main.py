# Import Statements
# for exiting the program
import sys
# for Integer checking
from isInt import *
# For path functionality
from pathlib import Path
# To open dialog box for file getter
from tkinter import *
from tkinter.filedialog import askopenfilename
#

Tk().withdraw()

while (True):
    # Greet the user
    print()
    print("Welcome to Mad Libs!")
    
    modeChoice = 0

    while not (isInt(modeChoice) and (modeChoice in [1,2,3])):
        print("Please select what you would like to do:")
        print("[1] Play an existing Mad Libs")
        print("[2] How to create a Mad Libs")
        print("[3] Exit program")
        print("CHOICE: ",end="")
        modeChoiceIn = input()
        if (isInt(modeChoiceIn)):
            modeChoice = int(modeChoiceIn)

    if (modeChoice == 1):
        # Ask for text file and get words out of there
        validFile = False
        txtFilename = ''
        print()
        print("Please select the .txt file.")

        while (not validFile):
            #opens dialog box which will return a filename
            txtFilename = askopenfilename()

            if (txtFilename == ''):
                validFile = False
                break
            elif (not txtFilename.endswith(".txt")):
                validFile = False
                print("Please choose a valid .txt file so you can begin writing.")
                print("[Press ENTER or RETURN]")
                wait1 = input()

            else:
                validFile = True
        
        print()

        if (not validFile):
            continue
        story = Path(txtFilename).read_text()
        words = []
        specials = []
        for line in story.splitlines():
            for word in line.split(" "):
                words.append(word)
        for word in words:
            if (word.startswith("{")):
                specials.append(word)
        
        replacements = []
        for special in specials:
            startIndex = 0
            endIndex = special.index("}")
            specialPresent = special[startIndex+1:endIndex]
            print(specialPresent + ": ",end="")
            answerIn = input()
            answer = str(answerIn).strip()

            pieces = special[1:len(special)].split("}")
            pieces[0] = answer
            replacement = "".join(pieces)
            replacements.append(replacement)

        for i in range(0,len(words)):
            if (words[i].startswith("{")):
                words[i] = replacements[0] 
                replacements.pop(0)

        finishedStory = " ".join(words)
        print()
        print(finishedStory)

    elif (modeChoice == 2):
        # Tell player formatting of Mad Libs stories
        print("To learn how to create a Mad Libs story, please refer to \"Story Formatting\" in the README.md.")
    elif (modeChoice == 3):
        print("Thanks for playing!")
        sys.exit()
    else:
        print("This shouldn't have happened. Please report the issue.")    

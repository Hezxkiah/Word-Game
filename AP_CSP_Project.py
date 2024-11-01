# #Imports
import time
import random
import os
os.system('cls')


#Variables
global points
points = 0
count = 0




#Lists
easyWords = ["Happy", "Cat", "Run", "Jump", "Book", "Tree", "Red", "Sun", "Door", "Ball", "Water", "Dog", "Blue", "Fish", "House", "Bird", "Food", "Chair", "Bed", "Smile", "Hat", "Friend", "Day", "Night", "Star", "Moon", "Song", "Dance", "Color", "Game", "One", "Two", "Three", "Four", "Five", "Big", "Small", "Happy", "Sad", "Fast", "Slow", "Hot", "Cold", "Wet", "Dry", "Good", "Bad", "Right", "Wrong", "New" ]
New_easyWords = []
mediumWords = [ "Weather", "Journey", "Courage", "Mystery", "Whisper", "Capture", "Gravity", "Motion", "Journey", "Symbol", "Connect", "Venture", "Absorb", "Theory", "Arrange", "Habitat", "Release", "System", "Control", "Insight", "Diverse", "Infinite", "Dynamic", "Relevant", "Analyze", "Sustain", "Enhance", "Synthesize", "Perspective", "Illuminate", "Assemble", "Optimize", "Disperse", "Manipulate", "Evolve", "Conceive", "Amplify", "Correlate", "Cultivate", "Validate", "Ascertain", "Attribute", "Chronicle", "Coalesce", "Conjecture", "Culminate", "Deliberate", "Fabricate", "Constitute", "Comprehend" ]
New_mediumWords = []
hardWords = [ "Serendipity", "Dichotomy", "Vicissitude", "Equanimity", "Mellifluous", "Perspicacity", "Recalcitrant", "Obfuscate", "Ineffable", "Quixotic", "Recalcitrant", "Obstreperous", "Multifarious", "Inscrutable", "Ineffable", "Nonchalant", "Ubiquitous", "Incontrovertible", "Idiosyncrasy", "Verisimilitude", "Antithesis", "Dissonance", "Ephemeral", "Reticent", "Pernicious", "Fallacious", "Alacrity", "Esoteric", "Capitulate", "Innocuous", "Paradox", "Proclivity", "Rhetoric", "Tenacity", "Altruistic", "Chicanery", "Debilitate", "Disparate", "Egregious", "Eschew", "Fatuous", "Impetuous", "Insidious", "Nefarious", "Obsequious", "Paragon", "Perfidious", "Precarious", "Spurious", "Vociferous" ]
New_hardWords = []


#Functions
#Function takes in user input (Yes or No, Y or N) and word
def CheckList(Yay_or_Nay,Func_CheckWord, randomNum):
    global points


    #While loop that checks user input and Randomly asks about a word in the New list
    while(1):
        #Y is a random word from the list
        y = random.randint(0,len(New_ListChoice)-1)
       
        #CHECKER
        # Checks to see if the input is yes, y, no, or n
        if Yay_or_Nay.lower() in ["yes", "y", "no", "n"]:


            #RANDOM
            #If the random number happens to be 1 this will run
            if randomNum == 1:        
                for Func_CheckWord in New_ListChoice[:]:
                    clear_terminal()
                    time.sleep(1.5)
                    print("*********************************************************************")
                    print("* SCORE: ",points,"                                   Difficulty:",Difficulty,"   *")
                    print("*                        THE WORD IS                                *")
                    print("                        ",New_ListChoice[y],"                                   ")
                    print("")
                    now = New_ListChoice[y]
                    New_CheckList(input("Have you seen this word before?: "), now)
                    break


   


            #FIRST INSTANCE
            #For the first time the game is played
            if Yay_or_Nay.lower() in ["no", "n"] and count == 1:
                print("")
                print("*********************************************************************")
                print("*                           YOURE RIGHT                             *")
                print("*********************************************************************")
                print("")
                points = points + 1
                time.sleep(1.5)
                clear_terminal()
                break
           


            #MAIN GAME
            #If the input was yes and they have seen the word then
            if Yay_or_Nay.lower() in ["yes", "y"]:
                if Func_CheckWord in New_ListChoice:
                    print("")
                    print("*********************************************************************")
                    print("*                            GAME OVER                              *")
                    print("*********************************************************************")
                    print("")
                    time.sleep(1.5)
                    clear_terminal()
                    exit()


            #MAIN GAME
            #For the rest of the game
            elif Yay_or_Nay.lower() in ["no", "n"]:
                if Func_CheckWord in New_ListChoice:
                    print("")
                    print("*********************************************************************")
                    print("*                           YOURE RIGHT                             *")
                    print("*********************************************************************")
                    print("")
                    points = points + 1
                    time.sleep(1.5)
                    clear_terminal()
                    break
                   
        #CHECKER  
        else:
            print("Please Try Again, you can only type Yes or No")
            Yay_or_Nay = input("Have you seen this word before?: ")






#CHECK FOR THE RANDOM INSTANCE
def New_CheckList(New_Yay_or_Nay, New_Func_oldWord):
    global points
   
    while(1):
            if New_Yay_or_Nay.lower() in ["yes", "y", "no", "n"]:
               
                #If the input was yes and they have seen the word then
                if New_Yay_or_Nay.lower() in ["yes", "y"]:
                    if New_Func_oldWord in New_ListChoice:
                        print("")
                        print("*********************************************************************")
                        print("*                           YOURE RIGHT                             *")
                        print("*********************************************************************")
                        print("")
                        points = points + 1
                        time.sleep(1.5)
                        clear_terminal()
                        break


                #MAIN GAME
                #For the rest of the game
                elif New_Yay_or_Nay.lower() in ["no", "n"]:
                    if New_Func_oldWord in New_ListChoice:
                        print("")
                        print("*********************************************************************")
                        print("*                            GAME OVER                              *")
                        print("*********************************************************************")
                        print("")
                        time.sleep(1.5)
                        clear_terminal()
                        exit()


            else:
                print("Please Try Again, you can only type Yes or No")
                New_Yay_or_Nay = input("Have you seen this word before?: ")


#Clears Terminal when prompted
def clear_terminal():
    if os.name == 'nt':
        os.system('cls')




#Intructions
print("************************************************************************")
print("*****        Hello, Welcome to CAN YOU REMEMBER THAT WORD!         *****")
print("*****                       Instructions                           *****")
print("*****        1. There will be a word that is displayed             *****")
print("*****        2. Then you'll be asked if you have seen the word     *****")
print("*****        3. You can only type Yes, yes, Y, No, no, or N        *****")
print("*****        4. If the word has been seen you lose                 *****")
print("*****        5. If the word hasn't been seen you get 1 point       *****")
print("*****        6. SEE HOW MANY POINTS YOU CAN GET                    *****")
print("************************************************************************")


#Pauses for 1 Second
time.sleep(1)


#Makes sure user inputs easy, medium, or hard
while (1):
    #Asks user for Difficulty of choice
    ListChoice = input("What Difficulty Do You Want Easy, Medium, or Hard?: ")


    #Sets the list and uses .lower() so if the user puts in Easy it will turn into easy
    if ListChoice.lower() == "easy":
        ListChoice = easyWords
        New_ListChoice = New_easyWords
        Difficulty = "Easy  "
        break
    elif ListChoice.lower() == "medium":
        ListChoice = mediumWords
        New_ListChoice = New_mediumWords
        Difficulty = "Medium"
        break
    elif ListChoice.lower() == "hard":
        ListChoice = hardWords
        New_ListChoice = New_hardWords
        Difficulty = "Hard  "
        break
    else:
        print("Please put it in a proper response")


#Print a word from the chosen list based on the number of words that are in said list
for word in ListChoice[:]:
    x = random.randint(0,1)
    count = count + 1
    print("*********************************************************************")
    print("* SCORE: ",points,"                                   Difficulty:",Difficulty,"   *")
    print("*                        THE WORD IS                                *")
    print("                        ",word,"                                   ")
    CheckWord = word
    ListChoice.remove(CheckWord)
    New_ListChoice.append(CheckWord)
    print("")
    CheckList(input("Have you seen this word before?: "), CheckWord, x)
    time.sleep(1.5)
    clear_terminal()

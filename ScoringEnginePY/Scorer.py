#Opening the text file with reg values and users
#There will be a seperate file for install directories and the like)
info = open("plz.txt", "r")
users = open("try.txt", "r")
frqOne = open("FRQ1.txt", "r")
frqTwo = open("FRQ2.txt", "r")
scoringPage = open("scoring.html", "rw")

#Defining the array that will hold the array (yes, it's blank)
userArr = []

#Requires some work, but is workable
def regAnalysis(mainKey, checkVal, isHex):
    if(isHex):
        if(mainKey[2]==checkVal):
            print("Yes")
        else:
            print("No")
        for i in range(0,3):
            info.readline()
    else:
        if(int(mainKey[2],16)==checkVal):
            print("Yes")
        else:
            print("No")
        for i in range(0,3):
            info.readline()

#Retrieves and sorts the users
def user():
    for i in range(0,4):
        users.readline()
    for val in users.readline().split():
        userArr.append(val)
    for val in users.readline().split():
        userArr.append(val)

#Checks the users for which ones are scored
def userCheck():
    if not "Bob" in userArr:
        print("Bob is removed")
    if not "Guest" in userArr:
        print("How did you do that?")

#Checks the forensics question answers to see if they are correct
def forensicsCheck(fileName, answer):
    for string in fileName:
        if("ANSWER:" in string.upper() and answer in string.upper()):
            print("Yay!")

#Initializes the webpage for the scoring engine
def webpage(start):
    if(start):
        scoringPage.write("<html>\n<body>\n")
    else:
        scoringPage.write("</html>\n</body>\n")

#All the function calls because....yeah
info.readline()
info.readline()
forensicsCheck(frqOne, "A value")
user()
userCheck()
regAnalysis(info.readline().split(), "0x1")
regAnalysis(info.readline().split(), "0x1")
regAnalysis(info.readline().split(), "0x0")
regAnalysis(info.readline().split(), "0x1")
scoringPage.close()

'''
Work to be done:
Software comparisons
Web page for display
Other things?
'''


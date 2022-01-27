import random




#Makes the password
def passMaker(length, usableChars, password, lengthOfChars):
    for i in range(length):
        addToPass = int(random.random() * lengthOfChars)
        password.append(usableChars[addToPass])
        i = i + 1
    return password

#Makes one list full of all of the chars the user wants in the password
def listMaker(baseList, listToAdd):
    for x in listToAdd:
        baseList.append(x)


# User questions
lengthOfPass = int(input("How long would you like your password to be: "))
caps = input("Type, Y, if you would like capital letters in your password and, N, if you would not: ")
lower = input("Type, Y, if you would like lowercase letters in your password and, N, if you would not: ")
nums = input("Type, Y, if you would like numbers in your password and, N, if you would not: ")
syms = input("Type, Y, if you would like symbols, exclamation points, question marks, etc, in your password and, N, if you would not: ")

#Just makes some lists
usableCharsList = []
password = []


# Making bools out of the user input
if(caps == "Y"):
    caps = True

else:
    caps = False

if(lower == "Y"):
    lower = True
    
else:
    lower = False

if(nums == "Y"):
    nums = True

else:
    nums = False

if(syms == "Y"):
    syms = True

else:
    syms = False


#Chars available for the password
capsList = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Z"]
lowerList = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "z"]
numsList = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]
symsList = ["!", "@", "$", "%", "^", '&', "*", "(", ")", "#", "-", "_", "+", "=", "{", "[", "]", "}", "|", "<", ">", "/"]

#Uses the listMaker funtion to add the chars to one list
if(caps == True):
    listMaker(usableCharsList, capsList)
if(lower == True):
    listMaker(usableCharsList, lowerList)
if(nums == True):
    listMaker(usableCharsList, numsList)
if(syms == True):
    listMaker(usableCharsList, symsList)

#Puts the password into a list
lengthOfChars = len(usableCharsList)
password = passMaker(lengthOfPass, usableCharsList, password, lengthOfChars)
finalPassword = ""

#Puts the password into a string
for i in range(len(password)):
    finalPassword = finalPassword + password[i]
    i = i + 1


#Prints the password
print(finalPassword)





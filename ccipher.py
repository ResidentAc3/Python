import math

def cipher(string, shift):    
    charArray = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]
    returnCipher = ""
    for text in string:
        if((charArray.index(text)+shift)<25):
            returnCipher += charArray[charArray.index(text)+shift]
        else:
            returnCipher += charArray[int(math.fabs((charArray.index(text)+shift)-26))]
    return returnCipher

cipherString = input("Enter the cipher text:" )
i = 1
j = 1
while(i<25):
    x = cipher(cipherString, i)
    print(cipher(cipherString, i))
    while(j<25):
        print("\t" + cipher(x, j))
        j+=1
    i+=1
    j = 0

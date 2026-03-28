#write a program to find letter A in the string and if you find the letter end the program
word=input("Enter a word: ")
word=word.upper()
for i in word:
    if (i=="A"):
        print("A is found")
        break
    else:
        print("A is not found")
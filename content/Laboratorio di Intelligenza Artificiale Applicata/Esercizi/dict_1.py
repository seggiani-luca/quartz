# Given a key, check whether a dictionary already contains the key

dictionary = {}

while True:
    word = input("Type a word, or \"Bye\" to terminate: ")
    if(word == "Bye"):
        break
    defo = input("Type the definition of this word: ")
    
    dictionary[word] = defo

print(f"Got dictionary: {dictionary}")

check = input("Enter the word to check: ")

if check in dictionary:
    print(dictionary[check])
else:
    print("No definition for this word")

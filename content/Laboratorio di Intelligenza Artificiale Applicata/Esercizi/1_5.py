# Given the string s = ‘Python is not that hard’, generate a new string 
# (string not list!!) containing only the consonants. Use comprehensions

vowels = {'a', 'e', 'y', 'o', 'u'}

s = "Python is not that hard"

cons = "".join([c for c in s if c not in vowels])

print(f"Consonant string is: \"{cons}\"")

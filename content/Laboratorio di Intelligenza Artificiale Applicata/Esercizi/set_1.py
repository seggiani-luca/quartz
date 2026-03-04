# Taking the string “HellO World” print the count of unique characters,
# ignoring case and spaces. It should return 7 unique characters. Use set
# operations to solve this efficiently

helo = input("Enter string: ")
print(f"String is: {helo}")

unique = set(helo.lower()) - {' '}

print(f"Unique chars are: {unique}, count {len(unique)}")

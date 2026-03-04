# Given a list of words, use set comprehension to create a set containing only
# words that have no repeated letters. For example, from ["hello", "python",
# "set", "unique"], only "python" and "set" would be included

def no_repeat(word):
    return len(set(word)) == len(word)

words = ["hello", "python", "set", "unique"]
print(f"List of words is: {words}")

res = {word for word in words if no_repeat(word)}
print(f"Set of unique words with no repeated letters is: {res}")

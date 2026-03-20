# rite a while loop using := that reads integers from input() and computes 
# their running sum. Stop when the user enters 0. Print the final sum

tot = 0
while n := int(input("Enter num: " )):
    if n == 0: 
        break
    tot += n

print(f"Total is: {tot}")

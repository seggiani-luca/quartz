# Write a function to find the max of some integers (unknown number of
# integers in the args). The max must be above a user-defined threshold. If 
# not, print a message

def my_max(*nums, tresh):
    m = max(nums)
    if m < tresh:
        print("Massimo troppo piccolo")
        return None    

    return m

print(my_max(2, 3, 4, tresh=2))
print(my_max(2, 3, 4, tresh=5))

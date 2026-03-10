# Write a function to check whether at least one number among some given as 
# input is above a user-defined threshold using filter()

def check(*nums, tresh):
    return any(map(lambda x: x > tresh, nums))

print(check(2, 5, 6, 10, tresh=18))
print(check(2, 5, 6, 10, tresh=9))

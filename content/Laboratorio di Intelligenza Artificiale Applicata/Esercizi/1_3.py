# Given a list of numbers a = [1,9,3,6,2,5,87,1,8,2] generate a new list 
# containing the indices i such that the square of the i-th number is greater 
# than the sum of the values from 0 to i using comprehensions

a = [1, 9, 3, 6, 2, 5, 87, 1, 8,2]

lst = [idx for idx, val in enumerate(a) if val * val > sum(a[:idx])]
print(f"List is: {lst}")

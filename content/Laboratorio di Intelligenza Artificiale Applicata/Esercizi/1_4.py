# Given a list of numbers A = [2,1,4,2,3,4,5,6,7,8,9,10] generate a new list B
# where the i-th element of B is the sum of the previous even elements in A 
# i.e. from 0 to i, using loops

a = [2, 1, 4, 2, 3, 4, 5, 6, 7, 8, 9, 10]
siz = len(a)

b = [0] * siz
for i in range(0, siz):
    for j in range(0, i):
        if a[j] % 2 == 0:
            b[i] += a[j]

print(f"List is: {b}")

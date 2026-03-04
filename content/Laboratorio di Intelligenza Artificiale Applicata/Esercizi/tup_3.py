# Create a new tuple with each i-th element containing the sum of the i-th
# elements of the original tuples

tup1 = (3, 6, 9)
tup2 = (1, 1, 1)
tup3 = (6, 3, 0)

tup_sum = tuple(sum(elems) for elems in zip(tup1, tup2, tup3))

print(f"Tuple sum is: {tup_sum}")

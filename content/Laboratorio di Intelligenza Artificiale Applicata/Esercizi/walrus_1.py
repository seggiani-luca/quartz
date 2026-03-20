# Rewrite the following code using the walrus operator:
# values = [4, 8, 15, 16, 23, 42]
# filtered = []
# for v in values:
#     doubled = v * 2
#     if doubled > 20:
#         filtered.append(doubled)

values = [4, 8, 15, 16, 23, 42]


filtered = []
for v in values:
    doubled = v * 2
    if doubled > 20:
        filtered.append(doubled)
print(filtered)

my_filtered = [r for v in values if (r := v * 2) > 20]
print(my_filtered)

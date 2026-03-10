# Bubble sort

def bubble(v):
    for i in range(len(v) - 1, 0, -1):
        for j in range(0, i):
            if v[j + 1] < v[j]:
               t = v[j + 1]
               v[j + 1] = v[j]
               v[j] = t
        print(f"Passaggio {len(v) - i}: {v}")

r = [5, 3, 8, 4, 2]
bubble(r)

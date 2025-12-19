import random
#
n= int(input("enter lenght of list: "))

a = [round(random.uniform(-10, 10), 2) for _ in range(n)]

indexed = list(enumerate(a))

sorted_indexed = sorted(indexed, key=lambda x: x[1])

print("Initial list:")
for i, x in enumerate(a):
    print(f"index {i}: {x}")

print("\nnubers was increase index after sort:")
for new_index, (old_index, value) in enumerate(sorted_indexed):
    if new_index > old_index:
        print(value)

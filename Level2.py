import math
#
s = input("input integers with spaces: ")

try:
    nums = list(map(int, s.split()))
except ValueError:
    print("error: only integers are allowed")
    exit()

n = int(math.sqrt(len(nums)))
if n * n != len(nums):
    print("error: cant make square matrix")
    exit()

matrix = [nums[i * n:(i + 1) * n] for i in range(n)]

print("\nmatrix")
for row in matrix:
    print(row)

symmetric = True
for row in matrix:
    for j in range(n // 2):
        if row[j] != row[n - 1 - j]:
            symmetric = False
            break
    if not symmetric:
        break

# Вивід результату
if symmetric:
    print("\nmatrix have vertical symetry")
else:
    print("\nmatrix dont have vertical symetry")

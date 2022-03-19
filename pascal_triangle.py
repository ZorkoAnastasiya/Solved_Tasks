"""
Pascal's triangle (arithmetic triangle) is an infinite table of
binomial coefficients having a triangular shape.
In this triangle there are ones on the top and on the sides.
Each number is equal to the sum of two numbers above it.
The lines of the triangle are symmetric about the vertical axis.
Named after Blaise Pascal.
"""

N = int(input("Enter an integer number: "))
PT = []

for i in range(N):
    row = [1] * (i + 1)
    for j in range(i+1):
        if j != 0 and j != i:
            row[j] = PT[i-1][j-1] + PT[i-1][j]
    PT.append(row)

for row in PT:
    print(row)

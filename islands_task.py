"""
    One day, a formidable pirate Jack was lost in the middle of the Carbican Sea.
    To get home, he had to calculate - how many islands are in the Carbiscan Sea?
    He presented the sea as a grid, where '1's are land and '0's are (water).
    An island is surrounded by water and is formed by connected lands horizontally or vertically.
    You may assume all four edges of the grid are all surrounded by water.
    Please, help Jack to count islands.
    Example of grid:
    [
        ['1', '1', '1', '0', '0'],
        ['1', '1', '1', '0', '0'],
        ['1', '1', '1', '0', '0'],
        ['1', '1', '0', '0', '1'],
        ['1', '0', '0', '0', '1'],
    ]
    Answer: 2.
"""

islands = [
        ['1', '1', '1', '0', '0'],
        ['1', '1', '1', '0', '0'],
        ['1', '1', '1', '0', '0'],
        ['1', '1', '0', '0', '1'],
        ['1', '0', '0', '0', '1'],
    ]

islands2 = [
    ['0', '0', '0', '1', '0', '0', '0'],
    ['0', '0', '1', '1', '0', '0', '0'],
    ['0', '1', '1', '0', '0', '1', '0'],
    ['1', '1', '1', '1', '1', '1', '0'],
    ['0', '0', '1', '1', '1', '0', '0'],
]


def check_points(arr, i, j):
    if i + 1 in range(len(arr)) and arr[i + 1][j] == '1':
        arr[i + 1][j] = 't'
        check_points(arr, i + 1, j)
    if i - 1 in range(len(arr)) and arr[i - 1][j] == '1':
        arr[i - 1][j] = 't'
        check_points(arr, i - 1, j)
    if j + 1 in range(len(arr[0])) and arr[i][j + 1] == '1':
        arr[i][j + 1] = 't'
        check_points(arr, i, j + 1)
    if j - 1 in range(len(arr[0])) and arr[i][j - 1] == '1':
        arr[i][j - 1] = 't'
        check_points(arr, i, j - 1)


def islands_counter(arr):
    count = 0
    for i in range(len(arr)):
        for j in range(len(arr[i])):
            if arr[i][j] == '1':
                count += 1
                arr[i][j] = 't'
                check_points(arr, i, j)
    return count


print(islands_counter(islands))
print(islands_counter(islands2))

def get_matrix(n, m, value):
    matrix = []
    list1 = []
    for i in range(1, n + 1):
        for j in range(1, m + 1):
            if n <= 0 or m <= 0:
                return matrix
            if len(list1) == n:
                pass
            else:
                list1.append(value)
            if len(matrix) == m:
                continue
            else:
                matrix.append(list1)
    return matrix

result1 = get_matrix(3, 2, 10)
result2 = get_matrix(2, 3, 12)
result3 = get_matrix(4, 2, 43)

print(result1)
print(result2)
print(result3)
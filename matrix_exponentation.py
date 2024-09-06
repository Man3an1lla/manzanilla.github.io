n = int(input())
matrix = [[int(j) for j in input().split()] for _ in range(n)]
m = int(input())


matrix1 = matrix.copy()
i = 1
while i < m:
    matrixC = [[0] * n for _ in range(n)]
    for r in range(n):
        for c in range(n):
            for q in range(n):
                matrixC[r][c] += matrix1[r][q] * matrix[q][c]
    matrix1 = matrixC
    i += 1

for row in matrixC:
    print(*row)
    
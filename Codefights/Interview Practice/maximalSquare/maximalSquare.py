def maximalSquare(matrix):
    # create square matrix of two tuples (longest horizontal sequence of ones, longest vertical sequence of ones)
    # solve using DP
    # create square matrix of area of biggest square from upper left corner
    # solve using DP and previous matrix
    if(len(matrix) == 0 or len(matrix[0]) == 0):
        return 0
    horizontalRunsMatrix = [ [None for j in range(len(matrix[0]))] for i in range(len(matrix))]
    verticalRunsMatrix = [ [None for j in range(len(matrix[0]))] for i in range(len(matrix))]
    for i in range(len(matrix)):
        horizontalRunsMatrix[i][-1] = int(matrix[i][-1])
    for i in range(len(matrix[0])):
        verticalRunsMatrix[-1][i] = int(matrix[-1][i])
    for i in range(len(horizontalRunsMatrix)):
        for j in range(len(horizontalRunsMatrix[0]) - 2, -1, -1):
            if matrix[i][j] == "1":
                horizontalRunsMatrix[i][j] = 1 + horizontalRunsMatrix[i][j + 1]
            else:
                horizontalRunsMatrix[i][j] = 0
    for i in range(len(verticalRunsMatrix[0])):
        for j in range(len(verticalRunsMatrix) - 2, -1, -1):
            if matrix[j][i] == "1":
                verticalRunsMatrix[j][i] = 1 + verticalRunsMatrix[j + 1][i]
            else:
                verticalRunsMatrix[j][i] = 0
    squaresMatrix = [ [ int(matrix[j][i]) for i in range(len(matrix[0])) ] for j in range(len(matrix))]
    maxArea = max(squaresMatrix[-1])
    maxArea = max(max([squaresMatrix[i][-1] for i in range(len(squaresMatrix))]), maxArea)
    for i in range(len(squaresMatrix) - 2, -1, -1):
        for j in range(len(squaresMatrix[0]) - 2, -1, -1):
            squaresMatrix[i][j] = min(verticalRunsMatrix[i][j],
                                      horizontalRunsMatrix[i][j],
                                      1 + squaresMatrix[i + 1][j + 1])
            maxArea = max(maxArea, squaresMatrix[i][j])
    print(squaresMatrix)
    return maxArea ** 2

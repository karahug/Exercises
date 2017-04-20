def booleanParenthesization(expression):
    symbols = re.split("[&^|]", expression);
    operators = re.split("[TF]", expression)[1:-1]
    T = [ [ (1 if symbols[i] == "T" else 0) if j == i else 0 for j in range(len(symbols)) ] for i in range(len(symbols)) ]
    F = [ [ (1 if (symbols[i] == "F") else 0) if j == i else 0 for j in range(len(symbols)) ] for i in range(len(symbols)) ]
    Total = [ [ (T[i][j] + F[i][j] if (T[i][j] != None and F[i][j] != None) else None) for i in range(len(symbols))] for j in range(len(symbols))]
    for gap in range(1, len(symbols)):
        for i in range(len(symbols) - gap):
            j = i + gap
            for k in range(i, j):
                co = operators[k]
                Total[i][k] = T[i][k] + F[i][k]
                Total[k+1][j] = T[k + 1][j] + F[k + 1][j]
                if co == "&":
                    T[i][j] += T[i][k] * T[k + 1][j]
                    F[i][j] += Total[i][k] * Total[k + 1][j] - T[i][k] * T[k + 1][j]
                elif co == "|":
                    T[i][j] += Total[i][k] * Total[k + 1][j] - F[i][k] * F[k + 1][j]
                    F[i][j] += F[i][k] * F[k + 1][j]
                else:
                    T[i][j] += T[i][k] * F[k + 1][j] + F[i][k] * T[k + 1][j]
                    F[i][j] += T[i][k] * T[k + 1][j] + F[i][k] * F[k+1][j]
    print(T)
    return T[0][-1] % 1003



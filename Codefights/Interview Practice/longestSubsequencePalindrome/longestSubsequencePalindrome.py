def longestSubsequencePalindrome(a):
    r = list(reversed(a))
    return lcs(a, r)

def lcs(sequence1, sequence2):
    table = []
    for i in range(len(sequence1) + 1):
        table.append([])
        for j in range(len(sequence2) + 1):
            if(i == 0 or j == 0):
                table[i].append(0)
            else:
                table[i].append(None)
    for i in range(1, len(sequence1) + 1):
        for j in range(1, len(sequence2) + 1):
            if(sequence1[i - 1] == sequence2[j - 1]):
                table[i][j] = table[i - 1][j - 1] + 1
            else:
                table[i][j] = max(table[i - 1][j], table[i][j - 1])
    return table[-1][-1]

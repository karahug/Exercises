def nearestGreater(a):
    nearestGreaterRight = ngr(a)
    nearestGreaterLeft = ngl(a)
    result = []
    for i in range(len(a)):
        diffLeft = abs(i - nearestGreaterLeft[i])
        diffRight = abs(i - nearestGreaterRight[i])
        if(nearestGreaterLeft[i] == -1 and nearestGreaterRight[i] == -1):
            result.append(-1)
        elif nearestGreaterLeft[i] == -1:
            result.append(nearestGreaterRight[i])
        elif nearestGreaterLeft[i] == -1:
            result.append(nearestGreaterRight[i])
        elif diffRight < diffLeft:
            result.append(nearestGreaterRight[i])
        else:
            result.append(nearestGreaterLeft[i])
    return result


def ngr(l):
    unassigned = []
    result = [-1 for i in range(len(l))]
    for i in range(len(l) - 1):
        if(l[i + 1] > l[i]):
            result[i] = i + 1
            while(len(unassigned) > 0 and l[i + 1] > l[unassigned[-1]]):
                result[unassigned.pop()] = i + 1
        else:
            unassigned.append(i)
    return result

def ngl(l):
    r = list(reversed(l))
    reversedResult = ngr(r)
    result = list(map(lambda x: -1 if x == -1 else len(l) - 1 - x, reversed(reversedResult)))
    return result

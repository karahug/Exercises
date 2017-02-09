def findPerms(cap, mySum):
	x = min(cap[0], mySum)
	y = min(cap[1], mySum - x)
	z = min(cap[2], mySum - x - y)
	firstPerm = [x, y, z]
	checkablePerms = [firstPerm]
	foundPerms = list(checkablePerms)
	while checkablePerms:
		base = checkablePerms.pop(0)
		newPerms = list()
		for i in range(3):
			if base[i] < cap[i]:
				temp = min(base[(i+1)%3], cap[i] - base[i])
				tempList = list(base)
				tempList[i] += temp
				tempList[(i+1)%3] -= temp
				newPerms += [list(tempList)]

				temp = min(base[(i+2)%3], cap[i] - base[i])
				tempList = list(base)
				tempList[i] += temp
				tempList[(i+2)%3] -= temp
				newPerms += [list(tempList)]
		for p in newPerms:
			if p not in foundPerms:
				foundPerms += [p]
				checkablePerms += [p]
	return foundPerms

def threeGlasses(cap):
	initialSum = sum(cap)
	cap = sorted(cap, reverse = True)
	checkableSums = [initialSum]
	sums = set(checkableSums)
	while checkableSums:
		base = checkableSums.pop(0)
		permutations = findPerms(cap, base)
		subtractables = set([item for sublist in permutations for item in sublist])
		for s in subtractables:
			result = base - s
			if result not in sums:
				sums.add(result)
				checkableSums += [result]
	sums.remove(0)
	return len(sums)
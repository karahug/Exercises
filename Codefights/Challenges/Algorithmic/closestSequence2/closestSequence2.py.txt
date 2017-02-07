def closestSequence2(a,b):
	aLength = len(a)
	bLength = len(b)
	#d = np.empty((aLength, bLength), dtype = int)
	d = [[None] * bLength for i in range(aLength)]
	nDiagonals = bLength - aLength
	## compute first diagonal:
	for i in range(1, aLength + 1):
		d[-i][-i] = sum([abs(a[-j] - b[-j]) for j in range(1, i + 1)])
	## compute nth diagonal:
	for i in range(1, nDiagonals + 1):
		## calculate bottom element in diagonal:
		d[-1][bLength - i - 1] = min(d[-1][bLength - i], abs(a[-1] - b[bLength - i]))
		## work up from bottom:
		for j in range(1, aLength):
			aIndex = aLength - 1 - j
			bIndex = bLength - i - j - 1
			d[aIndex][bIndex] = min(d[aIndex][bIndex + 1], abs(a[aIndex] - b[bIndex]) + d[aIndex + 1][bIndex + 1])
	
	return d[0][0]
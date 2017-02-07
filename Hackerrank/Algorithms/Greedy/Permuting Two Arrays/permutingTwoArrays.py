testCaseCount = int(input())

def minArrSums(arr1, arr2, k):
	arr1 = sorted(arr1)
	arr2 = sorted(arr2)
	added = []
	for i in arr1:
		success = False
		for j in arr2:
			if i+j >= k:
				arr2.remove(j)
				success = True
				break
		if not success:
			return False
	return True


for i in range(testCaseCount):
	[arrayLength, target] = [int(x) for x in input().split(' ')]
	firstArray = [int(x) for x in input().split(' ')]
	secondArray = [int(x) for x in input().split(' ')]
	if minArrSums(firstArray, secondArray, target):
		print('YES')
	else:
		print('NO')
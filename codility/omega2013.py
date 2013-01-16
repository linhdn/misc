def falling_disks (A, B):
	# process B
	current = 0
	for index in xrange(len(B)):
		if B[index]>current:
			current = B[index]
		else:
			B[index] = current
	# process A
	current = 1000000000
	lenA = len(A)
	for index in xrange(lenA):
		if A[index]<current:
			current = A[index]
		else:
			A[index] = current
	indexB = 0
	lenB = len(B)
	# do the comparision
	for indexA in xrange(lenA-1, -1, -1):
		if indexB >= lenB:
			return lenB
		if A[indexA] >= B[indexB]:
			indexB += 1
	return indexB

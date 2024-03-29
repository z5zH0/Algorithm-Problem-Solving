# link: 
# solving method: binary search (upper bound)
# upper bound: when "list[mid] <= key", "mid + 1" becomes "low"

def upperBS(a, L):
	low = 0
	high = max(L) + 1
	while low < high:
		mid = (low + high) // 2
		count = 0
		for i in range(len(L)):
			count += L[i] // mid
		if count < a:
			high = mid
		else:
			low = mid + 1
	return low - 1

k, n = map(int, input().split())
A = []
for i in range(0,k):
	A.append(int(input()))
print(upperBS(n, A))

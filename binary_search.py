import pdb 

#assumed ordered list
def binarySearch(list, item):
	first = 0
	last = len(list)-1
	found = False

	while first <= last and not found:
		#get center point
		middle = (first + last) // 2
		if list[middle] == item:
			return True
		else:
			if item < list[middle]:
				last = middle - 1
			else:
				first = middle + 1

	return found


#binary search recursivly 
# O(log n)
def recursiveBinarySearch(list, item):
	if len(list) == 0:
		return False
	else:
		middle = len(list) // 2
		# print list[middle]

		if item == list[middle]:
			return True
		else:
			if item < list[middle]:
				#slice operator in Python is actually O(k).
				#We can just pass in start and end points like the first example
				return recursiveBinarySearch(list[:middle], item)
			else:
				return recursiveBinarySearch(list[middle + 1:], item)


list = [1,3,5,6,7,8,9,12,43,63]

print binarySearch(list, 93)
print binarySearch(list, 3)

print recursiveBinarySearch(list, 3)
print recursiveBinarySearch(list, 43)
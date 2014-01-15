def insertionSort(num_list):
	for item in range(1,len(num_list)):
		current = num_list[item]
		position = item
		print "current"
		print current
		print num_list

		while position > 0 and num_list[position - 1] > current:
			print "in"
			num_list[item] = num_list[position - 1]
			position = position - 1 

		num_list[position] = current

	return num_list


num_list = [54,26,93,17,77,31,44,55,20]
print insertionSort(num_list)
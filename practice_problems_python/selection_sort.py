def selectionSort(num_list):
	for current in range(len(num_list) - 1, -1, -1):
		max_position = 0
		for location in range(1, current + 1):
			if num_list[location] > num_list[max_position]:
				max_position = location

		temp = num_list[current]
		num_list[current] = num_list[max_position]
		num_list[max_position] = temp

	return num_list

num_list = [54,26,93,17,77,31,44,55,20]
print selectionSort(num_list)

package main

// n = size, i = index of ie node at i
func heapify(arr []int, size, nodePos int) {
	largest := nodePos
	left := 2*nodePos + 1
	right := 2*nodePos + 2

	// if left child is larger then root
	if left < size && arr[left] > arr[largest] {
		largest = left
	}

	// if right child is larger then root
	if right < size && arr[right] > arr[largest] {
		largest = right
	}

	// if largest is not root
	if largest != nodePos {
		// swap
		swap(arr, nodePos, largest)

		// recurse
		heapify(arr, size, largest)
	}
}

func heapifyMin(arr []int, size, nodePos int) {
	smallest := nodePos
	left := 2*nodePos + 1
	right := 2*nodePos + 2

	if left < size && arr[left] < arr[smallest] {
		smallest = left
	}

	if right < size && arr[right] < arr[smallest] {
		smallest = right
	}

	if nodePos != smallest {
		swap(arr, nodePos, smallest)

		// recursively heapify now
		heapifyMin(arr, size, smallest)
	}
}

func heapSortMin(arr []int, size int) {
	// populate min heap
	for i := size; i >= 0; i-- {
		heapifyMin(arr, size, i)
	}

	// now rearrange array with min values on the right side
	for i := (size - 1); i >= 0; i-- {
		swap(arr, 0, i)
		heapifyMin(arr, i, 0)
	}
}

func heapSortMax(arr []int, size int) {
	for i := (size - 1); i >= 0; i-- {
		heapify(arr, size, i)
	}

	for i := size - 1; i >= 0; i-- {
		swap(arr, 0, i)
		heapify(arr, i, 0)
	}
}

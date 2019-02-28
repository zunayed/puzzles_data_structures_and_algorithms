package main

import (
	"fmt"
)

// n = size, i = index of ie node at i
func heapify(arr []int, n, i int) {
	largest := i
	left := 2*i + 1
	right := 2*i + 2

	// if left child is larger then root
	if left < n && arr[left] > arr[largest] {
		largest = left
	}

	// if right child is larger then root
	if right < n && arr[right] > arr[largest] {
		largest = right
	}

	// if largest is not root
	if largest != i {
		// swap
		swap(arr, i, largest)

		// recurse
		heapify(arr, n, largest)
	}
}
func heapSort(arr []int, size int) {
	for i := (size/2 - 1); i >= 0; i-- {
		heapify(arr, size, i)
	}

	for i := size - 1; i >= 0; i-- {
		swap(arr, 0, i)
		heapify(arr, i, 0)
	}
}

func main() {
	tc := []int{99, 212, 23, 3, 1, 10}
	// tc := []int{199, 212}
	heapSort(tc, len(tc))
	fmt.Printf("%v", tc)
}

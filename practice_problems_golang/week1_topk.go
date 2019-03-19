package main

// import "fmt"

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

func topK(arr []int, k int) []int {
	arrSize := len(arr)

	// populate max heap
	for i := 0; i < arrSize; i++ {
		heapify(arr, arrSize, i)
	}

	// Iterate through heap and use get max to
	// populate arr
	for i := 0; i < k; i++ {
		// swap the first and the last element
		// and re-heapify

		// swap only last element as we narrow the array
		right := (arrSize - 1) - i
		arr[0], arr[right] = arr[right], arr[0]
		heapify(arr, right, 0)
	}

	//return last k elements of
	return arr[arrSize-k:]
}

/*
func main() {
	arr := []int{5, 8, 1, 2, 3, 4, 0, 6, 7, -1}
	fmt.Printf("%v", topK(arr, 4))
}
*/

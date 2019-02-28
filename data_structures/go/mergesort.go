package main

func merge(arr, left, right []int) {
	res := make([]int, len(arr))
	leftSize, rightSize := len(left), len(right)

	var i, j, k int
	for i = range res {
		if j >= leftSize || k >= rightSize {
			break
		}

		if left[j] <= right[k] {
			res[i] = left[j]
			j++
		} else {
			res[i] = right[k]
			k++
		}
	}

	// Only one of these two copies run, so no need to increase i
	copy(res[i:], left[j:])
	copy(res[i:], right[k:])

	copy(arr, res)
}

func mergeSort(arr []int) {
	size := len(arr)

	if size <= 1 {
		return
	}
	mid := size / 2
	mergeSort(arr[:mid])
	mergeSort(arr[mid:])
	merge(arr, arr[:mid], arr[mid:])
}

/*
func main() {
	tc := []int{99, 212, 23, 3, 1, 10}
	mergeSort(tc, 0, len(tc)-1)
	fmt.Printf("%v", tc)
}
*/

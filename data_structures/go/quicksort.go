package main

func choosePivot(arr []int, start, stop int) int {
	return start
}

/*
// Linear scan method
// TODO finish linear scan
func partition(arr []int, start, stop, pivot int) int {
	fmt.Printf("partition -> %v, start %v, stop %v, pivot %v\n", arr, start, stop, pivot)
	num_less_then_pivot_count := 0
	for i := start; i < stop; i++ {
		if arr[i] <= arr[pivot] {
			num_less_then_pivot_count++
		}
	}

	new_arr := make([]int, len(arr))
	pivot_final_location := num_less_then_pivot_count - 1
	new_arr[pivot_final_location] = arr[pivot]

	less_then_count := 0
	greater_then_count := num_less_then_pivot_count

	for i := start; i < stop; i++ {
		if i == pivot {
			continue
		}
		if arr[i] <= arr[pivot] {
			new_arr[less_then_count] = arr[i]
			less_then_count++
		} else {
			new_arr[greater_then_count] = arr[i]
			greater_then_count++
		}
	}

	arr = new_arr
	return pivot_final_location
}
*/

// Lomuto partition method
// TODO understand the stop-1
func partition(arr []int, start, stop int) int {
	pivot_val := arr[stop]

	for current := start; current < stop-1; current++ {
		if arr[current] <= pivot_val {
			// swap arr[current] with arr[start]
			arr[current], arr[start] = arr[start], arr[current]
			start++
		}
	}

	arr[start], arr[stop] = arr[stop], arr[start]

	return start
}

func quickSort(arr []int, start, stop int) {
	if (start == stop) || (start > stop) {
		return
	}

	final_pivot_location := partition(arr, start, stop)
	quickSort(arr, start, final_pivot_location-1)
	quickSort(arr, final_pivot_location+1, stop)
}

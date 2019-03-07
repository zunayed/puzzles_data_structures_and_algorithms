package main

import (
	"sort"
)

func ThreeSum(arr []int) [][]int {
	output := [][]int{}

	if len(arr) < 3 {
		return output
	}

	// sort O(nlogn) operation
	sort.Sort(sort.IntSlice(arr))

	// skip the last two elements of array
	// so we can index into them without access errors
	for i, _ := range arr[:len(arr)-2] {
		if i > 0 && arr[i] == arr[i-1] {
			continue
		}

		left := i + 1
		right := len(arr) - 1

		for left < right {
			sum := arr[i] + arr[left] + arr[right]

			if sum > 0 {
				right--
			} else if sum < 0 {
				left++
			} else {
				output = append(output, []int{arr[i], arr[left], arr[right]})

				// Remove duplicates
				for left+1 < right && arr[left] == arr[left+1] {
					left += 1
				}

				for right-1 < left && arr[right] == arr[right-1] {
					right--
				}

				left++
				right--
			}
		}
	}

	return output
}

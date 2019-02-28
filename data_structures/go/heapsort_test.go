package main

import (
	"sort"
	"testing"
)

func TestHeapSort(t *testing.T) {
	var testCases = [][]int{
		{1},
		{},
		{5, 4},
		{2, 99, 1},
		{999, 2, 1, -2},
	}

	for _, tt := range testCases {
		// We need to make a copy of the slice to be able to test
		tmp := make([]int, len(tt))
		copy(tmp, tt)

		heapSort(tmp, len(tmp))
		sort.Sort(sort.IntSlice(tt))
		if !equal(tmp, tt) {
			t.Errorf("Invalid result custom_sort: %v, want: %v.", tmp, tt)
		}
	}
}

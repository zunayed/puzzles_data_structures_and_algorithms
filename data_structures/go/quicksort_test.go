package main

import (
	"sort"
	"testing"
)

func TestQuickSort(t *testing.T) {
	var testCases = [][]int{
		{0, 0, 1},
		{-8, 0, 1},
		{1},
		{},
		{5, 4},
		{2, 99, 1},
	}

	for _, tt := range testCases {
		// We need to make a copy of the slice to be able to test
		tmp := make([]int, len(tt))
		copy(tmp, tt)

		quickSort(tmp, 0, len(tmp)-1)
		sort.Sort(sort.IntSlice(tt))
		if !Equal(tmp, tt) {
			t.Errorf("Invalid result custom_sort: %v, want: %v.", tmp, tt)
		}
	}
}

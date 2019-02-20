package main

import (
	"sort"
	"testing"
)

func equal(a, b []int) bool {
	if len(a) != len(b) {
		return false
	}

	for i := range a {
		if a[i] != b[i] {
			return false
		}
	}

	return true
}

func TestQuickSort(t *testing.T) {
	var testCases = [][]int{
		{5, 4},
		{2, 99, 1},
	}

	for _, tt := range testCases {
		// We need to make a copy of the slice to be able to test
		tmp := make([]int, len(tt))
		copy(tmp, tt)

		quickSort(tmp, 0, len(tmp)-1)
		sort.Sort(sort.IntSlice(tt))
		if !equal(tmp, tt) {
			t.Errorf("Invalid result custom_sort: %v, want: %v.", tmp, tt)
		}
	}
}

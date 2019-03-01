package main

import (
	"sort"
	"testing"
)

func TestMaxHeapSort(t *testing.T) {
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

		heapSortMax(tmp, len(tmp))
		sort.Sort(sort.IntSlice(tt))
		if !Equal(tmp, tt) {
			t.Errorf("Invalid result: %v, want: %v.", tmp, tt)
		}
	}
}

func TestMinHeapSort(t *testing.T) {
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

		heapSortMin(tmp, len(tmp))
		sort.Sort(sort.Reverse(sort.IntSlice(tt)))
		if !Equal(tmp, tt) {
			t.Errorf("Invalid result: %v, want: %v.", tmp, tt)
		}
	}
}

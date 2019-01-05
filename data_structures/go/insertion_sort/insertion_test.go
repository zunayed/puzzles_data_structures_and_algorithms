package main

import (
	"reflect"
	"testing"
)

var sortTests = []struct {
	in  []int
	out []int
}{
	{[]int{}, []int{}},
	{[]int{9, 3, 4}, []int{3, 4, 9}},
	{[]int{1, 2, 3}, []int{1, 2, 3}},
	{[]int{-9, -11, 4}, []int{-11, -9, 4}},
	{[]int{0, 0, 1}, []int{0, 0, 1}},
	{[]int{}, []int{}},
}

func TestInsertionSort(t *testing.T) {
	for _, tt := range sortTests {
		insertionSort(tt.in)
		if !reflect.DeepEqual(tt.in, tt.out) {
			t.Errorf("Sorting incorrect got: %d, want: %d.", tt.in, tt.out)
		}
	}
}

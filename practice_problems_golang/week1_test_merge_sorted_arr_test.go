package main

import (
	"reflect"
	"testing"
)

func TestMergeSortedArray(t *testing.T) {
	var mergeTestCases = []struct {
		in1 [5]int
		in2 [10]int
		out [10]int
	}{
		{
			[5]int{1, 2, 4, 5, 99},
			[10]int{1, 3, 7, 9, 17},
			[10]int{1, 1, 2, 3, 4, 5, 7, 9, 17, 99},
		},
	}

	for _, tt := range mergeTestCases {
		mergeSortedArray(&tt.in1, &tt.in2)
		if !reflect.DeepEqual(tt.in2, tt.out) {
			t.Errorf(
				"Invalid result got: %v expected: %v",
				tt.in2,
				tt.out,
			)
		}
	}
}

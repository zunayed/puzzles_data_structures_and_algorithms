package main

import (
	"reflect"
	"testing"
)

var nutsBoltsTestCases = []struct {
	nuts  []int32
	bolts []int32
	out   []string
}{
	{[]int32{}, []int32{}, []string{}},
	{[]int32{1}, []int32{1}, []string{"1 1"}},
	{[]int32{1, 2}, []int32{2, 1}, []string{"1 1", "2 2"}},
	{
		[]int32{4, 32, 5, 7},
		[]int32{32, 7, 5, 4},
		[]string{"4 4", "5 5", "7 7", "32 32"},
	},
}

func TestNutsBolts(t *testing.T) {
	for _, tt := range nutsBoltsTestCases {
		result := matchNutsBolts(tt.nuts, tt.bolts)
		if !reflect.DeepEqual(result, tt.out) {
			t.Errorf(
				"Invalid result got: %v expected: %v",
				result,
				tt.out,
			)
		}
	}
}

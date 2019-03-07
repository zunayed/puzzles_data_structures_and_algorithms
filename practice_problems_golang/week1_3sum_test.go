package main

import (
	"reflect"
	"testing"
)

func in_array(val interface{}, array interface{}) (exists bool, index int) {
	exists = false
	index = -1

	switch reflect.TypeOf(array).Kind() {
	case reflect.Slice:
		s := reflect.ValueOf(array)

		for i := 0; i < s.Len(); i++ {
			if reflect.DeepEqual(val, s.Index(i).Interface()) == true {
				index = i
				exists = true
				return
			}
		}
	}
	return
}

var threeSumTestCases = []struct {
	in  []int
	out [][]int
}{
	{[]int{10, 3, -4, 1, -6, 9}, [][]int{{-6, -4, 10}, {-4, 1, 3}}},
	{[]int{12, 34, -46}, [][]int{{-46, 12, 34}}},
}

func TestThreeSum(t *testing.T) {
	for _, tt := range threeSumTestCases {
		result := ThreeSum(tt.in)
		if !reflect.DeepEqual(result, tt.out) {
			t.Errorf(
				"invalid result got: %v expected: %v",
				result,
				tt.out,
			)
		}
	}
}

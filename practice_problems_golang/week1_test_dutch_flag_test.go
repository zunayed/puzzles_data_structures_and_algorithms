package main

import (
	"reflect"
	"testing"
)

func TestDutchFlagSort(t *testing.T) {
	var dutchFlagTestCases = []struct {
		in  []string
		out []string
	}{
		{
			[]string{"G", "B", "G", "R", "B", "R", "G"},
			[]string{"R", "R", "G", "G", "G", "B", "B"},
		},
		{
			[]string{"G", "B"},
			[]string{"G", "B"},
		},
		{
			[]string{},
			[]string{},
		},
		{
			[]string{"B", "R", "G"},
			[]string{"R", "G", "B"},
		},
	}

	for _, tt := range dutchFlagTestCases {
		dutchFlagSort(tt.in)
		if !reflect.DeepEqual(tt.in, tt.out) {
			t.Errorf(
				"Invalid result got: %v expected: %v",
				tt.in,
				tt.out,
			)
		}
	}

}

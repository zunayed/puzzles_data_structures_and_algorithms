package main

import (
	"testing"
)

var OneAwayTestCases = []struct {
	inA string
	inB string
	out bool
}{
	{"pale", "pale", true},
	{"pale", "bale", true},
	{"pale", "ple", true},
	{"pales", "pale", true},
	{"pale", "bake", false},
	{"kal", "bake", false},
}

func TestOneAway(t *testing.T) {
	for _, tt := range OneAwayTestCases {
		result := OneAway(tt.inA, tt.inB)

		if result != tt.out {
			t.Errorf(
				"Invalid result input: %v, %v got: %v expected %v",
				tt.inA,
				tt.inB,
				result,
				tt.out,
			)
		}
	}
}

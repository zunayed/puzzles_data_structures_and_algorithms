package main

import (
	"testing"
)

var permutationTestCases = []struct {
	s1  string
	s2  string
	out bool
}{
	{"foo", "oof", true},
	{"foo", "fooo", false},
	{"foo", "foo", true},
	{"hello", "lleho", true},
	{"", "", true},
}

func TestCheckPermutation(t *testing.T) {
	for _, tt := range permutationTestCases {
		if checkPermutation(tt.s1, tt.s2) != tt.out {
			t.Errorf("Invalid result got: %s %s, want: %v.", tt.s1, tt.s2, tt.out)
		}
	}
}

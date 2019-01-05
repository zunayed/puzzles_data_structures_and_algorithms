package main

import (
	"testing"
)

var testCases = []struct {
	in  string
	out bool
}{
	{"abc", true},
	{"abcc", false},
	{"", false},
	{"abcdefghijklmnopqrstuvwxyz", true},
	{"failfail", false},
}

func TestIsUnique(t *testing.T) {
	for _, tt := range testCases {
		if isUnique(tt.in) != tt.out {
			t.Errorf("Invalid result got: %s, want: %v.", tt.in, tt.out)
		}
	}
}

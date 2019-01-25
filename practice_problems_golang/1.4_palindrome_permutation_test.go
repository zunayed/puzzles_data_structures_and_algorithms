package main

import (
	"testing"
)

var palindromeTestCases = []struct {
	in  string
	out bool
}{
	{"daad a", true},
	{"dad", true},
	{"catter", false},
	{"abcdefghijklmnopqrstuvwxyz", false},
	{"", false},
	{"Tact Coa", true},
}

func testIsPalindromePerm(t *testing.T) {
	for _, tt := range testCases {
		if IsPalindromePerm(tt.in) != tt.out {
			t.Errorf("Invalid result got: %s, want: %v.", tt.in, tt.out)
		}
	}
}

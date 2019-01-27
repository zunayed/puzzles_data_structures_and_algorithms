package main

import (
	"testing"
)

var CompressTestCases = []struct {
	in  string
	out string
}{
	{"aaa", "a3"},
	{"aaabb", "a3b2"},
	{"ab", "a1b1"},
	{"aabcccccaaa", "a2b1c5a3"},
}

func TestCompress(t *testing.T) {
	for _, tt := range CompressTestCases {
		result := Compress(tt.in)
		if result != tt.out {
			t.Errorf(
				"Invalid result input: %v got: %v expected: %v",
				tt.in,
				result,
				tt.out,
			)
		}
	}
}

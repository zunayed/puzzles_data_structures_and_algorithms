package main

import (
	"testing"
)

var urlifyTestCases = []struct {
	in  string
	out string
}{
	{"mr john smith", "mr%20john%20smith"},
	{"mr john", "mr%20john"},
	{"mrjohn", "mrjohn"},
	{"", ""},
	{"test ", "test%20"},
	{" test", "%20test"},
}

func TestURLify(t *testing.T) {
	for _, tt := range urlifyTestCases {
		result := URLify(tt.in)
		if result != tt.out {
			t.Errorf("Invalid result got: %s, want: %v.", result, tt.out)
		}
	}
}

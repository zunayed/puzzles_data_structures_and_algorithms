package main

import (
	"fmt"
	"testing"
)

func TestPrintEvenOddPerm(t *testing.T) {
	var permTestCase = []struct {
		in []int
	}{
		{[]int{1, 3, 5, 2, 4, 6}},
	}
	for _, tt := range permTestCase {
		printEvenOddPerm(tt.in, 0)
		fmt.Println("----------")
		printEvenOddPermBetter(tt.in, 0)
	}
}

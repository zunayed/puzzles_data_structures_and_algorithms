package main

import (
	"fmt"
)

func swapInt(input []int, a, b int) {
	input[a], input[b] = input[b], input[a]
}

func isEven(n int) bool {
	return n%2 == 0
}

func checkIfAlternating(input []int) bool {
	for index, num := range input {
		if isEven(index) {
			// this should be odd
			if isEven(num) {
				return false
			}
		} else {
			// this should be even
			if !isEven(num) {
				return false
			}
		}
	}
	return true
}

func printEvenOddPerm(input []int, i int) {
	if i == len(input)-1 {
		if input[0]%2 > 0 && checkIfAlternating(input) {
			fmt.Printf("%v\n", input)
		}
		return
	}

	for j := i; j < len(input); j++ {
		swapInt(input, i, j)
		printEvenOddPerm(input, i+1)
		swapInt(input, j, i)
	}
}

/*
func main() {
	printEvenOddPerm([]int{1, 3, 5, 2, 4, 6}, 0)
}
*/

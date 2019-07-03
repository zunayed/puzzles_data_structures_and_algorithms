package main

import (
	"fmt"
)

func validWord(input []string) {
	return true
}

func ValidWordPrefix(arr []string, size int) bool {
	return true
}

func printValidWords(input []int, i int) {
	if i == len(input)-1 {
		if ValidWord(input) {
			fmt.Printf("%v\n", input)
		}

		return
	}

	for j := i; j < len(input); j++ {
		if !validWordPrefix(input, j) {
			continue
		}

		swapInt(input, i, j)
		printEvenOddPerm(input, i+1)
		swapInt(input, j, i)
	}
}

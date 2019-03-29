package main

import (
	"fmt"
)

func printPerm(input []string, i int) {
	if i == len(input)-1 {
		fmt.Printf("%s\n", input)
		return
	}

	for j := i; j < len(input); j++ {
		swapString(input, i, j)
		printPerm(input, i+1)
		swapString(input, j, i)
	}
}

func main() {
	printPerm([]string{"b", "c", "e", "f"}, 0)
}

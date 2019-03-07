package main

import (
	"fmt"
)

/*
	input array
	seen so far
	start position
	end index
*/
func printSubsets(arr []string, seen []string, start, end int) {
	if start == len(arr) {
		for i := 0; i < end; i++ {
			fmt.Printf(seen[i])
		}
		fmt.Println("")

		return
	}

	printSubsets(arr, seen, start+1, end)
	seen = append(seen, arr[start])
	printSubsets(arr, seen, start+1, end+1)

}

/* Extension problem
Given an array of positive integers, print only those subsets that have a certain sum.
(If the values can be negative, this is a simple change in the base case, where you
print the said subset only if it has the right sum)

*/
func printSubsetsCertainSum(arr []int, seen []int, start, end, target int) {
	if start == len(arr) {
		sum := 0
		for i := 0; i < end; i++ {
			sum = sum + seen[i]
		}

		if sum == target {
			fmt.Println(start, end, seen)
		}

		return
	}

	printSubsetsCertainSum(arr, seen, start+1, end, target)
	seen = append(seen, arr[start])
	printSubsetsCertainSum(arr, seen, start+1, end+1, target)
}

func main() {
	input := []string{"t", "c", "d", "o"}
	seen := []string{}
	printSubsets(input, seen, 0, 0)
	input2 := []int{4, 5, 6, 2, 2, 1, 1}
	seen2 := []int{}
	printSubsetsCertainSum(input2, seen2, 0, 0, 4)
}

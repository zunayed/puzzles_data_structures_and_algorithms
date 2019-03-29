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
func genSubsets(arr []string, seen []string, start, end int) [][]string {
	if start == len(arr) {
		/*
				for i := 0; i < end; i++ {
					fmt.Printf(seen[i])
				}
				fmt.Println("")
			fmt.Printf("%v\n", seen)
		*/

		return [][]string{seen[:end]}
	}

	l := genSubsets(arr, seen, start+1, end)
	seen = append(seen, arr[start])
	r := genSubsets(arr, seen, start+1, end+1)

	return append(l, r...)

}

/* Extension problem # 1
Assume that the input is an array of size 'n' where 'n' is an even number.
Additionally, assume that  half the integers are even and the other half are odd.
Print only those permutations where odd and even integers alternate, starting with odd.

func isEven(num int) bool {
	return num%2 == 0
}

func printAlternatingNumOnly(arr []int, seen []int, start int) {
	if start == len(arr)-1 {
		// First has to be odd
		if isEven(seen[0]) {
			return
		}

		// check if alternating
		for i := 1; i < end; i++ {
			if isEven(i) { // if i is odd seen should be even
				if !isEven(seen[i]) {
					return
				}

			} else {
				if isEven(seen[i]) { // if i is even it should be odd
					return
				}
			}

			fmt.Printf("%d", seen[i])
		}

		fmt.Println("")
		return
	}

	printAlternatingNumOnly(arr, seen, start+1, end)
	seen = append(seen, arr[start])
	printAlternatingNumOnly(arr, seen, start+1, end+1)
}
*/

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

/* Extension problem
func main() {
	input := []string{"t", "c", "d", "o"}
	seen := []string{}
	fmt.Printf("%v\n\n", genSubsets(input, seen, 0, 0))

	fmt.Println("----------Extension problem 1------------")
	printAlternatingNumOnly([]int{1, 2, 3, 3, 5, 6}, []int{}, 0, 0)
	//printAlternatingNumOnly([]int{1, 1, 2}, []int{}, 0, 0)

	fmt.Println("----------Extension problem 2------------")
	printAlternatingNumOnly([]int{1, 2, 3, 3, 5, 6}, []int{}, 0, 0)

	fmt.Println("----------Extension problem 3------------")
	input2 := []int{4, 5, 6, 2, 2, 1, 1}
	seen2 := []int{}
	printSubsetsCertainSum(input2, seen2, 0, 0, 4)
}
*/

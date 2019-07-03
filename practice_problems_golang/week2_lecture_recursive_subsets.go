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

func main() {
	input := []string{"t", "c", "d", "o"}
	seen := []string{}

	for _, v := range genSubsets(input, seen, 0, 0) {
		fmt.Printf("%v\n", v)
	}
}

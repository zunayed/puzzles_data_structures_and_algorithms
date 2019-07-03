package main
/*

import (
	"fmt"
)

	input array
	seen so far
	start position
	end index
func genSubsets(arr string, seen string, start, end int) []string {
	if start == len(arr) {
		// fmt.Printf("%v %v\n", arr[:end], seen[:end])
		fmt.Printf("%s start:%v end: %v\n", seen[:end], start, end)
		return []string{string(seen[:end])}
	}

	l := genSubsets(arr, seen, start+1, end)
	seen = fmt.Sprintf("%s%s", seen, string(arr[start]))
	r := genSubsets(arr, seen, start+1, end+1)

	return append(l, r...)

}
*/

/*
func main() {
	input := "1234"
	seen := ""
	fmt.Printf("%v", genSubsets(input, seen, 0, 0))
}
*/

package main

import (
	"fmt"
)

/*
a2 is 2*len(a1)
merge a1 into a2
*/
func mergeSortedArray(a1 *[5]int, a2 *[10]int) {
	// (1) swap values of a2 into second half of a2
	mid := len(a2) / 2
	for i := 0; i < len(a1); i++ {
		//swap
		a2[i], a2[mid+i] = a2[mid+i], a2[i]
	}

	// (2) iterate two pointers
	// p1 -> 0 from a1
	// p2 -> mid from a2

	p1 := 0
	p2 := mid
	n := len(a2)
	for i := 0; i < n; i++ {
		if p1 == len(a1) {
			a2[i] = a2[p2]
			p2++
		} else if p2 == n {
			a2[i] = a1[p1]
			p1++
		} else if a1[p1] < a2[p2] {
			a2[i] = a1[p1]
			p1++
		} else {
			a2[i] = a2[p2]
			p2++
		}
	}
}

func main() {
	a1 := [5]int{1, 2, 4, 5, 999}
	a2 := [10]int{1, 3, 7, 9, 99}
	mergeSortedArray(&a1, &a2)
	fmt.Printf("%v", a2)
}

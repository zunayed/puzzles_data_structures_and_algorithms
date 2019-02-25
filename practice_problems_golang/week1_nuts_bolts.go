package main

import (
	"fmt"
	"math/rand"
)

func swap(arr []int32, i, j int) {
	arr[i], arr[j] = arr[j], arr[i]
}

/*
We want to partition in such a way that everything less than the pivot is
towards the beginning and everything greater than the pivot is towards the end
We maintain 2 areas 0 -> i (less than pivot) and i to end greater than pivot
if we get an element less than pivot we swap and extend both areas
if we get an element greater than pivot we can just extend the second area
if we get an element equal to pivot we move it to the end and then swap back
to the right place at the end of the while loop
*/

func partition(arr []int32, start, stop int, pivot int32) int {
	i, j := start, start
	for j < stop {
		if arr[j] < pivot {
			swap(arr, i, j)
			i++
			j++
		} else if arr[j] == pivot {
			swap(arr, j, stop)
		} else {
			j += 1
		}
	}

	swap(arr, i, stop)
	return i

}

func match(nuts, bolts []int32, start, stop int) {
	if start >= stop {
		return
	}

	// no range func in golang lol
	index := rand.Intn(stop-start) + start
	finalPivotPos := partition(nuts, start, stop, bolts[index])

	partition(bolts, start, stop, nuts[finalPivotPos])

	match(nuts, bolts, start, finalPivotPos-1)
	match(nuts, bolts, finalPivotPos+1, stop)
}

func matchNutsBolts(nuts, bolts []int32) []string {
	match(nuts, bolts, 0, len(nuts)-1)

	output := []string{}

	for index, nut := range nuts {
		bolt := bolts[index]
		output = append(output, fmt.Sprintf("%d %d", nut, bolt))
	}

	return output
}

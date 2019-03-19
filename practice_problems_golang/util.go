package main

func swap(arr []int, a, b int) {
	arr[a], arr[b] = arr[b], arr[a]
}

func swapString(input []string, a, b int) {
	input[a], input[b] = input[b], input[a]
}

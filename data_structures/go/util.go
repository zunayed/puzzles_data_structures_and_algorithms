package main

func swap(arr []int, a, b int) {
	arr[a], arr[b] = arr[b], arr[a]
}

func equal(a, b []int) bool {
	if len(a) != len(b) {
		return false
	}

	for i := range a {
		if a[i] != b[i] {
			return false
		}
	}

	return true
}

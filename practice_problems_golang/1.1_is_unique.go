/*
Implement an algorithm to determine if a string has all unique characters. What if you cannot use additional data structures?
*/
package main

func isUnique(s string) bool {
	if len(s) == 0 || len(s) > 128 {
		return false
	}

	var seenList = make([]bool, 128)

	for _, char := range s {
		if seenList[char] {
			return false
		}

		seenList[char] = true
	}

	return true
}

func main() {
	isUnique("")
}

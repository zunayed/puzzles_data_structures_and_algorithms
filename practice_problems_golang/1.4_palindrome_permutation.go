/*
Palindrome Permutation: Given a string, write a function to check if it is a permutation of a palin­ drome.
A palindrome is a word or phrase that is the same forwards and backwards.
A permutation is a rearrangement of letters. The palindrome does not need to be limited to just dictionary words.

EXAMPLE
Input: Tact Coa
Output: True (permutations: "taco cat", "atco eta", etc.)
*/
package main

/*
case -> even length string
	- all char have to have corresponding even match
	  ex. 2 a, 4 b, 8 d

case -> odd length string
	- only one char can have a odd number of instance
	- all char have to have corresponding even match
	  ex. 2 a, 4 b, 8 d
*/
func IsPalindromePerm(s string) bool {
	letterCount := make(map[rune]int)

	for _, char := range s {
		// If the requested key doesn't exist, we get the value type's zero value.
		// In this case the value type is int, so the zero value is 0
		letterCount[char] += 1
	}

	seenCharWithOddCount := false
	for _, v := range letterCount {
		if v/2 != 0 {
			if !seenCharWithOddCount {
				seenCharWithOddCount = true
			} else {
				return false
			}
		}
	}

	return true
}

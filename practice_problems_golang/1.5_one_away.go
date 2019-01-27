/*
One Away: There are three types of edits that can be performed on strings: insert a character, remove a character, or replace a character. Given two strings, write a function to check if they are one edit (or zero edits) away.
EXAMPLE
pale, ple -> true pales, pale -> true pale, bale -> true pale, bake -> false
*/
package main

import (
//"fmt"
// "math"
// "strings"
)

func replaceChar(s1, s2 string) bool {
	foundCharToReplace := false

	for pos, _ := range s1 {
		if s1[pos] != s2[pos] {
			if foundCharToReplace {
				return false
			}

			foundCharToReplace = true
		}
	}

	return true
}

func oneCharAway(s1, s2 string) bool {
	index1 := 0
	index2 := 0

	for index2 < len(s2) && index1 < len(s1) {
		if s1[index1] != s2[index2] {
			if index1 != index2 {
				return false
			}
			index2++
		} else {
			index1++
			index2++
		}
	}

	return true
}

func OneAway(s1, s2 string) bool {
	if s1 == s2 {
		return true
	} else if len(s1) == len(s2) {
		return replaceChar(s1, s2)
	} else if len(s1)+1 == len(s2) {
		return oneCharAway(s1, s2)
	} else if len(s1) == (len(s2) + 1) {
		return oneCharAway(s2, s1)
	}

	return false
}

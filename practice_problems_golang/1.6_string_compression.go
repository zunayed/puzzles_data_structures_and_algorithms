/*
String Compression: Implement a method to perform basic string compression using the counts of repeated characters. For example, the string aabcccccaaa would become a2blc5a3. If the "compressed" string would not become smaller than the original string, your method should return
the original string. You can assume the string has only uppercase and lowercase letters (a - z).
*/
package main

import (
	"strconv"
)

func Compress(s string) string {
	compressedString := ""
	lastChar := s[0]
	lastCharCounter := 0

	for pos, char := range s {
		if string(char) == string(lastChar) {
			lastCharCounter++
		} else {
			compressedString += string(lastChar)
			compressedString += strconv.Itoa(lastCharCounter)
			lastCharCounter = 1
		}

		lastChar = s[pos]
	}

	compressedString += string(lastChar)
	compressedString += strconv.Itoa(lastCharCounter)
	return compressedString
}

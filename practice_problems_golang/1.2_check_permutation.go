package main

import (
	"sort"
	"strings"
)

func sortString(w string) string {
	s := strings.Split(w, "")
	sort.Strings(s)
	return strings.Join(s, "")
}

func checkPermutation(s1, s2 string) bool {
	if s1 == s2 {
		return true
	}

	if sortString(s1) == sortString(s2) {
		return true
	}

	return false
}

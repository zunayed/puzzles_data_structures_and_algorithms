/*
input = n x m matrix of letters

   1 2 3 4 5

1  h o a y o
2  b s a b v
3  z b p e s
4  v n p l q

Find if list of words is in this board

ex
find_words([apple, bad, yo]) -> [true, false, true]


Solution approach -
recursive function using a graph?

Depth first traversal
- make sure to keep track of visited cells
make sure traversal happens only once


Need a way to store visited nodes
*/

package main

import (
	"fmt"
)

type boggleBoard struct {
	data  [][]string
	sizeX int
	sizeY int
}

func (b boggleBoard) pprint() {
	for i := range b.data {
		fmt.Println(b.data[i])
	}
}

func matchWord(wordsToSearch []string, word string) bool {
	fmt.Printf("checking word %s", word)

	for i, w := range wordsToSearch {
		if w == word {
			return true
		}
	}

	return false
}

func findWords(wordsToLookFor []string, board *boggleBoard, seen_words *[][]bool, curX, curY int, word string) {
	/*
		if curX > board.sizeX-1 || curY > board.sizeY {
			return
		}
	*/

	*(seen_words)[curX][curY] = true
	word = fmt.Sprintf("%s%s", word, board.data[curX][curY])

	if matchWord(wordsToLookFor, word) {
		fmt.Println("FOUND WORD", word)
	}

	for row := curX - 1; row <= curX+1 && row < board.sizeX; row++ {
		for col = curY - 1; col <= curY+1 && col < board.sizeY; col++ {
			if row >= 0 && col >= 0 && !seen_words[row][col] {
				findWordsUtil(wordsToLookFor, board, &seen_words, row, col, word)
			}
		}
	}
}

func main() {
	board := boggleBoard{}
	board.sizeX = 5
	board.sizeY = 4
	board.data = [][]string{
		{"h", "o", "a", "y", "o"},
		{"b", "s", "a", "b", "v"},
		{"z", "b", "p", "e", "s"},
		{"v", "n", "p", "l", "q"},
	}

	board.pprint()

	seen_words := make([][]bool, boggleSizeY)
	//fmt.Println(seen_words)

	// prepare seen word storage
	for i := range seen_words {
		seen_words[i] = make([]bool, sizeY)
	}

	word := ""

	wordsToLookFor := []string{"apple", "bad", "yo"}

	for x = 0; x < board.sizeX; x++ {
		for y = 0; y < board.sizey; y++ {
			findWords(wordsToLookFor, board, &seen_words, i, j, word)
		}
	}
}

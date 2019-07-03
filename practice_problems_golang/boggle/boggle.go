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
	//fmt.Printf("checking word %s \n", word)

	for _, w := range wordsToSearch {
		if w == word {
			return true
		}
	}

	return false
}

func findWords(wordsToLookFor []string, board *boggleBoard, seen_words *[][]bool, curY, curX int, word string) {
	/*
		if curX > board.sizeX-1 || curY > board.sizeY {
			return
		}
	*/

	//fmt.Printf("POS - %d, %d \n", curY, curX)

	(*seen_words)[curY][curX] = true
	word = fmt.Sprintf("%s%s", word, board.data[curY][curX])

	if matchWord(wordsToLookFor, word) {
		fmt.Println("FOUND WORD", word)
	}

	// row = Y col = X

	for row := curY - 1; row <= curY+1 && row < board.sizeY; row++ {
		for col := curX - 1; col <= curX+1 && col < board.sizeX; col++ {

			//fmt.Printf("Pre check - %d, %d \n", row, col)
			if row >= 0 && col >= 0 && !(*seen_words)[row][col] {
				// fmt.Printf("post check - %d, %d \n", row, col)
				findWords(wordsToLookFor, board, seen_words, row, col, word)
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
		{"b", "i", "z", "b", "v"},
		{"u", "b", "p", "e", "s"},
		{"q", "n", "p", "l", "q"},
	}

	board.pprint()
	word := ""

	wordsToLookFor := []string{"apple", "bad", "yo", "geek"}
	seen_words := make([][]bool, board.sizeY)
	//fmt.Println(seen_words)

	// prepare seen word storage
	for i := range seen_words {
		seen_words[i] = make([]bool, board.sizeX)
	}

	for y := 0; y < board.sizeY; y++ {
		for x := 0; x < board.sizeX; x++ {
			findWords(wordsToLookFor, &board, &seen_words, y, x, word)
		}
	}
}

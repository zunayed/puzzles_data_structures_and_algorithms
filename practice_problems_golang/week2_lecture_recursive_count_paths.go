package main

// import "fmt"

func countPath(grid [][]int, r, c int) int {
	N := len(grid)
	M := len(grid[0])

	if (r > N-1) || (c > M-1) {
		return 0
	}

	if (r == N-1) && (c == M-1) {
		return 1
	}

	return countPath(grid, r+1, c) + countPath(grid, r, c+1)
}

/*
func main() {
	grid := [][]int{
		{0, 0, 0, 0},
		{0, 0, 0, 0},
		{0, 0, 0, 0},
		{0, 0, 0, 0},
	}
	fmt.Printf("%d", countPath(grid, 2, 2))
}
*/

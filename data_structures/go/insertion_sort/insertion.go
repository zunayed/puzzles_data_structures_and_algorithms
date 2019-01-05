package main

func insertionSort(inputList []int) {
	for i := 0; i < len(inputList)-1; i++ {
		insert(inputList, i)
	}
}

func insert(inputList []int, mark int) {
	for i := mark; i > -1; i-- {
		if inputList[i] > inputList[i+1] {
			swap(inputList, i, i+1)
		} else {
			return
		}
	}
}

func swap(inputList []int, left, right int) {
	temp := inputList[left]
	inputList[left] = inputList[right]
	inputList[right] = temp
}

def printMatrix(matrix):
	rowstring =''
	for row in matrix:
		rowstring = rowstring + "["
		for cell in row:
			rowstring = rowstring + " " + str(cell) + " "
			rowstring = rowstring + "]\n"            
	
	return rowstring


def rotate90(matrix, n):
    temp = matrix[0]
    print temp


matrix = [[1, 2, 3, 4],[5, 6, 7, 8],[9, 10, 11, 12],[13, 14, 15, 16]]

print printMatrix(matrix)
# rotate90(matrix, 4)
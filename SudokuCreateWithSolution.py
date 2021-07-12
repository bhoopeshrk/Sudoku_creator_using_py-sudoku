from sudoku import Sudoku

#Creating 3x3 sudoku
puzzle = Sudoku(3).difficulty(0.65) #declaring difficulty level must between 0 and 1
#Displaying the created sudoku puzzle
puzzle.show()

#Creating solution for the created sudoku puzzle
solution = puzzle.solve()
#Displaying the solution for the the created sudoku puzzle
solution.show()

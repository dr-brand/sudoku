
public class SudokuJava {

	private static final int GRID_SIZE = 9;
	
	public static void main(String[] args) {
		System.out.println("Hello world!");
		
		int [][] board = {
				{7,0,2,0,5,0,6,0,0},
				{0,0,0,0,0,3,0,0,0},
				{1,0,0,0,0,9,5,0,0},
				{8,0,0,0,0,0,0,9,0},
				{0,4,3,0,0,0,7,5,0},
				{0,9,0,0,0,0,0,0,8},
				{0,0,9,7,0,0,0,0,5},
				{0,0,0,2,0,0,0,0,0},
				{0,0,7,0,4,0,2,0,3}
		};
		if (solveBoard(board)) {
			System.out.println("Sudoku resuelto!!");
		}
		else {
			System.out.println("No tiene solucion!!");
		}
		printBoard(board);
		
			
	}

	private static void printBoard(int[][] board) {
		for (int i = 0; i < GRID_SIZE; i++) {
			for (int j = 0; j < GRID_SIZE; j++) {
				System.out.print(board[i][j]);
				if(((j+1) % 3 == 0) && j != 0 && j != 8 ) {
					System.out.print("|");
				}
			}
			System.out.println();
			if(((i+1) % 3 == 0) && i != 0 && i != 8 ) {
				System.out.print("-----------");
				System.out.println();
			}
		}
	}

	private static boolean isNumberInRow(int[][] board, int number, int row) {
		for(int i = 0; i < GRID_SIZE; i++) {
			if (board[row][i] == number) {
				return true;
			}
		}
		return false;
	}
	
	private static boolean isNumberInColumn(int[][] board, int number, int column) {
		for(int i = 0; i < GRID_SIZE; i++) {
			if (board[i][column] == number) {
				return true;
			}
		}
		return false;
	}

	private static boolean isNumberInBox(int[][] board, int number, int row, int column) {
		int rowpos = row - row % 3;
		int colpos = column - column % 3;
		
		for(int i = rowpos; i < rowpos + 3; i++) {
			for(int j = colpos; j < colpos + 3; j++) 
			if (board[i][j] == number) {
				return true;
			}
		}
		return false;
	}
	
	private static boolean isValidPlacement(int[][] board, int number, int row, int column) {
		return !isNumberInRow(board, number, row) &&
				!isNumberInColumn(board, number, column) &&
				!isNumberInBox(board, number, row, column);
	
	}
	
	private static boolean solveBoard(int[][] board) {
		
		for(int i = 0 ; i < GRID_SIZE; i++) {
			for(int j = 0 ; j < GRID_SIZE; j++) {
				if(board[i][j] == 0) {
					for(int numberToTry = 1; numberToTry <= GRID_SIZE; numberToTry++) {
						if (isValidPlacement(board, numberToTry, i, j)) {
							board[i][j] = numberToTry;
							if (solveBoard(board)) {
								
								return true;
							}
							else {
								board[i][j] = 0;
							}
							
						}
					
					}
				return false;
				} 
		}
		
	}
	return true;
	
}
	
}

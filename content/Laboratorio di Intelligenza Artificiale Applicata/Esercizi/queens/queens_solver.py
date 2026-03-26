"""
8-Queens Problem Solver

This module implements functions to solve the classic 8-queens problem.
"""

def is_safe(board, row, col):
    """
    Check if a queen can be placed at position (row, col) without being threatened.
    
    A queen threatens another queen if they share the same row, column, or diagonal.
    
    Parameters:
        board (list): A 1D array where board[i] represents the column position 
                     of the queen in row i
        row (int): The row to check
        col (int): The column to check
    
    Returns:
        bool: True if it's safe to place a queen at position (row, col), False otherwise
    """

    def safe(q_row, q_col):
        """
        Check if the queen to place is safe relative to one queen already on the board.

        Parameters:
            q_row (int): The row of the queen already on the board
            q_col (int): The column of the queen already on the board

        Returns:
            bool: True if the queen to place doesn't conflict with the queen already on
                 the board, False otherwise
        """

        # ignore same row
        if q_row == row:
            return True 

        # check same column
        if q_col == col:
            return False 

        # check same diagonal
        if abs(q_row - row) == abs(q_col - col):
            return False 

        return True 
    
    # check against all queens
    return all([safe(q_row, q_col) for q_row, q_col in enumerate(board)])

def solve_queens(n=8):
    """
    Solve the n-queens problem and return a solution if one exists.
    
    Parameters:
        n (int): The size of the board and number of queens to place
        
    Returns:
        list or None: A 1D array representing a solution, where solution[i] is the 
                     column position of the queen in row i, or None if no solution exists
    """

    # initialize board 
    board = []

    def place():
        """
        Recursively places a queen on the board. Quits upon finding the first solution.

        Parameters:

        Returns:
            list or None: A 1D array representing a solution, where solution[i] is the 
                     column position of the queen in row i, or None if no solution exists
        """

        # return if solution
        if len(board) == n:
            return board.copy()

        # go through each row
        for col in range(n):
            # check if safe
            if not is_safe(board, len(board), col):
                continue

            # place queen
            board.append(col) 

            # see if next row solves
            res = place()
            if res:
                return res
            
            # backtrack
            board.pop()
      
        # no solutions on this branch
        return None
 
    # place first queen and return result of recursion
    return place() 

def find_all_solutions(n=8):
    """
    Find all solutions to the n-queens problem.
    
    Parameters:
        n (int): The size of the board and number of queens to place
        
    Returns:
        list: A list of solutions, where each solution is a 1D array where
              solution[i] is the column position of the queen in row i
    """
    
    # initialize board 
    board = []
    solutions = []

    def place():
        """
        Recursively places a queen on the board. Appends found solutions to solutions 
        (list), and doesn't quit upon finding a single solution.

        Parameters:

        Returns:
        """
        
        # return if solution
        if len(board) == n:
            solutions.append(board.copy())
            return

        # go through each row
        for col in range(n):
            # check if safe
            if not is_safe(board, len(board), col):
                continue

            # place queen
            board.append(col) 

            # see if next row solves
            res = place()
            
            # backtrack
            board.pop()
      
        # no solutions on this branch
        return
 
    # place the first queen
    place()

    # return the populated solutions list
    return solutions

def board_to_string(board):
    """
    Convert a board configuration to a string representation.
    
    Parameters:
        board (list): A 1D array where board[i] represents the column position 
                     of the queen in row i
                     
    Returns:
        str: A string representation of the board with 'Q' for queens and '.' for empty squares
    """

    # initialize string
    res = ""

    # go through each row
    for row in board:
        # go through each column
        for col in range(len(board)):
            # print a queen if found, dot otherwise
            if col == row:
                res += "Q" 
            else:
                res += "." 
        res += "\n"

    return res

def count_solutions(n=8):
    """
    Count the number of solutions to the n-queens problem.
    
    Parameters:
        n (int): The size of the board and number of queens to place
        
    Returns:
        int: The number of solutions
    """

    return len(find_all_solutions(n))

def is_valid_solution(board):
    """
    Check if a board configuration is a valid solution to the n-queens problem.
    
    Parameters:
        board (list): A 1D array where board[i] represents the column position 
                     of the queen in row i
                     
    Returns:
        bool: True if the board is a valid solution, False otherwise
    """

    def is_valid(row, col):
        """
        Wraps is_safe by checking for validity of a single queen.

        Parameters:
            row (int): The row to check
            col (int): The column to check

        Returns: True if the queen is in a valid position, False otherwise
        """

        # check if column is valid
        if col >= len(board):
            return False

        # check if position is safe 
        return is_safe(board, row, col)

    # check all queens    
    return all([is_valid(row, col) for row, col in enumerate(board)])

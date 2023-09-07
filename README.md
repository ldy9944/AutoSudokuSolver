# Sudoku Solver with Tkinter

## History and Popularity of Sudoku

Sudoku originated in the late 19th century but gained massive popularity in the 2000s. The game tests your logical and numerical arrangement skills and has become a staple in many newspapers and online platforms. Despite its simple rules, Sudoku requires deep strategic thinking, which has contributed to its global popularity.

## Drawbacks and Challenges of Sudoku

### Time-Consuming

Sudoku puzzles can often take a considerable amount of time to solve, especially those of higher difficulty levels. This can result in decreased productivity and requires long periods of focus.

### Repetitive

The game relies on the same logic and patterns, making it monotonous after a certain period. This contrasts with other brain games that require creative thinking.

### Inefficient

Solving it manually means you have to try out multiple possibilities and spot errors, making the process inefficient. Mistakes can easily happen, leading to restarting the puzzle.

## Features and Working Principles of the Code

### Automatic Solution

This code uses a Tkinter GUI to take Sudoku puzzles from the user and solves them automatically, significantly mitigating the aforementioned drawbacks.

### Validation Checks

The `is_valid_move` function pre-checks if a number can be placed at a particular location, reducing the chances of user errors.

### Recursive Algorithm

The `solve_sudoku` function finds empty cells recursively and fills them with valid numbers. The algorithm is a form of backtracking algorithm, making it highly efficient.

### Input Validation

The `read_board` function validates the user input, minimizing errors. For instance, if a character or special symbol is input, it treats it as zero.

### UI and Logic Separation

The UI and Sudoku-solving logic are well-separated, making the code clean and easier to maintain.

## How to Use the Program

1. Run the Python script.
2. A Tkinter window will open displaying a 9x9 grid.
3. Fill in the initial Sudoku numbers in the grid.
4. Click the 'Go' button to solve the Sudoku.
5. The solved Sudoku will appear on the grid.
6. To reset the grid, click the 'Reset' button.

Enjoy solving your Sudoku puzzles!

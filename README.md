# AI_Project2
# NQueens-Problem-Solver

This is a **Python** implementation of the **N-Queens** Problem using Hill Climbing and Random-Restart Hill Climbing both with and without sideways moves. The program allows users to input the number of queens and number of times you want to run the algorithm. Then select an algorithm variant and observe the solving process.

## Group Members 
- Parth Patel
- Sai Priyanka Taduri

## Features

- Implements different Hill Climbing strategies to solve the N-Queens problem:
  - Hill Climbing
  - Hill Climbing with Sideways Moves
  - Random-Restart Hill Climbing
  - Random-Restart Hill Climbing with Sideways Moves
- Displays step-by-step placement of queens on the board.
- Shows performance metrics, including:
  - Success and failure rates
  - Average number of steps taken
  - Average Number of restarts (for Random-Restart approaches)

---

## Getting Started

### Prerequisites

Ensure you have **Python 3.x** installed. You can check your current version by running:

```bash
python3 --version
```
## Installation & Running the Program

### Clone the Repository:

```bash
git clone https://github.com/parth448812/NQueens-Problem-Solver.git
cd NQueens-Problem-Solver
```
### Run the Solver:

```bash
python3 nqueens_solver.py
```

### Provide Input:

- Enter the number of queens (minimum 4).
- Enter the number of times you want to run the program.
- Choose an algorithm:
  - Enter `1` for **Hill Climbing**.
  - Enter `2` for **Hill Climbing with Sideways Moves**.
  - Enter `3` for **Random-Restart Hill Climbing**.
  - Enter `4` for **Random-Restart Hill Climbing with Sideways Moves**.

### View the Output:

- The program will display the **step-by-step board states**.
- It will also print:
  - **Success and failure rates**.
  - **Average number of steps taken**.
  - **Average Number of restarts (for Random-Restart approaches)**.

### Example Run

#### Input:

```bash
Enter the number of queens (minimum 4): 8
Enter the number of runs: 4

Select algorithm:
1. Hill Climbing
2. Hill Climbing with Sideways Moves
3. Random-Restart Hill Climbing
4. Random-Restart Hill Climbing with Sideways Moves
Enter choice (1-4): 1
```
#### Output:

```bash
Run 1:

Random Initial State: Current heuristic: 10
 .  .  .  .  .  .  .  . 
 Q  Q  .  Q  .  .  .  . 
 .  .  Q  .  .  .  .  Q 
 .  .  .  .  .  .  .  . 
 .  .  .  .  .  .  .  . 
 .  .  .  .  .  Q  Q  . 
 .  .  .  .  .  .  .  . 
 .  .  .  .  Q  .  .  . 


Step 1: Current heuristic: 6
 .  .  .  .  .  .  .  . 
 Q  Q  .  Q  .  .  .  . 
 .  .  .  .  .  .  .  Q 
 .  .  .  .  .  .  .  . 
 .  .  .  .  .  .  .  . 
 .  .  .  .  .  Q  Q  . 
 .  .  Q  .  .  .  .  . 
 .  .  .  .  Q  .  .  . 

...

Final Statistics:
Success Rate:        25.00%
Failure Rate:        75.00%
Avg Success Steps:   4.00
Avg Failure Steps:   2.67
 

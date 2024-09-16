# Dynamic Programming

## Overview
- Dynamic Programming is an algorithmic technique for solving optimization problems by breaking them down into simpler sub-problems that overlap.
- We store the previously calculated values in order to avoid repetitive calculations.


## When to use Dynamic Programming
To use Dynamic Programming we need to have overlapping sub-problems and optimal substructure:

### Overlapping Subproblems
- This means the problem can be broken down into smaller subproblems, which are reused multiple times.
- Imagine you have a large puzzle, and you solve smaller sections of it repeatedly to complete the whole puzzle.

### Optimal Substructure
- The optimal solution for a problem of a given size is based on the optimal solution for smaller-sized problems.
- Think of it like building a house: the strength of the entire house depends on the strength of each individual brick.


## Dynamic Programming Methods
There are two methods for dynamic programming

### Bottom-Up Approach (Tabulation)
- This method involves solving all possible subproblems first and storing their solutions in a table (usually an array).
- You then use these stored solutions to build up the solution to the original problem.
- It's like filling out a table row by row, ensuring you have all the data you need before moving to the next row.

### Top-Down Approach (Memoization)
- This method involves solving the problem by breaking it down into subproblems and solving each subproblem only once, storing the results to avoid redundant work.
- It's like having a checklist where you mark off tasks as you complete them, so you don't repeat any task.


## Application of Dynamic Programming
- Resource Management
- Distribution Problems
- Text Comparison Problems
- Path finding algorithms such as Floyd's algorithm
- Financial modeling
- Statistical Analysis
- Constructing Optimal Search trees.
- Genome Matching



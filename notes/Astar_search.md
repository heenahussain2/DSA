## A* Search Algorithm
- A* search uses a heuristic to determine the likely best choice for the next step of the algorithm. The use of heuristic is how A* is different from other path finding algorithms
- A **heuristic** is often informally defined as a rule if thumb.
- In the case of the A* Algorithm, the rule of thumb is to choose the next position to visit based on its distance from the goal.
- This distance is calculated using the Manhattan distance or Euclidean distance
- **Manhattan distance** or taxi-cab distance. which means the distance between the points on a 2D grid. It is based on the idea that a taxi will have to drive around buildings and not through it.
- Taxi cab distance between 2 points is measured along the axes at right angles.
- It doesn't matter what path you take, the Manhattan distance will remain the same.

###  Key Terms
- In A* algorithm, every discovered cell is assigned the following values.
    - **G value**: best distance from start to current cell.
    - **H value**: heuristic distance from current cell to destination
    - **F value**: The sum of the G value and H value (representing the probable optimal value or minimum distance based on the heuristic used)
- **Discovered nodes**
    - Discovered nodes are the ones that are in the priority queue but it does not mean that they have been visited.
    - An Open set contains the discovered nodes
- **Visited nodes**
    - Visited nodes are the one that have already been stored in G values dictionary and predecessors dictionary.
    - A closed set contains visited nodes.

### Pseudocode
- variables: 
    - `G-values`: `dict`  `{ cell: G-value or distance from the starting node}`
    - `Predecessors`: `dict` predecessors of the visited nodes. 

- PQ: [(cell, F-value)]
- Get Highest priority item from PQ (min F-value)
- Is it the goal?
- If so we are done
- Otherwise:
    - put undiscovered neighbors in PQ and calculate F-values
    - update predecessors
- Repeat until the PQ is empty.

### Applications of A* Search
- Traffic Navigational System (for ex GPS)
- Social Network Analysis
- Natural Language Processing
- Machine Learning
- Puzzle solutions and puzzle analogous problems
- Algorithmic Trading
- Robotics
- Video Games
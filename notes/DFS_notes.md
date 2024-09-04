## Depth First Search (DFS)

- DFS or Depth First Search is an algorithm where you continue down a path until you either find the goal or reach the end.
- If it reaches a dead end without finding its goal, it backtracks to the last viable position and tries a different path from there.
- DFS is better in situations where the goal is to discover a path to a given destination as soon as possible. 
- This does not guarantee finding the shortest path.

### Applications of DFS
- Optimizations for criteria (cost, speed, safety, fuel).
- Path finding.
- Scheduling Algorithms
- Assessing investment decision trees
- Ordering of formula cell evaluation in spreadsheets.
- Determining the order of compilation tasks for software builds.
- Data Serialization.
- Resolving symbol dependencies.
- Simulating games

### DFS Pseudocode
- We have a stack containing just the start position. `Stack: [start_pos]`
- We also have a dictionary containing the predecessors of discovered cells. `Predecessors: {start_pos: None}`

#### Algorithm
- Take the top item of the stack or Pop the stack
- Is this the goal?
- If so, we are done.
- Otherwise, push undiscovered neighbors onto the stack and add them to the predecessors/discovered.
- The neighbors are pushed in the order - we go clockwise starting from up
- So we are going up, right, down and left.
- Repeat while all the items all still on the stack 



 

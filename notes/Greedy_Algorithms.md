## Greedy Algorithms
- A greedy algorithm makes locally optimal choices at any given point and once the choice is made it cannot be revisited.
- This makes the algorithm "short sighted", and it may not find the optimal solution. It may also fail on some instances of a solution.
- There are some advantages to the greedy algorithm:
    - It is quite fast
    - Relatively easy to implement


### Dijkstra's Algorithm
#### Pseudocode
- While any vertex remains unvisited:
    - Visit unvisited vertex with smallest known distance from the start vertex. Call this current_vertex
    - For each unvisited neighbor of current vertex:
        - Calculate the new distance from the start vertex if this route is taken.
        - If the calculated distance of this vertex is less than the known distance:
            - Update the distance for this neighbor.


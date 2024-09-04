## Breadth First Search (BFS) Algorithm

- The BFS algorithm is implemented using queue Data Structure
- It is like having the centre of a circle and then moving out to different radii or distances from that central point as the algorithm progresses.
- BFS will always give the shortest path if no edge weights are used.
- This is because it first finds all the vertices that are one edge away from the starting point, then two edges away and so on, until it reaches a goal.
- When you find the goal vertex, you know the path you have traced so far is the shortest path to a node. If there were a shorter path then BFS would have found that already.


### Applications of Breadth First Search (BFS)
- GPS Systems
- Flight reservation systems
- Finding neighbor nodes in peer-to-peer networks
- Social networking sites to find connections between users
- Web crawlers
- Applications in Artificial Intelligence
- Electronics and Communication Engineering
- Scientific modelling


### BFS Algorithm
- In BFS we use a queue data structure for adding and removing discovered nodes
- The queue contains the initial cell and we also have a list of predecessors
- Dequeue
- Is this the goal?
- If so we are done.
-       Else, enqueue undiscovered neighbors and update predecessors.
- Repeat until the queue is empty.
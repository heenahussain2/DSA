## Queue Data Structure
- A queue in computing is very similar to a queue in real life in which you have to maintain an arrival order.
- It follows FIFO pattern - First in First Out
- Additions are made from the rear or tail of the queue 
- Deletions are made from the front or head of the queue.

### Queue Operations
- `enqueue()`: add an item to the end of the queue.
- `dequeue()`: remove an item from the front of the queue

### Application of Queue
- CPU Scheduling
- Data transferred between two processes and we need a way of maintaining the original order.
- Graph Traversal Algorithms
- Transport and operations management.
- File servers
- I/O Buffers
- Printer Queues
- Phone calls to customer service hotlines.
- Often when a resource is shared a,ong multiple customers


## Priority Queue
- A priority queue is a data structure where the items can be added at any time but only the item with the highest priority can be removed.
- This structure is particularly useful in scenarios where resources need to be allocated based on priority.

### Priority Queue Operations
- `get()` : Retrieves the item with the highest priority
- `put()`: Adds an item to the queue (like enqueue)
- `is_empty()`: checks if the queue is empty

### Applications of Priority Queue
- Artificial Intelligence - for ex A* search Algorithm
- Optimization Algorithms
- Operating System Process Scheduling
- Bandwidth Management
- Statistical Analysis
- Spam filtering
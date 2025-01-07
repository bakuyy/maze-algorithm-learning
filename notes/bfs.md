# Breadth First Search (BFS)

- BFS searches for all children of one node, then moves onto the next node (level by level).
- Goal: Find the shortest path between any two given nodes.

## DS: Queue

- Data structure used for the collection of objects based on FIFO (first in, first out) principle.
    - The first item stored in the queue is the first item out.
    
<img src="./images/queue" width="400" />

- **Similar DS: Dequeue**
    - Can push and pop from both sides.
    
<img src="./images/dequeue" width="400" />

- There is no built-in queue in Python, so we can either import the `queue` library or use lists:
    - `append()` pushes an item in.
    - `pop(0)` returns the first item in the list.

## Pseudocode

- Initialize a queue: `Frontier`
- Initialize a list: `Explored`
- Add the start cell in both `Frontier` and `Explored`
- Repeat while the target hasn’t been reached or there are still elements in `Frontier`:

```python
currCell = Frontier.pop(0)
for each direction (E, S, N, W):  # order doesn't matter as long as you add all applicable paths
    childCell = Next possible cell
    if childCell is already in explored:
        # do nothing
    else:
        # append/push the childCell into both explored and frontier

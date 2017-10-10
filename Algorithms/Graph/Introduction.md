# Graph Representations

* Adjacency Matrix
* Adjacency List

### Breadth First Traversal or BFS

Similar to BFS in tree, Just to avoid cycles, we use a boolean visited array

```python
def breadth_first_search(problem):

  # a FIFO open_set
  open_set = Queue()
  # an empty set to maintain visited nodes
  closed_set = set()
  # a dictionary to maintain meta information (used for path formation)
  meta = dict()  # key -> (parent state, action to reach child)

  # initialize
  start = problem.get_start_state()
  meta[start] = (None, None)
  open_set.enqueue(start)

  if problem.is_goal(start):
    return construct_path(start, meta)

  while not open_set.is_empty():

    parent_state = open_set.dequeue()

    for (child_state, action) in problem.get_successors(parent_state):
      if child_state in closed_set:
        continue

      if child_state not in open_set:
        meta[child_state] = (parent_state, action)
        if problem.is_goal(child_state):
          return construct_path(child_state, meta)

        open_set.enqueue(child_state)
    
    closed_set.add(node)


def construct_path(state, meta):
  action_list = list()
  
  while True:
    row = meta[state]
    if len(row) == 2:
      state = row[0]
      action = row[1]
      action_list.append(action)
    else:
      break
  
  return action_list.reverse()
```

### Depth First Traversal or DFS

Similar to DFS in tree, Just to avoid cycles, we use a boolean visited array


```c
void Graph::DFSUtil(int v, bool visited[])
{
    // Mark the current node as visited and print it
    visited[v] = true;
 
    // Recur for all the vertices adjacent to this vertex
    list<int>::iterator i;
    for (i = adj[v].begin(); i != adj[v].end(); ++i)
        if (!visited[*i])
            DFSUtil(*i, visited);
}
 
// DFS traversal of the vertices reachable from v. 
// It uses recursive DFSUtil()
void Graph::DFS(int v)
{
    // Mark all the vertices as not visited
    bool *visited = new bool[V];
    for (int i = 0; i < V; i++)
        visited[i] = false;
 
    // Call the recursive helper function to print DFS traversal
    DFSUtil(v, visited);
}
```

### Credits

* [Wikipedia](https://en.wikipedia.org/wiki/Breadth-first_search)
* [Geeks For Geeks](http://www.geeksforgeeks.org/depth-first-traversal-for-a-graph/)
# AI : Problem Solving
 
### Definition of a Problem
 
* Initial state
* Actions($$s$$) -> $$\{a1, a2, a3 ...\}$$
* Result($$s, a$$) -> $$s$$
* GoalTest($$s$$) -> True/False
* PathCost($$s_1->a_1->s_2->a_2->s_3$$) -> $$n$$
* StepCost($$s, a, s^1$$) -> $$n$$

```code
  function GraphSearch(Problem)
     frontier = {initial}, explored = {}
     loop:
        if frontier is empty: return Fail
        path = remove_choice(frontier)
        s = path.end, explored += {s}
        if s is goal: return path
        for a in actions:
           add [path + a -> Result(s, a)] to frontier if Result(s, a) is not in explored
```

The `remove_choice` function above decides the entire algorithm, Possible options are

* BFS
* DFS


Problems with above approach of algorithms is the search is not direct towards the goal, instead we are searching all the nodes level by level, How can we optimize this by making it more goal oriented?

### A* Algorithm

Similar to BFS A* also expands based on minimum cost function

$$f = g + h$$

g(path) signifies path cost
h(state) signifies estimated distance to goal

A* finds lowest cost path if h(s) < true cost

Heuristic function is admissible if h(s) less than equal to true cost, rather than necessarily being strictly smaller than the true cost
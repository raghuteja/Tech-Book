# Priority Queue STL implementations

#### Declaring Max Heap with default data types
```
priority_queue<int> p(vector.begin(), vector.end());
```


#### Declaring Min Heap with some struct

```
struct ListNode {
    int val;
    ListNode *next;
    ListNode(int x) : val(x), next(NULL) {}
};
```

```
class MyComparator {
public:
    int operator() (const ListNode* l1, const ListNode* l2) {
        return l1->val > l2->val;
    }
};
```

```
priority_queue<ListNode*, vector<ListNode*>, MyComparator> p;
```

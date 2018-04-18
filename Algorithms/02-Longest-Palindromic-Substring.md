# Longest Palindromic Substring

### Brute Force

Check for every substring if it is palindrome

**Time Complexity :** $$O(N^3)$$
**Space Complexity :** $$O(1)$$


### Dynamic Programming

Maintain a boolean 2D matrix and store if sub string from i to j is palindrome or not by using value of i+1 to j-1

**Time Complexity :** $$O(N^2)$$
**Space Complexity :** $$O(N^2)$$

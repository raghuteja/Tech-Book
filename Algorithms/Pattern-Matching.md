# Pattern Matching Problem

### Problem

Given a pattern and text, find the occurrences of pattern in the text

### Algorithm

#### Rabin-Karp Algorithm
Every string s[] of length m can be seen as a number H written in a positional numeral system in base B (B >= size of the alphabet used in the string):

H = s[0] * B {% sup %} (m – 1) {% endsup %} + s[1] * B {% sup %} (m – 2) {% endsup %} + … + s[m - 2] * B {% sup %} 1 {% endsup %} + s[m - 1] * B {% sup %} 0 {% endsup %}

If we calculate the number H (the hash value) for the pattern and the same number for every substring of length m of the text than the inner loop of the "naive" method will disappear – instead of comparing two strings character by character we will have just to compare two integers.

A problem arises when m and B are big enough and the number H becomes too large to fit into the standard integer types. To overcome this, instead of the number H itself we use its remainder when divided by some other number M. To get the remainder we do not have to calculate H.

For the sub string starting from i

H{% sub %}i{% endsub %} = ( Hi – 1 – s[i- 1] * Bm - 1 ) * B + s[i + m - 1]

### Implementation

### Source
* [TopCoder](https://www.topcoder.com/community/data-science/data-science-tutorials/introduction-to-string-searching-algorithms/)

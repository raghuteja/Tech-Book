# Pattern Matching Problem

### Problem

Given a pattern and text, find the occurrences of pattern in the text

### Algorithm

#### Rabin-Karp Algorithm
Every string s[] of length m can be seen as a number H written in a positional numeral system in base B (B >= size of the alphabet used in the string):

$$
H = s[0] * B {% sup %} (m – 1) {% endsup %} + s[1] * B {% sup %} (m – 2) {% endsup %} + … + s[m - 2] * B {% sup %} 1 {% endsup %} + s[m - 1] * B {% sup %} 0 {% endsup %}
$$


### Implementation

### Source

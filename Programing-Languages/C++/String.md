# Useful String functions

**Length of a String**

```
str.length();
```

**Check if a character is alphanumeric**
```
#include <ctype.h>
isalnum(c);
```

**Convert a character to upper case**
```
#include <ctype.h>
toupper(c);
```

**Append a character to String**

```
str.push_back(c);
```

**Convert string to int**

```
stoi(string);
```

**Convert int to string**

```
to_string(integer);
```

**Append String to String**

```
str1.append(str2);
```

**Append anything to String**

```
stringstream ss;
ss << integer;
ss << string;
ss << character;
ss.str();
```

**Reverse a String**
```
reverse(str.begin(), str.end());
```

**Erase characters in string**
```
str.erase(index_of_first_char_to_remove, num_chars)
```
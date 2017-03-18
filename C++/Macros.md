# Macros

### Example

```
#define mac(x) f1(x); f2(x)
```

On using the above macro
```
mac(x);
```
equivalent to
```
f1(x); f2(x)
```
which is expected behaviour


Suppose if we are calling the macro inside if condition
```
if (cond)
    mac(x);
```
equivalent to
```
if (cond)
    f1(x); f2(x);
```
impiles
```
if (cond)
    f1(x);
f2(x);
```
which is not the expected behaviour

So while defining the multi statement macro to avoid such scenarios we will wrap macro with do while(0)

```
#define mac(x)  do { f1(x); f2(x); } while (0)
```

which works as expected
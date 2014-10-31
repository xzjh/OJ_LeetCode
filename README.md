#LeetCode solution by xzjh

###Reverse words in a string

In Python, `split()` is different from `split(' ')`:

- `' '.split(' ')` => `['', '']`
- `' '.split()` => `[]`

###Evaluate reverse polish notation

In Python, `5/6` => `0` but `-5/6` => `-1`.

###Gas station

Max sub-sequence implemented, including non-positive in the sequence.

###Word Ladder

Bi-directional search. Need to ensure to traverse current whole level of nodes in each direction in every iteration.

###First Missing Positive

**Attention to use tuple to swap values in an array!**

*"When a comma-separated list of expressions is supplied, its elements are evaluated from left to right and placed into the list object in that order."* from the [docs](http://docs.python.org/2/reference/expressions.html#list-displays).

So for this example:

`A[i], A[A[i] - 1] = A[A[i] - 1], A[i]`,

in this expression: `A: [2, 3], i: 0`.

```
  2           0 LOAD_FAST                0 (A)
              3 LOAD_FAST                0 (A)
              6 LOAD_FAST                1 (i)
              9 BINARY_SUBSCR
             10 LOAD_CONST               1 (1)
             13 BINARY_SUBTRACT
             14 BINARY_SUBSCR
             15 LOAD_FAST                0 (A)
             18 LOAD_FAST                1 (i)
             21 BINARY_SUBSCR
             22 ROT_TWO
             23 LOAD_FAST                0 (A)
             26 LOAD_FAST                1 (i)
             29 STORE_SUBSCR
             30 LOAD_FAST                0 (A)
             33 LOAD_FAST                0 (A)
             36 LOAD_FAST                1 (i)
             39 BINARY_SUBSCR
             40 LOAD_CONST               1 (1)
             43 BINARY_SUBTRACT
             44 STORE_SUBSCR
             45 LOAD_CONST               0 (None)
             48 RETURN_VALUE
```

Right part of `=` will be evaluated first and we get `(3, 2)` for this part. Then `3` is assigned to `A[i]`, and at this time `A[i]` is `3`. So `A[i] - 1` is `2` which results to index error for expression `A[A[i] - 1]` (which is `A[2]`).
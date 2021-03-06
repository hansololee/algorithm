# Distance Between Bus Stops

A bus has n stops numbered from 0 to n - 1 that form a circle. We know the distance between all pairs of neighboring stops where distance[i] is the distance between the stops number i and (i + 1) % n.
The bus goes along both directions i.e. clockwise and counterclockwise.
Return the shortest distance between the given start and destination stops.

- Example 1:

![untitled-diagram-1](https://user-images.githubusercontent.com/44221590/64686148-28d0e200-d4c3-11e9-9c08-8a69749600a5.jpg)

```
**Input**: distance = [1,2,3,4], start = 0, destination = 1
**Output**: 1
**Explanation**: Distance between 0 and 1 is 1 or 9, minimum is 1.
```

- Example 2:

![untitled-diagram-1-1](https://user-images.githubusercontent.com/44221590/64686155-2bcbd280-d4c3-11e9-8e8e-404be0f2ce87.jpg)

```
**Input**: distance = [1,2,3,4], start = 0, destination = 2
**Output**: 3
**Explanation**: Distance between 0 and 2 is 3 or 7, minimum is 3.
```

- Example 3:

![untitled-diagram-1-2](https://user-images.githubusercontent.com/44221590/64686157-2d959600-d4c3-11e9-9404-386bfa28ad1a.jpg)

```
**Input**: distance = [1,2,3,4], start = 0, destination = 3
**Output**: 4
**Explanation**: Distance between 0 and 3 is 6 or 4, minimum is 4.
``` 

- Constraints:

```
1 <= n <= 10^4
distance.length == n
0 <= start, destination < n
0 <= distance[i] <= 10^4
```

## My Result

**Runtime**: 56 ms, faster than 66.70% of Python3 online submissions for Distance Between Bus Stops.

**Memory Usage**: 14.6 MB, less than 100.00% of Python3 online submissions for Distance Between Bus Stops.

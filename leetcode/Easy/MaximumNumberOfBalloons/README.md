# Maximum Number of Balloons

Given a string text, you want to use the characters of text to form as many instances of the word "balloon" as possible.
You can use each character in text at most once. Return the maximum number of instances that can be formed.

- Example 1:

![1536_ex1_upd](https://user-images.githubusercontent.com/44221590/65222064-47555f80-daf9-11e9-8947-31349e74f490.jpg)

```
Input: text = "nlaebolko"
Output: 1
```

- Example 2:

![1536_ex2_upd](https://user-images.githubusercontent.com/44221590/65222065-47555f80-daf9-11e9-9aa9-8b8ddd3364ce.jpg)

```
Input: text = "loonbalxballpoon"
Output: 2
```

- Example 3:

```
Input: text = "leetcode"
Output: 0
```

- Constraints:

```
1 <= text.length <= 10^4
text consists of lower case English letters only.
```

## My Result

**Runtime**: 468 ms, faster than 7.89% of Python3 online submissions for Maximum Number of Balloons.

**Memory Usage**: 13.9 MB, less than 100.00% of Python3 online submissions for Maximum Number of Balloons.

## TODO

- while 안에 for 안에 in. 시간복잡도 고려 문제였으면 시간초과.

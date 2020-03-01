#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the alternatingCharacters function below.
# Easy

def alternatingCharacters(s):
    before_char = s[0]
    count = 0
    for char in s[1:]:
        if char == before_char:
            count +=1
        else:
            before_char = char

    return count


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    q = int(input())

    for q_itr in range(q):
        s = input()

        result = alternatingCharacters(s)

        fptr.write(str(result) + '\n')

    fptr.close()


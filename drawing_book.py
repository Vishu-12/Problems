#question-
#https://www.hackerrank.com/challenges/one-month-preparation-kit-drawing-book/problem?h_l=interview&isFullScreen=true&playlist_slugs%5B%5D%5B%5D=preparation-kits&playlist_slugs%5B%5D%5B%5D=one-month-preparation-kit&playlist_slugs%5B%5D%5B%5D=one-month-week-two&h_r=next-challenge&h_v=zen

#Solution:-

#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'pageCount' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER n
#  2. INTEGER p
#

def pageCount(n, p):
    # Write your code here
    start=p//2
    d=n-p
    if n%2!=0:
        end=(n-p)//2
    else:
        if d==1:
            end=(d//2)+1
        elif d>1:
            end=d//2
        else:
            end=0
    
    if start>end:
        return end
    else:
        return start
        

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    p = int(input().strip())

    result = pageCount(n, p)

    fptr.write(str(result) + '\n')

    fptr.close()

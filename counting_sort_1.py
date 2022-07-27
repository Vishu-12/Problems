#Question:-
#https://www.hackerrank.com/challenges/one-week-preparation-kit-countingsort1/problem?h_l=interview&isFullScreen=true&playlist_slugs%5B%5D%5B%5D=preparation-kits&playlist_slugs%5B%5D%5B%5D=one-week-preparation-kit&playlist_slugs%5B%5D%5B%5D=one-week-day-two


#Solution:-

#!/bin/python3

import math
import os
import random
import re
import sys
from collections import Counter

#
# Complete the 'countingSort' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts INTEGER_ARRAY arr as parameter.
#

def countingSort(arr):
    result=[]
    a=max(arr)
    s=dict(Counter(arr))
    
    for i in range(100):
        if i in s:
            result.append(s[i])    
        else:
            result.append(0)
    return result
    
                    
        
    

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    result = countingSort(arr)

    fptr.write(' '.join(map(str, result)))
    fptr.write('\n')

    fptr.close()


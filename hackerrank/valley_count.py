import math
import os
import random
import re
import sys

#
# Complete the 'countingValleys' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER steps
#  2. STRING path
#

def countingValleys(steps, path):
    # Write your code here
    hike = 0
    valley_flag = False
    valley_count = 0
    for step in path:
        if(step == 'U'):
            hike +=1
        else:
            hike -=1
        if(hike <0 and valley_flag is False):
            valley_flag = True
            valley_count +=1
        if(hike >=0):
            valley_flag =False
    return valley_count        

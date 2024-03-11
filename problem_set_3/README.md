# Problem Set 3: Longest Increasing Subsequence

## Problem Description

Given an unsorted array of integers, find the length of the longest increasing subsequence.

## Solution Overview

For this solution, the first step was to initialize a cache/list with all the values as 1
with a length of the input array. Then it iterates over the input array but in reverse order.
Inside this loop, it iterates starting from the next value after (i) to the end of the input array.
It then checks if the value at (i) is less than the value at (j) (this means that the number after i
in the array is greater than the value at i meaning it can form a increasing subsequence). If it does,
LIS[i] is update with the max value between LIS[i] and 1 + LIS[j] to make sure that the largest
possible increasing subsequence is taken.

## Instructions to Run the Code

Code could be run by entering "python longest-increasing-subsequence.py" in a terminal opened in the directory
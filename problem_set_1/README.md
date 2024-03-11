# Problem Set X: Palindrome Pairs

## Problem Description

Given a list of unique words, your task is to find all pairs of distinct indices (i, j) in the list so that
the concatenation of the two words, i.e., words[i] + words[j], forms a palindrome.

## Solution Overview

First I created a function to check if a string is a palindrome.
Then I created a function that iterates over the words in the input array and checks if their concatenation (words[i] + words[j])
is a palindrome using the initial function. It then stores the pair [i, j] to the list palindromes but it checks first if [j, i]
already exists in the list before storing to make sure that the pairs are distinct.

## Instructions to Run the Code

Code could be run by entering "python palindrome-pairs.py" in a terminal opened in the directory


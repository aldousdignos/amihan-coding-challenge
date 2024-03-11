# Problem Set X: Valid Parentheses

## Problem Description

Given a string containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is
valid. An input string is valid if:
1. Open brackets must be closed by the same type of brackets.
2. Open brackets must be closed in the correct order.

## Solution Overview

Firstly, the isValid function initializes a bracket map that has the closing brackets as the keys
and the opening brackets as the values and also an empty list(stack). It then iterates over every character 
in the string and uses an if elif to check if the character is a value in the bracket map or a key 
(whether it is an opening bracket or a closing bracket). If it is an opening bracket, add it to the stack,
if not, it checks the top of the stack to check if the the current closing bracket matches a corresponding
opening bracket (this is to make sure that the brackets are closed in the correct order) if not it returns
False. If it does, it pops the stack to remove the last element and after all iterations, if the stack is
empty, the function returns True, and False if not.

## Instructions to Run the Code

Code could be run by entering "python validate-parentheses.py" in a terminal opened in the directory

def isPalindrome(s: str) -> bool:
    return s == s[::-1]

def palindromePairs(words):
    length = len(words)
    palindromes = []
    for i in range(length):
        for j in range(length):
            if i != j:
                if isPalindrome(words[i] + words[j]) and [j, i] not in palindromes:
                    palindromes.append([i, j])
    return palindromes

input_words = ['tac', "tab", "cat", "bat"]
result = palindromePairs(input_words)
print(result)
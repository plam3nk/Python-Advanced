def palindrome(word, start_index, last_index=-1):
    if start_index == len(word) // 2:
        return f"{word} is a palindrome"
    if word[start_index] != word[last_index]:
        return f"{word} is not a palindrome"

    return palindrome(word, start_index + 1, last_index - 1)


print(palindrome("abcba", 0))
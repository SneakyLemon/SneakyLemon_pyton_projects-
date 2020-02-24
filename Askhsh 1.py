from itertools import count

def reverse(string):
    string = string[::-1]
    return string

def longest_word(lst):
    cnt = count()
    return sorted(lst, key = lambda w : (len(w), next(cnt)), reverse = True)[:5]

def rem_vowels(string):
    vowels = ('A','E','I','O','U','a', 'e', 'i', 'o', 'u')
    for x in string.lower():
        if x in vowels:
            string = string.replace(x, "")
    return string

with open("text.txt") as file:
    lines = file.read().split()
    biggestwords = longest_word(lines)
    for word in biggestwords:
        print(rem_vowels(reverse(word)))

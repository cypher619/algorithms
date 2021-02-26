def split(word):
    return [char for char in word]

def count(words):
    d=dict()

    for word in words:

        if word in d:
            d[word] = d[word] + 1
        else:
            d[word] = 1
    if len(d) == 26:
        return "YES"
    else:
        return "NO"


n = int(input())
word = input()
word=word.upper()
print(count(split(word)))

def word_count(str):
    counts = dict()
    words = str.split()
    for word in words:
        if word in counts:
            counts[word] += 1
        else:
            counts[word] = 1
    return counts
f = open("sample.txt", "r")
message = f.read()
print(word_count(message))
print("\n")

with open('sample.txt')as infile:
    lines=0
    words=0
    characters=0
    for line in infile:
        wordlist=line.split()
        lines=lines+1
        words=words+len(wordlist)
        characters+=sum(len(word)for word in wordlist)
print("Number of lines:",lines)
print("Number of words:",words)
print("Number of char:",characters)

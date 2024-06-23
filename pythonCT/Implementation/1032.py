n = input()
word = list(input())

for _ in range(int(n)-1):
    word2 = input()
    for idx in range(len(word2)):
        if word[idx] == word2[idx]:
            continue
        else:
            word[idx] = "?"

print("".join(word))
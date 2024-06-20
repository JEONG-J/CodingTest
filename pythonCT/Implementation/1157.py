word = input().upper()
set_word = list(set(word))
save_count = []

for i in set_word:
    save_count.append(word.count(i))

result_max = max(save_count)

if save_count.count(result_max) > 1:
    print("?")
else :
    result_idx = save_count.index(result_max)
    result = set_word[result_idx]
    print(result)
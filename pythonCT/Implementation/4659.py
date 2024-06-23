rule = ['a', 'e', 'i', 'o', 'u']

while(1):
    word = input()
    if word == "end":
        break
    else:
        cnt = 0
        errorOne = errorTwo = 0
        for i in rule:
            if i in word:
                cnt += 1
        if cnt < 1:
            print("<{}> is not acceptable.".format(word))
        else:
            for idx in range(len(word) - 1):
                if word[idx] == word[idx+1]:
                    if word[idx] == 'e' or word[idx] == 'o':
                        continue
                    else:
                        errorOne = 1
            if errorOne == 1:
                print("<{}> is not acceptable.".format(word))
                continue

            for idx in range(len(word) - 2):
                if word[idx] in rule and word[idx+1] in rule and word[idx+2] in rule:
                    errorTwo = 1
                elif not(word[idx] in rule) and not(word[idx+1] in rule) and not(word[idx+2] in rule):
                    errorTwo = 1
            if errorTwo == 1:
                print("<{}> is not acceptable.".format(word))
                continue
            
            print("<{}> is acceptable.".format(word))


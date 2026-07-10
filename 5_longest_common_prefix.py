strs = ['flower', 'fly', 'flight']
res = ''

for i in range(len(strs[0])):
    char = strs[0][i]
    for word in strs:
        if i == len(word) or word[i] != char:
            print(res)
            break
    else:
        res += char
        continue
    break
else:
    print(res)
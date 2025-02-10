target = int(input())
alpha = [0]*26
for _ in range(target):
    word = input()
    alpha[ord(word[0]) - ord('a')] += 1

result = []
for i in range(26):
    if alpha[i] >= 5:
        result.append(chr(i + ord('a')))
if not result:
    print('PREDAJA')
else:
    print("".join(result))

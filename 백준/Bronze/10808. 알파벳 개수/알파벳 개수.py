from collections import Counter

word = input().strip()
count = Counter(word)

result =[count[chr(i)] for i in range(ord('a'), ord('z')+1)]
print(*result)

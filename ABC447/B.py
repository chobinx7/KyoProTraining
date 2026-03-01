# S = input()
# for i in range(len(S)):
# print(S[i])
# char = max(S)
# S.pop(char)
# print(S)
# ここまでで分からなくなった

# Claudeに作成してもらったコード
from collections import Counter

S = input()
cnt = Counter(S)
max_count = max(cnt.values())
remove = {c for c, n in cnt.items() if n == max_count}
print("".join(c for c in S if c not in remove))

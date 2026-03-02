N, L = map(int, input().split())
S = []
for i in range(N):
    s = input()
    S.append(s)
# print(S)
ans = sorted(S)
# print(ans)
result = ""
for j in ans:
    result += j
print(result)

# 文字列の並び替えはsorted()を使用する！

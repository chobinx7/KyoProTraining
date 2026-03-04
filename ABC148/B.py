N = int(input())
S, T = map(str, input().split())
# print(S, T)
mergeList = []
# print(mergeList)
for i in range(N):
    mergeList += S[i]
    mergeList += T[i]
# print(mergeList)
ans = "".join(mergeList)
print(ans)

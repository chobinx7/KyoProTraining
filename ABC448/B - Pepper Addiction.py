# N = 料理の数　M = 胡椒の種類
N, M = map(int, input().split())
# C = M種類の胡椒のグラム数
C = list(map(int, input().split()))
ans = 0
for i in range(N):
    # A = Cのindex B = 上限グラム
    A, B = map(int, input().split())
    if C[A - 1] >= B:
        C[A - 1] -= B
        ans += B
    elif C[A - 1] < B:
        pass
print(ans)

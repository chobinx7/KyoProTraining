N, P = map(int, input().split())
student = list(map(int, input().split()))
cnt = 0
for i in range(N):
    if student[i] < P:
        cnt += 1
print(cnt)

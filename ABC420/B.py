n, m = map(int, input().split())
s_i = [input().strip() for _ in range(n)]

pts = [0] * n

for j in range(m):  # 列ごと（投票回ごと）
    zero = 0
    one = 0
    for v in s_i:
        if v[j] == '0':
            zero += 1
        else:
            one += 1
    # print(f"列{j}: 0={zero}, 1={one}")  # ←必要ならデバッグ表示

    # ここで pts を更新（列ごとに毎回やる）
    if zero == 0 or one == 0:
        # 全員同じ → 全員 +1
        for i in range(n):
            pts[i] += 1
    elif zero < one:
        # '0' が少数派 → '0' を出した人に +1
        for i in range(n):
            if s_i[i][j] == '0':
                pts[i] += 1
    else:
        # '1' が少数派 → '1' を出した人に +1
        for i in range(n):
            if s_i[i][j] == '1':
                pts[i] += 1

mx = max(pts)
for i in range(n):
    if pts[i] == mx:
        print(i + 1, end=" ")

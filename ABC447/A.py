N, M = map(int, input().split())
# 偶数座席数の場合
if N % 2 == 0:
    if M <= N // 2:
        print("Yes")
    else:
        print("No")
# 奇数座席数の場合
else:
    if M <= N // 2 + 1:
        print("Yes")
    else:
        print("No")

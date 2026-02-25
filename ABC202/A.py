a, b, c = map(int, input().split())
dice = [0, 6, 5, 4, 3, 2, 1]
ans = dice[a] + dice[b] + dice[c]
print(ans)

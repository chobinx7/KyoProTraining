N = int(input())
for i in range(N):
    if N != 1:
        print(N, end=",")
        N -= 1
    else:
        print(N)

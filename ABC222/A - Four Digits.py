N = int(input())
if N > 999:
    print(N)
elif N > 99:
    print(f"0{N}")
elif N > 9:
    print(f"00{N}")
else:
    print(f"000{N}")

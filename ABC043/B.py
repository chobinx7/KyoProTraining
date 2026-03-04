s = input()
out = []
for i in s:
    out.append(i)
    # print(out)
cnt = out.count("B")
for j in range(0, len(out) + cnt):
    if out[j] == "B":
        del out[j - 1]  # Bの前を削除
        del out[j]  # Bを削除
result = ""
for k in out:
    result += k
print(result)

# WA
# Bの時の判定で前の文字をRemoveしてbreakしているのが間違いな気がする

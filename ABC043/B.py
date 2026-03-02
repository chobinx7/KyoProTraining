s = input()
out = []
for i in s:
    out.append(i)
    # print(out)
for j in range(len(out)):
    if out[j] == "B":
        print(out[j])
        out.remove(out[j])
        out.remove(out[j - 1])
        break
result = ""
for k in out:
    result += k
print(result)

# WA
# Bの時の判定で前の文字をRemoveしてbreakしているのが間違いな気がする

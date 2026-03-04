list_a = list(map(str, input().split()))
new_list = sorted(list_a, reverse=True)
result = "".join(new_list)
print(result)

x, y = map(int,input().split())
month = [12,1,2,3,4,5,6,7,8,9,10,11]
i = (x + y) % 12
print(month[i])
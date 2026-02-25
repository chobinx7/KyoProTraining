s = input()
lng_list = {"red": "SSS", "blue": "FFF", "green": "MMM"}

is_key_error = False
try:
    lng_list[s]
except KeyError:   # ここは組み込みの KeyError を使えるようにする
    is_key_error = True

if is_key_error:
    print("Unknown")
else:
    print(lng_list[s])

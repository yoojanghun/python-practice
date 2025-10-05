# Dictionary = A set of key-value pairs. A collection which is unordered but indexed, and changeable.
#              No duplicate members (set인데 key-value 쌍)

capitals = {"USA": "Washington D.C.",
            "India": "New Delhi",
            "China": "Beijing",
            "Russia": "Moscow"}

# dictionary의 모든 method와 attribute를 보려면
# print(dir(capitals))
# method와 attribute의 설명을 보려면
# print(help(capitals))

print(capitals["USA"])
print(capitals.get("Japan"))                # 잘 사용하지 않는 표현

print()

if capitals.get("Russia"):
    print("That capital exists")
else:
    print("That capital doesn't exist")

if "USA" in capitals:
    print("That capital exists")
else:
    print("That capital doesn't exist")

print()

# dictionary의 값을 추가, 변경 가능
capitals["Germany"] = "Berlin"
print(capitals)

capitals["USA"] = "USA Capital"
print(capitals)

# key: value 쌍을 없애기 위해선
del capitals["China"]
print(capitals)

# 가장 최근의 쌍을 없애기 위해선
capitals.popitem()
print(capitals)

# capitals.clear()

print()

# dictionary의 모든 key를 얻으려면 (key 객체를 반환)
keys = capitals.keys()
print(keys)                         # dict_keys(['USA', 'India', 'Russia'])
keys = list(keys)
print(keys)                         # ['USA', 'India', 'Russia']

for key in capitals.keys():
    print(key)

print()

# dictionary의 모든 value를 얻으려면 (value 객체를 반환)
values = capitals.values()         # dict_values(['usa capital', 'New Delhi', 'Moscow'])
print(values)
values = list(values)              # ['usa capital', 'New Delhi', 'Moscow']
print(values)

for value in capitals.values():
    print(value)

print()

# dictionary 객체를 반환 (Tuple의 2d list와 비슷한 모양)
item = capitals.items()            # dict_items([('USA', 'usa capital'), ('India', 'New Delhi'), ('Russia', 'Moscow')])
print(item)
item = list(item)                  # [('USA', 'usa capital'), ('India', 'New Delhi'), ('Russia', 'Moscow')]
print(item)

for key, value in capitals.items():
    print(f"{key}: {value}")
# dictionary = a collection of {key: value} pairs
#              ordered and mutable. No duplicates

capitals = {"USA": "Washington D.C.",
            "India": "New Delhi",
            "China": "Beijing",
            "Russia": "Moscow"}

# dictionary의 모든 method와 attribute를 보려면
# print(dir(capitals))
# method와 attribute의 설명을 보려면
# print(help(capitals))

print(capitals.get("USA"))
print(capitals.get("Japan"))

if capitals.get("Russia"):
    print("That capital exists")
else:
    print("That capital doesn't exist")

# dictionary의 값을 추가, 변경 가능
capitals.update({"Germany": "Berlin"})
print(capitals)

capitals.update({"USA": "usa capital"})
print(capitals)

# key: value 쌍을 없애기 위해선
capitals.pop("China")
print(capitals)

# 가장 최근의 쌍을 없애기 위해선
capitals.popitem()
print(capitals)

# capitals.clear()

# dictionary의 모든 key를 얻으려면 (key 객체를 반환)
keys = capitals.keys()
print(keys)

for key in capitals.keys():
    print(key)

# dictionary의 모든 value를 얻으려면 (value 객체를 반환)
values = capitals.values()
print(values)

for value in capitals.values():
    print(value)

# dictionary 객체를 반환 (Tuple의 2d list와 비슷한 모양)
item = capitals.items()
print(item)

for key, value in capitals.items():
    print(f"{key}: {value}")
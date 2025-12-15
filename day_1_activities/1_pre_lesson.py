# this is what we will use for the video intro to dictionaries
# dictionaries = a collection of {key:value} pairs
#                ordered and changeable. No duplicates

capitals = {"USA": "Washington D.C.",
            "India": "Delhi",
            "China": "Beijing",
            "Russia": "Moscow"}

# print(dir(capitals))
# print(help(capitals))
# print(capitals.get("Japan"))

if capitals.get("Japan"):
    print("That capital exists")
else:
    print("That capital doesn't exist")

capitals.update({"Germany": "Berlin"})
capitals.update({"USA": "Detriot"})
# capitals.pop("China")
# capitals.popitem()

keys = capitals.keys()

for key in capitals.keys():
    print(key)

values = capitals.values()
for value in capitals.values():
    print(value)

items = capitals.items()
for key, value in capitals.items():
    print(f"{key}:  {value}")
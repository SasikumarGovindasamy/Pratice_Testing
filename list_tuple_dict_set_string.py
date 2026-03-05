# LIST
m=[1,"a",2,"sasi",3,4,"z"]
print(len(m))
m.append(5)
print(m)
print(m.count("sasi"))
m.insert(2,"kumar")
print(m)
print(m.pop(2))
print(m)
print(sorted(m,key=str,reverse=False))
m.sort(key=str,reverse=True)
print(m)
# -----------------------------------------------------------------------------
# DICTIONARY

person = {"name": "Alice", "age": 25}

print(person.get("name"))       # Alice
print(person.keys())            # dict_keys(['name', 'age'])
print(person.values())          # dict_values(['Alice', 25])
print(person.items())           # dict_items([('name', 'Alice'), ('age', 25)])

person.update({"age": 26})      # {'name': 'Alice', 'age': 26}
print(person.pop("age"))        # 26
print(person.setdefault("city", "NY"))  # adds city if not present
copy_dict = person.copy()
print(person.items())
person.clear()                  # {}

# set
fruits = {"apple", "banana"}
fruits.add("cherry")            # {'apple', 'banana', 'cherry'}
fruits.update(["orange", "kiwi"])  # adds multiple
fruits.remove("banana")         # removes banana
fruits.discard("pear")          # no error if missing
print(fruits.pop())             # removes random element
copy_set = fruits.copy()
fruits.clear()                  # {}

# Set operations
a = {1, 2, 3}
b = {3, 4, 5}
print(a.union(b))               # {1, 2, 3, 4, 5}
print(a.intersection(b))        # {3}
print(a.difference(b))          # {1, 2}
print(a.symmetric_difference(b))# {1, 2, 4, 5}
print(a.issubset({1,2,3,4}))    # True

# Tuple
t = (1, 2, 2, 3)
print(t.count(2)) # 2 print(t.index(3)) # 3

# string

text = "  Hello World  "

print(text.lower())             # "  hello world  "
print(text.upper())             # "  HELLO WORLD  "
print(text.strip())             # "Hello World"
print(text.split())             # ['Hello', 'World']
print("-".join(["a", "b", "c"]))# "a-b-c"
print(text.replace("World", "Python"))  # "  Hello Python  "
print(text.find("Hello"))       # 2
print(text.startswith("  He"))  # True
print(text.endswith("ld  "))    # True
print(text.count("l"))          # 3
print("Name: {}".format("Alice"))  # "Name: Alice"
print("abc".isalpha())          # True
print("123".isdigit())          # True
print("abc123".isalnum())       # True
print("hello".capitalize())     # "Hello"
print("hello world".title())    # "Hello World"


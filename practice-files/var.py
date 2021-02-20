i = 5
print(i)
i = i + 1
print(i)

print("---------")

s = '''This is a multi-line string.
This is the second line.'''
print(s)

print("---------")

newList = ["apple", "banana", "cherry"]
newList.insert(1, "grape")
newList.append("blueberry")
for i in range(len(newList)):
    print(newList[i])

print("---------")

listCopy = newList.copy()
listCopy.remove("banana")
print(listCopy)

print("---------")

print("This is a simple dictionary item.")
myCar = {
    "make": "Chevy",
    "model": "Impala",
    "year": "2016"
}
print(myCar)
print("I drive a/an " + myCar["model"])
# Slice the following input: “hello” to get the following output: “hlo”

hello = "hello"

print(hello[::2])
print(hello[:len(hello):2])
print(hello[0::2])
print(hello[0:len(hello):2])
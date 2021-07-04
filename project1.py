import hashlib

print(hashlib.algorithms_available)

name = "supriyasri"
string = hashlib.md5(name.encode())
string_1 = hashlib.sha1(name.encode())
string_2 = hashlib.sha256(name.encode())


print(string)
print(string_1)
print(string_2)
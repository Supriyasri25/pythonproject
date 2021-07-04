import hashlib

name = "supriyasri"
string = hashlib.md5(name.encode())
print("hash value : ")
print(string)

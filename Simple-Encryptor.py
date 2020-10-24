import hashlib

password = input("The word you want to encrypt (you can enter any value): ")
password = str(password)

# MD5 
mdFive = hashlib.md5(password.encode())
print("MD5 Password:", mdFive.hexdigest())

# SHA1 
SHAOne = hashlib.sha1(password.encode())
print("SHA1 Password:", SHAOne.hexdigest())

# MD5 (SHA1) 
mdFiveSHAOne = hashlib.sha1(password.encode())
mdFiveSHAOne = mdFiveSHAOne.hexdigest()
mdFiveSHAOne = hashlib.md5(mdFiveSHAOne.encode())
print("MD5 (SHA1) Password:", mdFiveSHAOne.hexdigest())

# SHA1 (MD5) 
SHAOnemdFive = hashlib.md5(password.encode())
SHAOnemdFive = SHAOnemdFive.hexdigest()
SHAOnemdFive = hashlib.sha1(SHAOnemdFive.encode())
print("MD5 (SHA1) Password:", SHAOnemdFive.hexdigest())




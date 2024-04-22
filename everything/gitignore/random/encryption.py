from cryptography.fernet import Fernet

# working decryption example
# key = Fernet.generate_key()
# f = Fernet(key)
# base_string = (b'Hello World!')
# encrypted = f.encrypt(base_string)
# decrypted = f.decrypt(encrypted)

# print(f"""DATA:
# - {key}
# - {f}
# - {base_string}
# - {encrypted}
# - {decrypted}""")

# attempt to open a file, and encrypt its contents. Use a previous established key
file = open('everything/gitignore/random/extract.py', 'r')
file_content = file.read()
file.close()

key = b'5VsQ04U13bSDhhbv8Uk9nFbPfPY1VGoVhkA87JDyYdA='
f = Fernet(key)
encrypted = f.encrypt(b'{file_content}')

file = open('everything/gitignore/random/extract.py', 'w')
file.write(encrypted)
file.close()
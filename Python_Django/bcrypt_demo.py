import bcrypt

hash = bcrypt.hashpw('secret', bcrypt.gensalt())
print hash

print hash == bcrypt.hashpw('secret', hash)

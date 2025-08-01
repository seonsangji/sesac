import hashlib

def generate_hash(password):
    return hashlib.sha256(password.encode()).hexdigest()

hashed_pw1 = generate_hash('hello1234')
hashed_pw2 = generate_hash('hello1234')

print('Hash1:', hashed_pw1)
print('Hash2:', hashed_pw2)
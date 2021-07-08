from passlib.context import CryptContext

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")
print(pwd_context)

def get_password_hash(password):
    return pwd_context.hash(password)

def verify_password(plain_password, hashed_password):
    return pwd_context.verify(plain_password, hashed_password)

print(get_password_hash('0d92fa77a98d5108c14a7e5468674018697f1fc8dafed76efe92421254fa3fb5'))

# print(verify_password('hello', '$2b$12$Oqe9hzpfBT9deUE6dpgw9eIrWJ35JQIBlBXw4Ng5NqeTf3xXNoWuW'))
import bcrypt

password = input("Enter a password: ")

password_bytes = password.encode('utf-8')
salt = bcrypt.gensalt()
hashed = bcrypt.hashpw(password_bytes, salt)

print(f"\nSalt:   {salt.decode('utf-8')}")
print(f"Hash:   {hashed.decode('utf-8')}")

attempt = input("\nRe-enter password to verify: ")
attempt_bytes = attempt.encode('utf-8')

if bcrypt.checkpw(attempt_bytes, hashed):
    print("Correct")
else:
    print("Incorrect")

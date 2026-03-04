import random
import string

captcha = ''.join(random.choices(string.ascii_uppercase + string.digits, k=5))
print("CAPTCHA:", captcha)

user = input("Enter CAPTCHA: ")

if user == captcha:
    print("Access Granted")
else:
    print("Access Denied")
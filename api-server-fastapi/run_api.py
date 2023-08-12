#import os
#os.system("uvicorn api:api --reload")
import string
import random
print(list(string.ascii_letters))


list_of_passwords = []
for i in range(len(list(string.ascii_letters))):
    password = []
    for i in range(8):
        password.append(list(string.ascii_letters)[random.randint(1,26)])
        list_of_passwords.append(password)
    print(list_of_passwords)
    final_list = []
    for i in range(len(list_of_passwords)):
        interim = ''.join(list_of_passwords[i])
        final_list.append(interim)
    print(final_list)

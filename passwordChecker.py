import re

password = input("Enter the password:")

flag = True
while True:
    if len(password) < 8:    # Checking length
        flag = False
        print(f"Password length is too short. Try a longer password")
        break
    elif not re.search("[A-Z]", password):  # Checking presence of capital letters
        flag = False
        print(f"No capital letter found. Invalid password")
        break
    elif not re.search("[0-9]", password):   # Checking if numeric value is present
        flag = False
        print(f"No numeric character found in the password. Thus invalid.")
        break
    else:
        flag = True
        print('Valid Password')
        break

tries = 0
maxtries = 3
maxlength = 8
password = "1234"
while tries < maxtries:
    pwdin = input(f"Enter Password (max {maxlength} characters): ")
    if len(pwdin) > maxlength:
        print(f'Password should not exceed {maxlength} characters. Try again.')
        tries += 1
    elif pwdin == password:
        print('PASS!!')
        pwdin = input(f"Please setup new password (max {maxlength} characters): ")
        password = pwdin
        if len(password) > maxlength:
            print(f"Password should not exceed {maxlength} characters. Try again.")
        tries = 0  # Reset tries after successful password change
    else:
        tries += 1
        print(f"Password not correct!!! {tries} attempt(s). Will exit after {maxtries} attempts.")
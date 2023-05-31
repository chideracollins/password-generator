import password


def create_password():
    print("You can randomly generate a password by hitting 'enter' twice")
    try:
        user_inp = [int(x) for x in
                    input("Enter your password level (1, for basic... 2, for strong... 3, for complex)\n"
                          "And/or your password length (min: 8, max: 15):").split()]
        if len(user_inp) < 1:
            try:
                structure = [int(y) for y in input("Enter the structure of your password (alpha, num, sym): ").split()]
                if len(structure) < 1:
                    print(password.generate())
                elif len(structure) == 3:
                    print(structure)
                    print(password.generate(ch_type_size=structure))
                else:
                    err_msg(f"Password structure missing {3 - len(structure)} more parameter(s)")
            except ValueError as e:
                err_msg(f"{e} identified, please make sure to provide 3 integers or none to randomly generate")
        elif len(user_inp) < 2:
            print(password.generate(user_inp[0]))
        else:
            print(password.generate(user_inp[0], user_inp[1]))
        create_password()
    except Exception as e:
        err_msg(f"{e} identified, please make sure to provide integer type")


def err_msg(err):
    print(err)
    quit()


create_password()

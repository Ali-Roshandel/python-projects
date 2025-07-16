from My_Module.sign_in_login_modules import sign_in, login, store
user_list = []
username_list = []
user_password_list = []
while True:
    print("1) Sign in: \n2) login\n3) exit")
    choice = input("What would you like to do? (1 or 2 or 3): ")
    if choice == "1":
        if len(user_list) == 5:
            print("Memory is full")
        else:
            user, user_pass = sign_in()
            if [user["Username"]] in username_list:
                print("User Already Existed")
            else:
                user_list.append(user)
                user_password_list.append(user_pass)
                username_list.append(list(user_pass.keys()))
    store(user_list)

    if choice == "2":
        user = login()
        if [user["Username"]] in username_list:
            if {user["Username"]: user["Password"]} in user_password_list:
                print("Logged in")
            else:
                print("Wrong Password")
        else:
            print("User Does Not Exist")

    if choice == "3":
        break

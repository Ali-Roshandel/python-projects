from My_Module.sign_in_login_modules import ordering, final_check, store
order_list = []
while True:
    print("1) Order \n2) Check\n3) Clear The List\n4) Exit")
    choice = input("What would you like to do? (1 or 2 or 3): ")
    if choice == "1":
        if len(order_list) == 5:
            print("Memory is full")
        else:
            order = ordering()
            order_list.append(order)

    if choice == "2":
        check = final_check(order_list)
        print(check)
        store(check)
    if choice == "3":
        order_list.clear()
    if choice == "4":
        break

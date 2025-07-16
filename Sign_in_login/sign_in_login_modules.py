import pickle


# Test Passed
def sign_in():
    first_name = input("Enter Your First name: ")
    last_name = input("Enter Your Last name: ")
    username = input("Enter Your Username: ")
    password = input("Enter Your Password: ")
    user = {"First_name": first_name,
            "Last_name": last_name,
            "Username": username,
            "Password": password}
    user_pass = {username: password}
    return user, user_pass


# Test Passed
def login():
    user_name = input("Username: ")
    password = input("Password: ")
    user = {"Username": user_name,
            "Password": password}
    return user


# Test Passed
def store(x):
    file = open("Files/data.pickle", "wb")
    pickle.dump(x, file)
    file.close()


# Test Passed
def ordering():
    product_name = input("Enter The Product Name: ")
    product_quantity = int(input("Enter The Product Quantity: "))
    product_price = float(input("Enter The Product Price($): "))
    order = {"Product Name": product_name,
             "Product Quantity": product_quantity,
             "Product Price": product_price,
             "Total Price": product_price * product_quantity}
    return order


# Test Passed
def final_check(order_list):
    final = []
    name_list = []
    for i in order_list:
        if i['Product Name'] not in name_list:
            name_list.append(i['Product Name'])
            check = {"Product Name": i['Product Name'],
                     "Product Quantity": i['Product Quantity'],
                     "Total Price": i['Total Price']}
            final.append(check)
            name_list.append(i['Product Name'])
        else:
            for j in final:
                if j['Product Name'] == i['Product Name']:
                    j["Total Price"] += i['Total Price']
                    j["Product Quantity"] += i['Product Quantity']
    return final

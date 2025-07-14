car_list = []
while True:
    ask = input("Do you want to enter car information?(y or n) ")
    if ask == "y":
        name = input("What is the name of the car? ")
        color = input("What is the color of the car? ")
        manufacture_date = (int(input("What is the year of manufacture? ")),
                            int(input("What is the month of manufacture? ")),
                            int(input("What is the day of manufacture? ")))
        car_information = {"Name": name,
                           "Color": color,
                           "Date date_of_manufacture": manufacture_date}
        car_list.append(car_information)
    if ask == 'n':
        break
print(car_list)

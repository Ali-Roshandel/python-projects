from persiantools.jdatetime import JalaliDate
course_list = []
master_list = []
lesson_list = []


# Test Passed
def show_menu():
    print("1) Add Lesson\n2) Report\n3) Report By Master\n4) Report By Lesson\n5) Exit")
    choice = input("Welcome, What would you like to do?: ")
    return choice


# Test Passed
def add_course():
    course = {
        "Course Title": input("Enter Course Title: ").lower(),
        "Master's Name": input("Enter Master: ").lower(),
        "Course Credit": int(input("Enter Course credit: ")),
        "Start Date": input("Enter Start Date:(yyyy-mm-dd Jalali) ")  # yyyy-mm-dd Jalali
    }
    return course


# Test Passed
def add_to_database(course):
    master_list.append(course["Master's Name"])
    lesson_list.append(course["Course Title"])
    course_list.append(course)


# Test Passed
def jalali_str_to_gregorian(course):
    y, m, d = course["Start Date"].split("-")
    jalali_date = JalaliDate(int(y), int(m), int(d))
    course["Start Date"] = jalali_date.to_gregorian()


# Test Passed
def total_report():
    total_dict = {}
    for course in course_list:
        total_dict["Course Title"] = course["Course Title"]
        total_dict["Master's Name"] = course["Master's Name"]
        total_dict["Course Credit"] = course["Course Credit"]
        total_dict["Start Date"] = JalaliDate.to_jalali(course["Start Date"])
        print_report(total_dict)


# Test Passed
def report_by_master():
    master_dict = {}
    master_name = input("Enter Master's Name: ").lower()
    for course in course_list:
        if course["Master's Name"] == master_name:
            master_dict["Course Title"] = course["Course Title"]
            master_dict["Course Credit"] = course["Course Credit"]
            master_dict["Start Date"] = JalaliDate.to_jalali(course["Start Date"])
            print_master(master_dict)
    if master_name not in master_list:
        not_in("Master's Name")


# Test Passed
def report_by_lesson():
    lesson_dict = {}
    lesson_name = input("Enter Course Title: ")
    for course in course_list:
        if course["Course Title"] == lesson_name:
            lesson_dict["Master's Name"] = course["Master's Name"]
            lesson_dict["Course Credit"] = course["Course Credit"]
            lesson_dict["Start Date"] = JalaliDate.to_jalali(course["Start Date"])
            print_lesson(lesson_dict)
    if lesson_name not in lesson_list:
        not_in("Course")


# Test Passed
def print_report(report):
    print(f"Course Title: {report["Course Title"]}, "
          f"Master's Name: {report["Master's Name"]}, ",
          f"Course Credit: {report["Course Credit"]}, ",
          f"Start Date: {report["Start Date"]} ")


# Test Passed
def print_master(report):
    print(f"Course Title: {report["Course Title"]}, "
          f" Course Credit: {report["Course Credit"]}, "
          f"Start Date: {report["Start Date"]}")


# Test Passed
def print_lesson(report):
    print(f"Master's Name: {report["Master's Name"]}, "
          f" Course Credit: {report["Course Credit"]}, "
          f"Start Date: {report["Start Date"]}")


# Test Passed
def not_in(x):
    print(f"{x} Does Not Exist")

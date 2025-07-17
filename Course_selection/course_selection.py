from My_Module.course_selection_modules import *
while True:
    choice = show_menu()
    print("------------------------")
    if choice == "1":
        if len(course_list) >= 20:
            print("Course Limit Has Been Reached")
        else:
            course = add_course()
            jalali_str_to_gregorian(course)
            if course in course_list:
                print("Course Already Exited")
            else:
                if master_list.count(course["Master's Name"]) < 3:
                    add_to_database(course)
                else:
                    print("Each Master Must Have at Most 3 Courses")
        print("------------------------")
    elif choice == "2":
        if len(course_list) == 0:
            print("There Is No Course Available")
        else:
            total_report()
        print("------------------------")
    elif choice == "3":
        if len(master_list) == 0:
            print("There Is No Course Available")
        else:
            report_by_master()
        print("------------------------")
    elif choice == "4":
        if len(lesson_list) == 0:
            print("There Is No Course Available")
        else:
            report_by_lesson()
        print("------------------------")
    elif choice == "5":
        break
    else:
        print("Invalid Option")
        print("------------------------")

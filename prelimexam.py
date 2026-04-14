def get_letter_grade(grade):
    
    if grade >= 90:
        return "A"
    elif grade >= 80:
        return "B"
    elif grade >= 75:
        return "C"
    elif grade >= 60:
        return "D"
    else:
        return "F"


def check_pass_or_fail(grade):
   
    if grade >= 75:
        return "PASSED"
    else:
        return "FAILED"


def save_student_record(first_name, last_name, grade, letter_grade, status):
    
    with open("grade.txt", "a") as file:
        file.write(f"Name: {first_name} {last_name} | Grade: {grade} | Letter: {letter_grade} | Status: {status}\n")



while True:
    # 1. INPUT SECTION
    first_name = input("Enter student's first name: ")
    last_name = input("Enter student's last name: ")
    grade = int(input("Enter student's grade (0-100): "))

    # 2. PROCESSING SECTION
    letter_grade = get_letter_grade(grade)
    status = check_pass_or_fail(grade)

    # 3. OUTPUT SECTION
    print("\nLetter Grade:", letter_grade)
    print("Status:", status)

    save_student_record(first_name, last_name, grade, letter_grade, status)
    print("Record saved successfully!\n")

    # EXIT SECTION
    choice = input("Do you want to add another student? (yes/no): ").lower()
    if choice != "yes":
        print("All student records have been saved. Goodbye!")
        break
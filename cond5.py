'''write a python program to input marks of 5 students.
for each student, the program should check whether the enterd mrks are valid or imvalid. Marks are considered valid only if they are between 0 and 1000. if the marks are invalid, the program should display "Invalid marks skipped" and move to the next student without printing those marks.
    If the marks are valid, the program should display the marks as valid'''

for i in range(5):
    marks = int(input("Enter marks: "))

    if marks < 0 or marks > 100:
        print("Invalid marks skipped")
    else:
        print("Marks are valid:", marks)
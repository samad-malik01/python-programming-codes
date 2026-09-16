'''write a python program to input marks of n students in a list. Display highest marks, lowest marks, average marks, and number of students who passed.'''
n = int(input("Enter number of students: "))
marks = []
for i in range(n):
    m = float(input("Enter marks: "))
    marks.append(m)
highest = max(marks)
lowest = min(marks)
average = sum(marks)/n

passed = 0
for m in marks:
    if m>=40:
        passed = passed + 1

print("Highest Marks: ",highest)
print("Lowest Marks: ",lowest)
print("Average Marks: ",average)
print("Number of students who passed: ",passed)
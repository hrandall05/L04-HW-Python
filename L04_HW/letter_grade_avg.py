# main
from grade_compute import grade_to_number, number_to_grade, validate_input, grade_avg, drop_lowest

count = 0
num_grades = []
letter_grades = []
while count < 4:
    grade_input = input("Enter a letter grade (or 'q' to quit): ")
    if grade_input.lower() == 'q':
        break
    if validate_input(grade_input):
        letter_grades.append(grade_input.upper())
        num_grades.append(grade_to_number(grade_input))
        count +=1
    else:
        print("Invalid input. Please enter a valid letter grade (A+, A, A-, B+, B, B-, C+, C, C-, D, F).")

print("Grades Entered: ", letter_grades)
dropped = number_to_grade(min(num_grades))
print("Lowest grade dropped: ", dropped)
num_grades = drop_lowest(num_grades)
avg = grade_avg(num_grades)
avg_letter = number_to_grade(avg)
print(f"Calculated Average: {avg:.2f}")
print("The average letter grade is: ", avg_letter) 
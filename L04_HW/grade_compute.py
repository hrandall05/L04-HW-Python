
def validate_input(grade: str) -> bool:
    grade = grade.strip().upper()
    valid_grades = {
        'A+', 'A', 'A-',
        'B+', 'B', 'B-',
        'C+', 'C', 'C-',
        'D', 'F'
    }
    if grade in valid_grades:
        return True
    else:
        return False
    
        
    


def grade_to_number(grade: str) -> float:
    grade = grade.strip().upper()
    if grade == 'A+' or grade == 'A':
        return 4.0
    elif grade == 'A-':
        return 3.7
    elif grade == 'B+':
        return 3.3
    elif grade == 'B':
        return 3.0
    elif grade == 'B-':
        return 2.7
    elif grade == 'C+':
        return 2.3
    elif grade == 'C':
        return 2.0
    elif grade == 'C-':
        return 1.7
    elif grade ==  'D':
        return 1.0
    elif grade == 'F':
        return 0.0
    

def number_to_grade(number: float) -> str:
    if 3.7 < number <= 4.0:
        return 'A'
    elif number == 3.7:
        return 'A-'
    elif 3.3 <= number < 3.7:
        return 'B+'
    elif 3.0 <= number <= 3.3:
        return 'B'
    elif 2.7 <= number < 3.0:
        return 'B-'
    elif 2.3 <= number < 2.7:
        return 'C+'
    elif 2.0 <= number < 2.3:
        return 'C'
    elif 1.7 <= number < 2.0:
        return 'C-'
    elif 1.0 <= number < 1.7:
        return 'D'
    else:
        return 'F'


def drop_lowest(grades: list[str]) -> list[str]:
    if not grades:
        return grades
    lowest_grade = min(grades)
    grades.remove(lowest_grade)
    return grades

def grade_avg(grades: list[float]) -> float:
    return sum(grades)/ len(grades)



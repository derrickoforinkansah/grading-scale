def get_letter_grade(mark):
    if mark >= 80:
        return 'A'
    elif 75 <= mark <= 79:
        return 'B+'
    elif 70 <= mark <= 74:
        return 'B'
    elif 65 <= mark <= 69:
        return 'C+'
    elif 60 <= mark <= 64:
        return 'C'
    elif 55 <= mark <= 59:
        return 'D'
    elif 50 <= mark <= 54:
        return 'D+'
    elif 45 <= mark <= 49:
        return 'E'
    else:
        return 'F'
# example usage:
mark = 91
letter_grade = get_letter_grade(mark)
print(f"Therefore, Derrick the letter grade for your mark of {mark} is: {letter_grade}")   

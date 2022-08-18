def compute_grade(value: int):
    grade = "A"
    if (value < 50):
        grade = "D"
    elif (50<= value <= 64):
        grade = "C"
    elif (65<= value <= 79):
        grade = "B"
    return grade
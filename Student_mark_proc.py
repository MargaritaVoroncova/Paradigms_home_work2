# Процедурное программирование

student_data = [
    {'name': 'Alice', 'score': 85},
    {'name': 'Bob', 'score': 92},
    {'name': 'Charlie', 'score': 78},
    {'name': 'David', 'score': 95},
]


def count_average(student_data):
    total_score = 0
    for student in student_data:
        total_score += student['score']
    return total_score / len(student_data)


def find_higher_average_students(student_data, average):
    higher_average_students = []
    for student in student_data:
        if student['score'] > average:
            higher_average_students_average_students.append(student['name'])
    return higher_average_students_average_students


average = count_average(student_data)
higher_average_students = find_higher_average_students(student_data, average)

print(f"Средний балл: {average}")
print(f"Студенты с баллом выше среднего: {higher_average_students}")
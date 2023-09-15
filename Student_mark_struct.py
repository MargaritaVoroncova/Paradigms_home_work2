# Структурное программирование

student_data = [
    {'name': 'Alice', 'score': 85},
    {'name': 'Bob', 'score': 92},
    {'name': 'Charlie', 'score': 78},
    {'name': 'David', 'score': 95},
]

# Сначала вычислим средний балл
total_score = 0
for student in student_data:
    total_score += student['score']

average = total_score / len(student_data)

# Теперь найдем студентов с баллами выше среднего
higher_average_students = []
for student in student_data:
    if student['score'] > average:
        higher_average_students.append(student['name'])

print(f"Средний балл: {average}")
print(f"Студенты с баллом выше среднего: {higher_average_students}")
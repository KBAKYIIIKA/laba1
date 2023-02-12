groupmates = [
    {
        "name": "Алан",
        "surname": "Шарифуллин",
        "exams": ["Ввит", "Философия", "АиГ"],
        "marks": [5, 4, 5]
    },
    {
        "name": "Фредерик",
        "surname": "Младший",
        "exams": ["Социология", "АиГ", "ФОЧП"],
        "marks": [4, 4, 3]
    },
    {
        "name": "Артур",
        "surname": "Шаляпин",
        "exams": ["Философия", "ИС", "КТП"],
        "marks": [5, 5, 5]
    }
]

print("Введите балл:")
mark=int(input())
print(u"Имя".ljust(15), u"Фамилия".ljust(10), u"Экзамены".ljust(30), u"Оценки".ljust(20))

for student in groupmates:
    st_m=student['marks']
    sr_b=sum(st_m)/len(st_m)
    print(sr_b)

    if sr_b>mark:
        print(student["name"].ljust(15), student["surname"].ljust(10), str(student["exams"]).ljust(30), str(student["marks"]).ljust(20))


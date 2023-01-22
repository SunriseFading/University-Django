from celery import shared_task
from direction.models import Direction
from group.models import Group
from openpyxl import Workbook
from student.models import Student


@shared_task
def create_report(
    directions=Direction.objects.all(),
    groups=Group.objects.all(),
    students=Student.objects.all(),
):

    report = Workbook()
    sheet = report.active

    sheet.append(["Направление", "Куратор", "Дисциплины"])
    for direction in directions:
        sheet.append(
            [
                direction.name,
                direction.curator.full_name,
                " ".join([x[0] for x in direction.disciplines.values_list("name")]),
            ]
        )

    sheet.append([])
    sheet.append(
        [
            "Группа",
            "Направление",
            "Кол-во студентов",
            "Кол-во студентов мужского пола",
            "Кол-во студентов женского пола",
        ]
    )
    for group in groups:
        sheet.append(
            [
                group.name,
                group.direction.name,
                group.students.count(),
                group.students.filter(gender="male").count(),
                group.students.filter(gender="female").count(),
            ]
        )

    sheet.append([])
    sheet.append(["ФИО", "Email", "Группа", "Пол", "Возраст"])
    for student in students:
        sheet.append(
            [
                student.full_name,
                student.email,
                student.group.name,
                student.gender,
                student.age,
            ]
        )

    report.save("media/report.xlsx")

    return "report.xlsx"

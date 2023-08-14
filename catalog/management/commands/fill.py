from django.core.management import BaseCommand
from catalog.models import Student


class Command(BaseCommand):

    def handle(self, *args, **options):
        students_list = [
            {'name': 'Luka', 'surname': 'Shneiderman', 'age': 24, },
            {'name': 'Ivan', 'surname': 'Ivanov', 'age': 22, },
            {'name': 'Oleg', 'surname': 'Yegorovich', 'age': 26, },
            {'name': 'Anna', 'surname': 'Krylov', 'age': 23, },
            {'name': 'Kliment', 'surname': 'Krylov', 'age': 23, },
        ]

        students_for_create = []
        for student in students_list:
            students_for_create.append(Student(**student))

        Student.objects.bulk_create(students_for_create)
        print('Students created!')

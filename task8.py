import json
import os


class DataBase:
    def __init__(self, file_name):
        self.file_name = file_name

        if os.path.exists(self.file_name):
            with open(self.file_name, encoding='utf-8') as f:
                self.all_students = json.load(f)

        else:
            self.all_students = []

    def save(self):
        with open(self.file_name, 'w', encoding='utf-8') as f:
            json.dump(self.all_students, f, ensure_ascii=False)

    def get(self, num):
        return self.all_students[num - 1]

    def add_student(self, name, surname, age):
        self.all_students.append({"name": name, "surname": surname, "age": age})
        self.save()

    def select_by_age(self, age):
        return [x for x in self.all_students if x['age'] == age]


if __name__ == '__main__':
    db = DataBase('all_students.json')

    print('''\
choose an action:

    1 - add a student
    2 - withdrawal by number
    3 - conclusion by age
    4 - output from file 
    to exit - 0
''')

    while True:
        f = input('Entering an action: ')
        if f == '1':
            print(' Space entry (first name, last name, age)')
            name, surname, age = input().split()
            db.add_student(name, surname, age)

        elif f == '2':
            num = int(input('number ->  '))
            print(db.get(num))


        elif f == '3':
            items = db.select_by_age(input('age-> '))
            print(items)

        elif f == '4':
            with open(db.file_name, encoding='utf-8') as f:
                text = f.read()
                print(repr(text))

        else:
            break

    # Save file
class Diary:
    def __init__(self):
        self.__grades = {}
        self.__allowed_subjects = ["Биология", "Химия", "Физика", "Математика", "Русский", "Литература"]

    def add_grade(self, subject, grade):
        if type(subject) != str or subject.strip() == "":
            print("Неверный предмет")
            return
        subject = subject.strip()
        if subject not in self.__allowed_subjects:
            print("Предмет не разрешен")
            return
        if type(grade) != int or grade < 2 or grade > 5:
            print("Неверная оценка")
            return
        if subject in self.__grades:
            self.__grades[subject].append(grade)
        else:
            self.__grades[subject] = [grade]
    def get_average(self, subject):
        if type(subject) != str:
            return 0
        subject = subject.strip()

        if subject not in self.__grades:
            return 0
        s = 0
        for g in self.__grades[subject]:
            s = s + g
        return s / len(self.__grades[subject])
    def get_all_average(self):
        s = 0
        count = 0
        for subject in self.__grades:
            for g in self.__grades[subject]:
                s = s + g
                count = count + 1
        if count == 0:
            return 0
        return s / count
    def get_bad_subjects(self):
        bad = []
        for subject in self.__grades:
            avg = self.get_average(subject)
            if avg < 3.5:
                bad.append(subject)
        return bad
    def reset_diary(self):
        self.__grades = {}


my_diary = Diary()
my_diary.add_grade("Биология", 5)
my_diary.add_grade("Биология", 5)
my_diary.add_grade("Биология", 5)
my_diary.add_grade("Химия", 2)
my_diary.add_grade("Химия", 3)

my_diary.add_grade("История", 5)   # предмет не разрешен
my_diary.add_grade("", 10)         # неверный предмет
my_diary.add_grade("Физика", 6)    # неверная оценка
my_diary.add_grade("Физика", 4)    # норм
print(my_diary.get_average("Биология"))
print(my_diary.get_average("Химия"))
print(round(my_diary.get_all_average(), 2))
print(my_diary.get_bad_subjects())
my_diary.reset_diary()
# Подготовить файлы проекта, предварительно клонировав их с GitHub себе в проект - https://github.com/yanchuki/HumanMoveTest.git. В загруженном проекте находится модуль main с классом Student; объектами этого класса вам и нужно будет управлять и тестировать их.
# Создайте в отдельном модуле класс для тестирования (наследованный от TestCase).
# Напишите 3 теста, где будут создаваться отдельные объекты класса Student:
# Первый тест: у одного объекта должен запускать метод walk 10 раз, после чего должен возвращаться результат сравнения полученных данных.
# В  случае провального теста должно выводится сообщение: Дистанции не равны [дистанция человека(объекта)] != 500
# Второй тест: у одного объекта должен запускать метод run 10 раз, после чего должен возвращаться результат сравнения полученных данных.
# В  случае провального теста должно выводится сообщение: Дистанции не равны [дистанция человека(объекта)] != 1000
# Третий тест: 2 объекта "соревнуются", один "бежит", другой "идёт" (тот самый студент, кто не посещает вебинары).
# После чего должен возвращаться результат сравнения полученных данных. В  случае провального теста должно выводится сообщение:
# [бегущий человек] должен преодолеть дистанцию больше, чем [идущий человек].
#
# Рекомендуемые методы для тестирования:
# assertEqual, assertGreather, assertLess


import unittest
from homework38 import Student


class StudentTest(unittest.TestCase):

    def test_walk(self):
        student = Student("Вася")
        for n in range(10):
            student.walk()
        result = student.distance
        self.assertEqual(result,50, f'Дистанции не равны {result} != 50')



    def test_run(self):
        student = Student("Коля")
        for n in range(10):
            student.run()
        result2 = student.distance
        self.assertEqual(result2, 100, f'Дистанции не равны {result2} != 100')



    def test_equal(self):
        student = Student("Вася")
        for n in range(10):
            student.walk()
        result = student.distance
        student2 = Student("Коля")
        for n in range(10):
            student.run()
        result2 = student.distance
        self.assertLess(result, result2, f'{student2} должен преодолеть дистанцию больше, чем {student}')





if __name__ == '__main__':
    unittest.main()
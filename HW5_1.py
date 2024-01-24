# 2. Напишите функцию, которая принимает на вход строку - абсолютный путь до файла.
# Функция возвращает кортеж из трёх элементов: путь, имя файла, расширение файла.

def parse_link(link: str):
    *b,c = link.split("\\")
    my_str = '\\'.join(b)
    file_name, ext_file = c.split(".")
    return my_str, file_name, ext_file

print(parse_link("d:\my doc\Обучение\Бизнесс аналитик\20_погружение в Python\Lesson5\Лекция 5 Погружение в Python Итераторы и генераторы.pdf" ))
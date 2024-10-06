'''
Задача "Мифическое наследование":
Необходимо написать 3 класса:
Horse - класс описывающий лошадь. Объект этого класса обладает следующими атрибутами:
x_distance = 0 - пройденный путь.
sound = 'Frrr' - звук, который издаёт лошадь.
И методами:
run(self, dx), где dx - изменение дистанции, увеличивает x_distance на dx.

Eagle - класс описывающий орла. Объект этого класса обладает следующими атрибутами:
y_distance = 0 - высота полёта
sound = 'I train, eat, sleep, and repeat' - звук, который издаёт орёл (отсылка)
И методами:
fly(self, dy) где dy - изменение дистанции, увеличивает y_distance на dy.

Pegasus - класс описывающий пегаса. Наследуется от Horse и Eagle в том же порядке.
Объект такого класса должен обладать атрибутами классов родителей в порядке наследования.
Также обладает методами:
move(self, dx, dy) - где dx и dy изменения дистанции. В этом методе должны запускаться наследованные методы run и fly
соответственно.
get_pos(self) возвращает текущее положение пегаса в виде кортежа - (x_distance, y_distance) в том же порядке.
voice - который печатает значение унаследованного атрибута sound.
'''

# Пункты задачи:
# 1. Создайте классы родители: Horse и Eagle с методами из описания.
# 2. Создайте класс наследник Pegasus с методами из описания.
# 3. Создайте объект класса Pegasus и вызовите каждый из ранее перечисленных методов, проверив их работу.


# Класс Horse описывает лошадь
class Horse:
    def __init__(self):
        self.x_distance = 0  # Пройденный путь
        self.sound = 'Frrr'  # Звук лошади

    def run(self, dx):
        """Увеличивает пройденный путь на dx"""
        self.x_distance += dx


# Класс Eagle описывает орла
class Eagle:
    def __init__(self):
        self.y_distance = 0  # Высота полета
        self.sound = 'I train, eat, sleep, and repeat'  # Звук орла

    def fly(self, dy):
        """Увеличивает высоту полета на dy"""
        self.y_distance += dy


# Класс Pegasus, который наследуется от Horse и Eagle
class Pegasus(Horse, Eagle):
    def __init__(self):
        Horse.__init__(self)  # Инициализация атрибутов лошади
        Eagle.__init__(self)  # Инициализация атрибутов орла

    def move(self, dx, dy):
        """Перемещает пегаса, используя методы родительских классов"""
        self.run(dx)  # Используем метод run класса Horse
        self.fly(dy)  # Используем метод fly класса Eagle

    def get_pos(self):
        """Возвращает текущее положение пегаса"""
        return (self.x_distance, self.y_distance)

    def voice(self):
        """Выводит звук, унаследованный от родительских классов"""
        print(self.sound)  # Используется атрибут sound из Eagle, так как он последний в цепочке наследования


# Пример использования
p1 = Pegasus()

# Вывод начальной позиции
print(p1.get_pos())  # (0, 0)

# Движение пегаса
p1.move(10, 15)
print(p1.get_pos())  # (10, 15)

# Ещё одно движение пегаса
p1.move(-5, 20)
print(p1.get_pos())  # (5, 35)

# Вывод звука пегаса
p1.voice()  # I train, eat, sleep, and repeat

'''
Вывод на консоль:
(0, 0)
(10, 15)
(5, 35)
I train, eat, sleep, and repeat

'''
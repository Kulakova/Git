# T# 5.1.Создайте любой класс с произвольным количеством подклассов, экземпляров, атрибутов
# # и методов - как минимум один атрибут должен быть с уровнем доступа private.
# # Соответственно, для получания значений этого атрибута нужно использовать методы get
# # и set
#
class Bird:
    ClassName = "Птица"
    objInstancesCount = 0

    def __init__(self, name, id, age):
        self._name = name
        self.id = id
        self.age = age
        Bird.objInstancesCount = Bird.objInstancesCount + 1

    # getter
    def get_name(self):
        return self._name

    # setter
    def set_name(self, n):
        self._name = n

    def info(self):
        print(self._name)
        print("Идентификационный номер: " + str(self.id))
        print("Возраст: " + str(self.age))

b = Bird("Синяя", 23, 2)
print("Это " + b.get_name())
b.set_name("Жар")
print("А, нет... Это " + b.get_name())


class Duck(Bird):
    species = "Утка"

    def __init__(self, name, id, age, fly_speed, fly_height):
        super().__init__(name, id, age)
        self.__fly_speed = fly_speed
        self.__fly_height = fly_height

    @property
    def fly_speed(self):
        return self.__fly_speed

    @fly_speed.setter
    def fly_speed(self, fly_speed):
        self.__fly_speed = fly_speed

    @property
    def fly_height(self):
        return self.__fly_height

    @fly_height.setter
    def fly_height(self, fly_height):
        self.__fly_height = fly_height

    def info(self):
        super().info()
        print("Вид: " + Duck.species)
        print("Скорость полета: " + str(self.__fly_speed))
        print("Высота полета: " + str(self.__fly_height))

d = Duck("duck1", 22, 2, 110, 5)
d.info()


class GalaBacklane(Bird):
    species = "Галапагосский баклан"

    def __init__(self, name, id, age, population, color):
        super().__init__(name, id, age)
        self.__population = population
        self.color = color

    @property
    def population(self):
        return self.__population

    @population.setter
    def population(self, population):
        self.__population = population

    def color(self):
        return self.color

    def info(self):
        super().info()
        print("Вид: " + GalaBacklane.species)
        print("Количество особей: " + str(self.__population))


g = GalaBacklane("galaBacklane1", 22, 2, 60, "green")
g.info()


#
# # 5.2.Cоздайте репозиторий на Github и отправте файл с домашним заданием в этот
# # удаленный репозиторийhis is a sample Python script.

# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.


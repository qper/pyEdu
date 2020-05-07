task = """
Создайте класс GameCharacter с атрибутами name, health, level и методом speak(),
который выводит на печать 'Hi, my name is (значение атрибута name)'.

Создайте класс Villain, наследник класса GameCharacter с теми же атрибутами, методом speak(), который выводит на печать
'Hi, my name is (значение атрибута name) and I will kill you',
методом kill(), который принимает в качестве параметра объект класса GameCharacter,
присваивает атрибуту health этого объекта значение 0 и  выводит на печать 'Bang-bang, now you're dead'
"""


class GameCharacter:
    def __init__(self, name, health, level):
        self.name = name
        self.health = health
        self.level = level

    def speak(self):
        print("Hi, my name is " + self.name)


class Villain(GameCharacter):
    def __init__(self, name, health, level):
        GameCharacter.__init__(self, name, health, level)

    def speak(self):
        print("Hi, my name is " + self.name + " and I will kill you")

    def kill(self, game_object):
        game_object.health = 0
        print("Bang-bang, now you're dead")


def show_current_health_points(health):
    print("My current health point(s): " + str(health))


if __name__ == "__main__":
    character = GameCharacter("Pac-Man", 100, 16)
    character.speak()
    show_current_health_points(character.health)

    bad_character = Villain("Assassin", 100, 80)
    bad_character.speak()
    bad_character.kill(character)

    character.speak()
    show_current_health_points(character.health)

class Animal:
    __legs = 0
    __eyes = 0

    def __init__(self, legs, eyes) -> None:
        super().__init__()
        self.__legs = legs
        self.__eyes = eyes

    def sound(self):
        print(f"Animal Sound having {self.__eyes} eyes and {self.__legs} legs")


class Eagle(Animal):

    def __init__(self, legs, eyes) -> None:
        super().__init__(legs, eyes)

    def sound(self):
        super().sound()


brd = Eagle(legs=5,eyes=5)
brd.sound()


from abc import ABC, abstractmethod

class FlyBehavior(ABC):
    @abstractmethod
    def fly(self) -> None:
        pass

class FlyWithWings(FlyBehavior):
    def fly(self) -> None:
        print("Estou voando com asas!")

class FlyNoWay(FlyBehavior):
    def fly(self) -> None:
        print("Eu não consigo voar.")

class FlyRocketPowered(FlyBehavior):
    def fly(self) -> None:
        print("Voando como um foguete!")
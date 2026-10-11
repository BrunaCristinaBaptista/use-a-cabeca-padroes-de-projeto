from abc import ABC, abstractmethod
from FlyBehavior import FlyBehavior, FlyWithWings, FlyNoWay
from QuackBehavior import QuackBehavior, Quack, Squeak, MuteQuack

class Duck(ABC):
    def __init__(self, fly_behavior: FlyBehavior, quack_behavior: QuackBehavior):
        self._fly_behavior = fly_behavior
        self._quack_behavior = quack_behavior

    @abstractmethod
    def display(self) -> None:
        pass

    def perform_fly(self) -> None:
        self._fly_behavior.fly()

    def perform_quack(self) -> None:
        self._quack_behavior.quack()

    def swim(self) -> None:
        print("Todos os patos flutuam, até os de borracha!")

    def set_fly_behavior(self, fb: FlyBehavior) -> None:
        self._fly_behavior = fb

    def set_quack_behavior(self, qb: QuackBehavior) -> None:
        self._quack_behavior = qb

class MallardDuck(Duck):
    def __init__(self):
        super().__init__(fly_behavior=FlyWithWings(), quack_behavior=Quack())

    def display(self) -> None:
        print("Eu sou um pato-real (Mallard) de verdade!")

class RubberDuck(Duck):
    def __init__(self):
        super().__init__(fly_behavior=FlyNoWay(), quack_behavior=Squeak())

    def display(self) -> None:
        print("Eu sou um patinho de borracha amarelo!")

class ModelDuck(Duck):
    def __init__(self):
        super().__init__(fly_behavior=FlyNoWay(), quack_behavior=MuteQuack())

    def display(self) -> None:
        print("Eu sou um pato modelo/isca de madeira.")
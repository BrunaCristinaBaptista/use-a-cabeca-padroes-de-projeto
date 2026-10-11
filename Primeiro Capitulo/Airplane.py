from FlyBehavior import FlyBehavior, FlyWithWings, FlyRocketPowered

class Airplane:
    def __init__(self, fly_behavior: FlyBehavior):
        self._fly_behavior = fly_behavior

    def take_off(self) -> None:
        print("Preparando para decolar...")
        self._fly_behavior.fly()

    def set_fly_behavior(self, fb: FlyBehavior) -> None:
        self._fly_behavior = fb
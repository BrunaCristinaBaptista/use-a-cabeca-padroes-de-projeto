from FlyBehavior import FlyBehavior, FlyWithWings, FlyRocketPowered

class SuperHero:
    def __init__(self, name: str, fly_behavior: FlyBehavior):
        self.name = name
        self._fly_behavior = fly_behavior

    def patrol_city(self) -> None:
        print(f"{self.name} está patrulhando:")
        self._fly_behavior.fly()

    def set_fly_behavior(self, fb: FlyBehavior) -> None:
        self._fly_behavior = fb
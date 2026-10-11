from Duck import MallardDuck, ModelDuck
from FlyBehavior import FlyRocketPowered
from Airplane import Airplane
from SuperHero import SuperHero

def main():
    mallard = MallardDuck()
    mallard.display()
    mallard.perform_fly() 
    mallard.perform_quack() 

    print("-" * 30)

    model = ModelDuck()
    model.display()
    model.perform_fly()   
    model.set_fly_behavior(FlyRocketPowered())
    model.perform_fly()

    print("-" * 30)

    boeing = Airplane(fly_behavior=FlyRocketPowered())
    boeing.take_off()

    print("-" * 30)

    heroi = SuperHero(name="Gavião Negro", fly_behavior=FlyRocketPowered())
    heroi.patrol_city()

if __name__ == "__main__":
    main()

""" Types of transport

-Implemented some types of transport as electric also as no.
-Below in main is how it works
"""
from abc import ABC, abstractmethod


class Transport(ABC):
    """ Something that moves """

    def __init__(self, length: int, weight: int):
        """ Physical parameters """
        self.__length = length
        self.__weight = weight

    @property
    def speed(self) -> float:
        """ Dynamic characteristic that depends on other
        by formula V = N / mg, where g = 9.8
        """
        return self._power / (self.__weight * 9.8)

    @abstractmethod
    def move(self) -> None:
        """ How it moves """
        raise NotImplementedError

    @abstractmethod
    def stop(self) -> None:
        """ How it stops """
        raise NotImplementedError

    def __gt__(self, other) -> bool:
        """ Is one faster then other """
        return self.speed > other.speed

    def __eq__(self, other) -> bool:
        """ If speeds are equal """
        return self.speed == other.speed

    def __len__(self) -> int:
        """ Transport length in centimeters """
        return self.__length


class Engine:
    """ A detail that converts energy and makes transport move """

    def __init__(self, power: int, fuel: int):
        """ Parameters """
        self._power = power
        self.__fuel = fuel

    @staticmethod
    def run():
        """ Start converting energy """
        return "engine's running..."

    @staticmethod
    def stop() -> None:
        """ Stop spinning """
        print("engine's stopping...")

    @property
    def power(self) -> int:
        """ Get the power """
        return self._power

    def __pow__(self, power, modulo=None):
        """ Upgrade the power """
        self._power += power

    @property
    def fuel(self) -> int:
        """ Get the amount of fuel """
        return self.__fuel

    def __iadd__(self, other: int):
        """ Increase the amount of fuel """
        self.__fuel += other
        return self


class Plane(Transport, Engine):
    """ The transport that flies """

    def __init__(self, length, weight, engine_power: int, engine_fuel: int):
        Transport.__init__(self, length, weight)
        Engine.__init__(self, engine_power, engine_fuel)

    def move(self):
        self.run()
        print("plane is flying...")

    def stop(self):
        print("plane is landing...")
        Engine.stop()


class Car(Transport, Engine):
    """ The transport that rides """

    def __init__(self, length, weight, engine_power: int, engine_fuel: int):
        Transport.__init__(self, length, weight)
        Engine.__init__(self, engine_power, engine_fuel)

    def move(self):
        self.run()
        print("car is riding...")

    def stop(self):
        print("car is parking...")
        Engine.stop()


class Boat(Transport, Engine):
    """ The transport that sails """

    def __init__(self, length, weight, engine_power: int, engine_fuel: int):
        Transport.__init__(self, length, weight)
        Engine.__init__(self, engine_power, engine_fuel)

    def move(self):
        self.run()
        print("boat is sailing...")

    def stop(self):
        print("boat is mooring...")
        Engine.stop()


class Horse(Transport):
    """ The transport that gallops """

    def __init__(self, length, weight, power: int):
        Transport.__init__(self, length, weight)
        self._power = power

    def move(self):
        print("horse is galloping...")

    def stop(self):
        print("horse is stopping...")


def main():
    """ To show how it works """

    # Let's create some transports:
    plane_1 = Plane(7000, 168000, 1646400000, 183380)
    car_1 = Car(450, 2000, 2352000, 50)
    boat_1 = Boat(600, 1000, 588000, 30)
    horse_1 = Horse(250, 300, 264600)

    # Check how they move:
    plane_1.move()
    plane_1.stop()
    car_1.move()
    car_1.stop()
    boat_1.move()
    boat_1.stop()
    horse_1.move()
    horse_1.stop()
    print("-"*20)

    # View the length of some of them:
    print("lengths: ")
    print(len(car_1))
    print(len(horse_1))
    print("-" * 20)

    # Compare them to find out which is faster:
    print("compare speed: ")
    print(car_1.speed)
    print(boat_1.speed)
    print(car_1 > boat_1)
    print("-" * 20)

    # Let's put the fuel into:
    print("put the fuel: ")
    print(boat_1.fuel)
    boat_1 += 10
    print(boat_1.fuel)
    print("-" * 20)

    # Upgrade the engine to increase the speed:
    print("power and speed: ")
    print(plane_1.speed)
    print(plane_1.power)
    pow(plane_1, 3)
    print(plane_1.speed)
    print(plane_1.power)
    print("-" * 20)


if __name__ == "__main__":
    main()

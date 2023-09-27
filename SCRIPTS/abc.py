import abc

class AutoMobile(abc.ABC):

    @abc.abstractmethod
    def start(self) -> None:
        pass

    @abc.abstractmethod
    def accelerate(self) -> None:
        pass

    @abc.abstractmethod
    def stop(self) -> None:
        pass


class Car(AutoMobile):

    def start(self) -> None:
        pass

    def accelerate(self) -> None:
        pass

    def stop(self) -> None:
        print(f'stop {self.__class__.__name__}')


class Truck(AutoMobile):

    def start(self) -> None:
        pass

    def accelerate(self) -> None:
        pass

    def stop(self) -> None:
        print(f'stop {self.__class__.__name__}')
        pass

class Bus(AutoMobile):

    def start(self) -> None:
        pass

    def accelerate(self) -> None:
        pass

    def stop(self) -> None:
        print(f'stop {self.__class__.__name__}')
        pass


for veicle in [Car(), Truck(), Bus()]:
    veicle.stop()





























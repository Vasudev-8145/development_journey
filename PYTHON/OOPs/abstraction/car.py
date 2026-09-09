

from abc import ABC,abstractmethod
class Car(ABC):

    @abstractmethod           # decorator
    def start(self):pass

    @abstractmethod
    def accelarate(self):pass

    @abstractmethod
    def stop(self):pass

class Baleno(Car):

    def start(self):
        print("Baleno start..")

    def accelarate(self):
        print("Baleno accelarate")  # parent class il ulla ella method num definition kodthilenkil error adikum

    def stop(self):
        print("Baleno stop")

baleno_instance = Baleno()
baleno_instance.stop()
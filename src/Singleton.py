from abc import abstractmethod


class Singleton:
    @abstractmethod
    def func(self):
        pass


    def __new__(cls):
        if not hasattr(cls, 'instance'):
            cls.instance = super().__new__(cls)
        return cls.instance


s = Singleton()
print("Object created", s)

s1 = Singleton()
print("Object created", s1)

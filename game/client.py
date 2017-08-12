from abc import ABCMeta, abstractmethod
from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from .unit import Unit


class Client(metaclass=ABCMeta):
    def __init__(self, id=0):
        self.id = id

    @abstractmethod
    def action(self, unit: 'Unit', order: int, observation: 'Observation') -> int:
        pass


class UserClient(Client):
    def action(self, unit: 'Unit', order: int, observation: 'Observation') -> int:
        print("please type next order")
        print("id: {} unit: {}".format(self.id, unit))
        user_input = self.get_input_int()
        print("id: {} next order: {}".format(self.id, user_input))
        return user_input

    def get_input_int(self):
        user_input = input()
        try:
            parsed_input = int(user_input)
            return parsed_input
        except:
            print("please type int")
            return self.get_input_int()

class EchoClient(Client):
    def action(self, unit: 'Unit', order: int, observation: 'Observation') -> int:
        return order

class AIClient(Client):
    def action(self, unit: 'Unit', order: int, observation: 'Observation') -> int:
        return order #stub
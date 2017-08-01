# -*- coding: utf-8 -*-
from game.master import Master
from game.unit import PlayerUnit, DelayUnit, ManufacturerUnit, CustomerUnit


class UserClient:
    def __init__(self, id=0):
        self.id = id

    def action(self, unit, order):
        print("pleese type next order")
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
            print("pleese type int")
            return self.get_input_int()

if __name__ == "__main__":
    unit0 = PlayerUnit(client=UserClient(id=0))
    unit1 = PlayerUnit(client=UserClient(id=1))
    unit2 = PlayerUnit(client=UserClient(id=2))
    unit3 = PlayerUnit(client=UserClient(id=3))

    delay_unit0 = DelayUnit()
    delay_unit1 = DelayUnit()
    delay_unit2 = DelayUnit()
    delay_unit3 = DelayUnit()
    delay_unit4 = DelayUnit()
    delay_unit5 = DelayUnit()

    customer_unit = CustomerUnit()

    manufacturer_unit = ManufacturerUnit()

    units = [
        customer_unit,
        unit0,
        delay_unit0,
        delay_unit1,
        unit1,
        delay_unit2,
        delay_unit3,
        unit2,
        delay_unit4,
        delay_unit5,
        unit3,
        manufacturer_unit,
    ]

    master = Master(*units)

    end_game = False
    while not end_game:
        end_game = master.next_action()
    print("unit0: inventory: {} backlog: {} cost: {}".format(unit0.inventory, unit0.backlog, unit0.cost))
    print("unit1: inventory: {} backlog: {} cost: {}".format(unit1.inventory, unit1.backlog, unit1.cost))
    print("unit2: inventory: {} backlog: {} cost: {}".format(unit2.inventory, unit2.backlog, unit2.cost))
    print("unit3: inventory: {} backlog: {} cost: {}".format(unit3.inventory, unit3.backlog, unit3.cost))
    print("end_game")

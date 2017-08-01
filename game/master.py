# -*- coding: utf-8 -*-
from .constants import *
from .unit import DelayUnit, ManufacturerUnit


class Master:
    current_round_index = 0

    units = []

    def __init__(
        self,
        *units
    ):
        self.units = list(units)

    def step1(self):
        transport = None
        for unit in reversed(self.units):
            transport = unit.step1(transport)

    def step2(self):
        order = None
        for unit in self.units:
            order = unit.step2(order)

    def step3(self):
        transport = None
        for unit in reversed(self.units):
            transport = unit.step3(transport)

    def step4(self):
        order = None
        for unit in self.units:
            order = unit.step4(order)

    def next_action(self):
        end_game = self.current_round_index == GAME_LEGTH - 1
        if end_game:
            return end_game
        self.step1()
        self.step2()
        self.step3()
        self.step4()
        end_game = self.current_round_index == GAME_LEGTH - 1
        if not end_game:
            self.current_round_index += 1
        return end_game

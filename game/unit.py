# -*- coding: utf-8 -*-
import random
from abc import ABCMeta, abstractmethod
from typing import Optional

from .constants import *


class Unit(metaclass=ABCMeta):
    @property
    @abstractmethod
    def inventories(self):
        return []

    @abstractmethod
    def step1(self, transport: int) -> Optional[int]:
        return transport

    @abstractmethod
    def step2(self, order: int) -> Optional[int]:
        return order

    @abstractmethod
    def step3(self, transport: int) -> Optional[int]:
        return transport

    @abstractmethod
    def step4(self, order: int) -> Optional[int]:
        return order


class PlayerUnit(Unit):
    order = 0

    backlog = 0
    inventory = INVENTORY_INITIAL

    cost = 0

    client = None

    @property
    def inventories(self):
        return [self.transport]

    def __init__(self, client):
        self.client = client

    def step1(self, transport: int) -> Optional[int]:
        if transport is not None:
            self.inventory += transport
        return None

    def step2(self, order: int) -> Optional[int]:
        if order is not None:
            self.order = order
        return None

    def step3(self, transport: int) -> Optional[int]:
        next_backlog = self.order + self.backlog - self.inventory
        if next_backlog > 0:
            next_transport = self.inventory
            self.inventory = 0
            self.order = 0
            self.backlog = next_backlog
            return next_transport
        else:
            next_transport = self.order + self.backlog
            self.inventory = -next_backlog
            self.order = 0
            self.backlog = 0
            return next_transport
    
    def step4(self, order: int) -> Optional[int]:
        next_order = self.client.action(self, order)
        return next_order

    def calc_cost(self):
        self.cost += (BACKLOG_COST * self.backlog) + (INVENTORY_COST * self.inventory)

    def action(self, order):
        return order

    def __repr__(self):
        return "order: {}, backlog: {}, inventory: {}, cost: {}".format(
            self.order, self.backlog, self.inventory, self.cost
        )


class DelayUnit(Unit):
    inventory = DELAY_INVENTORY_INITIAL
    order = 0

    @property
    def inventories(self):
        return [self.inventory]

    def step1(self, transport: int) -> Optional[None]:
        if transport is not None:
            next_transport = self.inventory
            self.inventory = transport
            return next_transport
        else:
            return None

    def step2(self, order: int) -> Optional[None]:
        next_order = self.order
        if order is not None:
            self.order = order
        return next_order

    def step3(self, transport: int) -> Optional[int]:
        self.inventory += transport
        return 0

    def step4(self, order: int) -> Optional[int]:
        if order is not None:
            self.order = order
        return None


class CustomerUnit(Unit):
    @property
    def inventories(self):
        return []

    def step1(self, _):
        return None

    def step2(self, _):
        next_order = random.randrange(MIN_CUSTOMER_ORDER, MAX_CUSTOMER_ORDER)
        return next_order

    def step3(self, _):
        return None

    def step4(self, _):
        return None


class ManufacturerUnit(Unit):
    inventory_1 = DELAY_INVENTORY_INITIAL
    inventory_2 = DELAY_INVENTORY_INITIAL

    order = 0

    @property
    def inventories(self):
        return [self.inventory_1, self.inventory_2]

    def step1(self, _):
        next_transport = self.inventory_1
        self.inventory_1 = self.inventory_2
        self.inventory_2 = self.order
        self.order = 0
        return next_transport

    def step2(self, _):
        return None

    def step3(self, _):
        return 0

    def step4(self, order):
        self.order = order
        return None

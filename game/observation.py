# -*- coding: utf-8 -*-
from typing import List

from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from .unit import PlayerUnit


class ObservationUnit(object):
    order: int = 0
    backlog: int = 0
    inventory: int = 0
    cost: int = 0

    def __init__(
        self,
        order: int = 0,
        backlog: int = 0,
        inventory: int = 0,
        cost: int = 0
    ) -> None:
        self.order = order
        self.backlog = backlog
        self.inventory = inventory
        self.cost = cost


class Observation(object):
    inventories: List[int]
    unit: "ObservationUnit"

    def __init__(
        self,
        inventories: List[int],
        player_unit: "PlayerUnit",
    ) -> None:
        self.inventories = inventories
        self.unit = ObservationUnit(
            order=player_unit.order,
            backlog=player_unit.backlog,
            inventory=player_unit.inventory,
            cost=player_unit.cost,
        )

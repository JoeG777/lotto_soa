import abc
from typing import Any
from dataclasses import asdict

from src.draw.domain.models import LottoDraw, DrawerConfig


class IDrawer(metaclass=abc.ABCMeta):
    def __init__(self, config: dict[str, Any] = asdict(DrawerConfig())) -> None:
        self.WINNING_NUMBERS_SET = config["WINNING_NUMBERS_SET"]
        self.WINNING_NUMBERS_TO_SELECT = config["WINNING_NUMBERS_TO_SELECT"]
        self.SUPER_NUMBER_SET = config["SUPER_NUMBER_SET"]
        self.SUPER_NUMBER_TO_SELECT = config["SUPER_NUMBER_TO_SELECT"]

    @abc.abstractmethod
    def draw(self) -> LottoDraw:
        raise NotImplementedError

    @abc.abstractmethod
    def draw_winning_numbers(self) -> list[int]:
        raise NotImplementedError

    @abc.abstractmethod
    def draw_super_number(self) -> list[int]:
        raise NotImplementedError

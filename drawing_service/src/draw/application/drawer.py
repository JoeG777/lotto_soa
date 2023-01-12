import random

from src.draw.application.models import LottoDraw


class Drawer:
    WINNING_NUMBERS_SET = range(1, 50)
    WINNING_NUMBERS_TO_SELECT = 6
    SUPER_NUMBER_SET = range(0, 10)
    SUPER_NUMBER_TO_SELECT = 1

    @classmethod
    def draw(cls) -> LottoDraw:
        winning_numbers = cls.draw_winning_numbers()
        super_number = cls.draw_super_number()
        return LottoDraw(winning_numbers=winning_numbers, super_number=super_number)

    @classmethod
    def draw_winning_numbers(cls) -> list[int]:
        winning_numbers = random.sample(
            cls.WINNING_NUMBERS_SET, k=cls.WINNING_NUMBERS_TO_SELECT
        )
        return winning_numbers

    @classmethod
    def draw_super_number(cls) -> list[int]:
        super_number = random.sample(cls.SUPER_NUMBER_SET, k=cls.SUPER_NUMBER_TO_SELECT)
        return super_number

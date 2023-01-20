import random


from src.draw.domain.models import LottoDraw

from src.draw.domain.i_drawer import IDrawer
from src.draw.adapters.mq.lotto_draw_event_handler import LottoDrawEventHandler


class Drawer(IDrawer):
    def draw(self) -> LottoDraw:
        winning_numbers = self.draw_winning_numbers()
        super_number = self.draw_super_number()
        lotto_results = LottoDraw(
            winning_numbers=winning_numbers, super_number=super_number
        )
        LottoDrawEventHandler.lotto_draw_event_created(lotto_results)
        return lotto_results

    def draw_winning_numbers(self) -> list[int]:
        winning_numbers = random.sample(
            self.WINNING_NUMBERS_SET, k=self.WINNING_NUMBERS_TO_SELECT
        )
        return winning_numbers

    def draw_super_number(self) -> list[int]:
        super_number = random.sample(
            self.SUPER_NUMBER_SET, k=self.SUPER_NUMBER_TO_SELECT
        )
        return super_number

import abc

from src.draw.domain.models import LottoDraw


class ILottoDrawEventHandler(metaclass=abc.ABCMeta):
    @abc.abstractmethod
    def lotto_draw_event_created(self, lotto_results: LottoDraw) -> None:
        raise NotImplementedError

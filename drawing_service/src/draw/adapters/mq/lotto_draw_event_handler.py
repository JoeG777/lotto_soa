import abc

from src.draw.adapters.mq.dto.lotto_draw_event import LottoDrawEvent
from src.draw.domain.models import LottoDraw


class ILottoDrawEventHandler(metaclass=abc.ABCMeta):
    @abc.abstractclassmethod
    def lotto_draw_event_created(cls, lotto_results: LottoDraw) -> None:
        raise NotImplementedError


from datetime import datetime

from src.draw.adapters.mq.publisher import Publisher


class LottoDrawEventHandler:
    @classmethod
    def lotto_draw_event_created(cls, lotto_results: LottoDraw) -> None:
        Publisher.publish_message(
            LottoDrawEvent(lotto_draw=lotto_results, timestamp=datetime.now())
        )
        return

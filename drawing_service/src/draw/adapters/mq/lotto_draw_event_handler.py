import abc
from datetime import datetime

from src.draw.common.autowire import Autowire
from src.draw.adapters.mq.publisher import Publisher
from src.draw.adapters.mq.dto.lotto_draw_event import LottoDrawEvent
from src.draw.domain.models import LottoDraw


class ILottoDrawEventHandler(metaclass=abc.ABCMeta):
    @abc.abstractmethod
    def lotto_draw_event_created(self, lotto_results: LottoDraw) -> None:
        raise NotImplementedError




class LottoDrawEventHandler(ILottoDrawEventHandler):
    publisher: Publisher

    def __init__(self, publisher: Publisher = Autowire(Publisher)) -> None:
        self.publisher = publisher

    def lotto_draw_event_created(self, lotto_results: LottoDraw) -> None:
        self.publisher.publish_message(
            LottoDrawEvent(lotto_draw=lotto_results, timestamp=datetime.now())
        )
        return

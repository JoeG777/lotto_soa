from datetime import datetime
from pydantic import BaseModel, Field
import json

from src.draw.domain.models import LottoDraw
from src.draw.common import constants


class LottoDrawEvent(BaseModel):
    lotto_draw: LottoDraw = Field(
        ..., title="Lotto Draw", description="The object holding the lotto numbers"
    )
    timestamp: datetime = Field(
        datetime.now().strftime(constants.TIMESTAMP_FORMAT),
        title="Timestamp",
        description="Timestamp of the event",
    )

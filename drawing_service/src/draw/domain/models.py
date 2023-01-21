from dataclasses import dataclass, field


@dataclass
class LottoDraw:
    winning_numbers: list[int]
    super_number: list[int]


@dataclass
class DrawerConfig:
    WINNING_NUMBERS_SET: list[int] = field(default_factory=lambda: list(range(1, 50)))
    WINNING_NUMBERS_TO_SELECT: int = 6
    SUPER_NUMBER_SET: list[int] = field(default_factory=lambda: list(range(0, 10)))
    SUPER_NUMBER_TO_SELECT: int = 1

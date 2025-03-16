from typing import List
from enum import Enum


class Frequency(Enum):
    DAILY = 1
    WEEKLY = 2
    MONTHLY = 3


FREQUENCIES: List[str] = [freq.name for freq in Frequency]
FREQUENCIES_REGEX: str = "^" + "|".join(FREQUENCIES) + "$"
from typing import List
from enum import Enum


class Frequency(Enum):
    WEEKLY = 1
    MONTHLY = 2
    # DAILY = 3 ; for now not allowing this frequency becuase it will reqiure smarter bot


FREQUENCIES: List[str] = [freq.name for freq in Frequency]
FREQUENCIES_REGEX: str = "^" + "|".join(FREQUENCIES) + "$"

FREQUENCY_MAP_TO_HEBREW: dict[Frequency, str] = {
    Frequency.WEEKLY: "שבועות",
    Frequency.MONTHLY: "חודשים",
}
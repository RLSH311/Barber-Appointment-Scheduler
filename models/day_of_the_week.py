from typing import List
from enum import Enum


class DayOfTheWeek(Enum):
    SUNDAY = 1
    MONDAY = 2
    TUESDAY = 3
    WEDNESDAY = 4
    THURSDAY = 5
    FRIDAY = 6
    SATURDAY = 7


DAYS_OF_THE_WEEKS: List[str] = [day.name for day in DayOfTheWeek]
DAYS_OF_THE_WEEKS_REGEX: str = "^" + "|".join(DAYS_OF_THE_WEEKS) + "$"

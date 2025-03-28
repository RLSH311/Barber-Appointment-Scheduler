from typing import List
from enum import Enum


class DayOfTheWeek(Enum):
    SUN = 1
    MON = 2
    TUE = 3
    WED = 4
    THU = 5
    FRI = 6
    SAT = 7

DAYS_OF_THE_WEEKS: List[str] = [day.name for day in DayOfTheWeek]
DAYS_OF_THE_WEEKS_REGEX: str = "^" + "|".join(DAYS_OF_THE_WEEKS) + "$"

DAYS_MAP_TO_HEBREW: dict[DayOfTheWeek, str] = {
    DayOfTheWeek.SUN: "ראשון",
    DayOfTheWeek.MON: "שני",
    DayOfTheWeek.TUE: "שלישי",
    DayOfTheWeek.WED: "רביעי",
    DayOfTheWeek.THU: "חמישי",
    DayOfTheWeek.FRI: "שישי",
    DayOfTheWeek.SAT: "שבת",
}
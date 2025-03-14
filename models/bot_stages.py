from enum import Enum


class BotStages(Enum):
    EMAIL = 1
    FREQUENCY = 2
    INTERVAL = 3
    DAY_OF_THE_WEEK = 4
    START_HOUR = 5
    END_HOUR = 6

from typing import List
from statistics import mean, StatisticsError


def get_average_speed(set_var: List[List[float | bool]]) -> float | int:
    try:
        return mean([i[0] for i in set_var if i[1]])

    except StatisticsError:
        raise StatisticsError("Mean not calculated, none of the speed is valid")

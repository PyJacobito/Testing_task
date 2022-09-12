from typing import List
from statistics import mean, StatisticsError


def get_average_speed(set_var: List[List[float | bool]]) -> float | int:
    try:
        return mean([i[0] for i in set_var if i[1] == True])

    except StatisticsError:
        raise StatisticsError("None of the speeds are valid, mean cannot be calculated")

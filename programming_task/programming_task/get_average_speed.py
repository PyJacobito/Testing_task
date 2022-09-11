from typing import Set, List
from statistics import mean

def get_average_speed(set_var: Set[List[float, bool]]) -> float:
    return mean([i[0] for i in set_var if i[1] == True])
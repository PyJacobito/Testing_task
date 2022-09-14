from programming_task.programming_task.get_average_speed import get_average_speed
from programming_task.programming_task.constatnts import get_speed_list
from programming_task.tests.test_constants import test_speed_list
from statistics import StatisticsError
import pytest


@pytest.mark.parametrize(
    "input_var, exp_result",
    [
        ([[50, True], [60, True], [70, True]], 60),
        ([[50, False], [60, True], [70, True]], 65),
        ([[50, True], [60, False], [70, True]], 60),
        ([[50, True], [60, True], [70, False]], 55),
        ([[50, False], [60, False], [70, False], [70, True]], 70),
        ([[50, True], [60, False], [70, False]], 50),
        ([[50, True], [60, True], [70, True], [80, True]], 65),
        ([[0, True], [0, True], [0, True]], 0),
    ],
)
def test_get_average_speed(input_var, exp_result):
    if test_speed_list():
        assert isinstance(get_average_speed(get_speed_list()), (int, float))
        assert get_average_speed(input_var) == exp_result

        try:
            assert get_average_speed([[50, False], [60, False], [70, False]])
        except StatisticsError:
            assert True

    else:
        assert False

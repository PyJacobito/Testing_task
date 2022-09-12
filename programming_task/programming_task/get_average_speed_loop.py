from programming_task.programming_task.get_average_speed import get_average_speed
from programming_task.programming_task import constatnts
from importlib import reload

while True:
    reload(constatnts)
    get_average_speed(constatnts.get_speed_list())
    print(get_average_speed(constatnts.get_speed_list()))

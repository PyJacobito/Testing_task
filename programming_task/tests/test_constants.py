from programming_task.programming_task.constatnts import get_speed_list


def test_speed_list() -> bool:
    assert isinstance(get_speed_list(), list)

    for i in get_speed_list():
        assert len(i) == 2
        assert isinstance(i[0], (int, float))
        assert isinstance(i[1], bool)

    return True

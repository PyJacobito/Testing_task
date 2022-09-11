from programming_task.programming_task.constatnts import speed_set

def test_speed_set():
    assert isinstance(speed_set, set)

    for i in speed_set:
        assert len(i) == 2
        assert isinstance(i[0], float)
        assert isinstance(i[1], float)
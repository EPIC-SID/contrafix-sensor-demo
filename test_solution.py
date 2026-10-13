from solution import average_reading


def test_normal_readings():
    assert average_reading([10, 20, 30]) == 20


def test_missing_readings_are_ignored():
    assert average_reading([10, None, 20]) == 15


def test_zero_is_a_real_reading():
    assert average_reading([0, 10, None]) == 5


def test_only_zeroes_are_valid():
    assert average_reading([0, 0, None]) == 0


def test_negative_readings_are_valid():
    assert average_reading([-10, 0, None]) == -5


def test_all_missing_returns_none():
    assert average_reading([None, None]) is None


def test_empty_batch_returns_none():
    assert average_reading([]) is None

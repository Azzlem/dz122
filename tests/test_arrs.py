from utils import arrs


def test_get():
    assert arrs.get([1, 2, 3], 1, "test") == 2
    assert arrs.get(['test'], 0, "test") == "test"
    assert arrs.get([], -1, 'test') == "test"
    assert arrs.get(['t', 't'], 0, "test") == "t"

def test_slice():
    assert arrs.my_slice([1, 2, 3, 4], 1, 3) == [2, 3]
    assert arrs.my_slice([1, 2, 3], 1) == [2, 3]
    assert arrs.my_slice([1, 2, 3], -3) == [1, 2, 3]
    assert arrs.my_slice([], 3) == []
    assert arrs.my_slice([1, 2, 3]) == [1, 2, 3]
    assert arrs.my_slice([1, 2, 3], -6) == [1, 2, 3]

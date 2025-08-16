from median_of_two_sorted_arrays import Solution
from pytest import fixture


@fixture
def s() -> Solution:
    return Solution()


def test_empty_1(s: Solution):
    assert s.findMedianSortedArrays([], [1]) == 1


def test_1_empty(s: Solution):
    assert s.findMedianSortedArrays([1], []) == 1


def test_12_empty(s: Solution):
    assert s.findMedianSortedArrays([1, 2], []) == 1.5


def test_123_empty(s: Solution):
    assert s.findMedianSortedArrays([1, 2, 3], []) == 2


def test_13_2(s: Solution):
    assert s.findMedianSortedArrays([1, 3], [2]) == 2


def test_134_2(s: Solution):
    assert s.findMedianSortedArrays([1, 3, 4], [2]) == 2.5


def test_12_34(s: Solution):
    assert s.findMedianSortedArrays([1, 2], [3, 4]) == 2.5


def test_34_12(s: Solution):
    assert s.findMedianSortedArrays([3, 4], [1, 2]) == 2.5


def test_11111_14899(s: Solution):
    assert s.findMedianSortedArrays([1, 1, 1, 1, 1], [1, 4, 8, 9, 9]) == 1


def test_1689_2348(s: Solution):
    assert s.findMedianSortedArrays([1, 6, 8, 9], [2, 3, 4, 8]) == 5


def test_1357_24668(s: Solution):
    assert s.findMedianSortedArrays([1, 3, 5, 7], [2, 4, 6, 6, 8]) == 5

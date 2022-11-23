from minimum_jumps_to_reach_home import Solution
from pytest import fixture


@fixture
def s() -> Solution:
    return Solution()


def test_first_example(s: Solution):
    assert s.minimumJumps(forbidden=[14, 4, 18, 1, 15], a=3, b=15, x=9) == 3


def test_second_example(s: Solution):
    assert s.minimumJumps(forbidden=[8, 3, 16, 6, 12, 20], a=15, b=13, x=11) == -1


def test_third_example(s: Solution):
    assert s.minimumJumps(forbidden=[1, 6, 2, 14, 5, 17, 4], a=16, b=9, x=7) == 2

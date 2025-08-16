from typing import List

import pytest
from kth_smallest_pair_distance import Solution


@pytest.fixture
def s() -> Solution:
    return Solution()


@pytest.mark.parametrize(
    "nums,k,want",
    [
        pytest.param([1, 3, 1], 1, 0, id="example 1"),
        pytest.param([1, 1, 1], 1, 0, id="example 2"),
        pytest.param([1, 6, 1], 3, 5, id="example 3"),
        pytest.param([62, 100, 4], 2, 58, id="example 4"),
    ],
)
def test_solution(s: Solution, nums: List[int], k: int, want: int):
    got = s.smallestDistancePair(nums, k)
    assert got == want, f"got != want, {got} != {want}"

"""Tests for the fairsharer.my_module module.
"""
from fairsharer.fair_sharer import fair_sharer


def test_fair_sharer():
    """Test the examples given in the assignment."""

    #1 iteration
    assert fair_sharer([0, 1000, 800, 0], 1) == [100.0, 800.0, 900.0, 0.0]

    #2 iterations
    assert fair_sharer([0, 1000, 800, 0], 2) == [100.0, 890.0, 720.0, 90.0]

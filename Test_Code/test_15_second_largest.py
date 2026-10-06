import importlib.util
from pathlib import Path

program_path = Path(__file__).resolve().parents[1] / "Code" / "15_second_largest.py"

spec = importlib.util.spec_from_file_location("second_largest", program_path)
module = importlib.util.module_from_spec(spec)
spec.loader.exec_module(module)

second_largest = module.second_largest


def test_second_largest():
    assert second_largest([10, 20, 30, 40]) == 30


def test_second_largest_2():
    assert second_largest([5, 15, 10, 20]) == 15


def test_with_duplicates():
    assert second_largest([10, 20, 20, 30]) == 20


def test_negative_numbers():
    assert second_largest([-10, -5, -20]) == -10


def test_not_enough_unique_numbers():
    assert second_largest([5, 5, 5]) is None
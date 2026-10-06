import importlib.util
from pathlib import Path

program_path = Path(__file__).resolve().parents[1] / "Code" / "18_missing_number.py"

spec = importlib.util.spec_from_file_location("missing_number", program_path)
module = importlib.util.module_from_spec(spec)
spec.loader.exec_module(module)

find_missing_number = module.find_missing_number


def test_missing_4():
    assert find_missing_number([1, 2, 3, 5], 5) == 4


def test_missing_3():
    assert find_missing_number([1, 2, 4, 5], 5) == 3


def test_missing_1():
    assert find_missing_number([2, 3, 4, 5], 5) == 1


def test_missing_5():
    assert find_missing_number([1, 2, 3, 4], 5) == 5


def test_missing_2():
    assert find_missing_number([1, 3, 4, 5], 5) == 2
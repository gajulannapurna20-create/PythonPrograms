import importlib.util
from pathlib import Path

program_path = Path(__file__).resolve().parents[1] / "Code" / "19_find_duplicates.py"

spec = importlib.util.spec_from_file_location("find_duplicates", program_path)
module = importlib.util.module_from_spec(spec)
spec.loader.exec_module(module)

find_duplicates = module.find_duplicates


def test_duplicates():
    assert find_duplicates([1, 2, 2, 3, 4, 4]) == [2, 4]


def test_duplicates_2():
    assert find_duplicates([5, 5, 6, 7, 7]) == [5, 7]


def test_no_duplicates():
    assert find_duplicates([1, 2, 3, 4]) == []


def test_all_duplicates():
    assert find_duplicates([3, 3, 3]) == [3]


def test_multiple_duplicates():
    assert find_duplicates([1, 1, 2, 2, 3, 3]) == [1, 2, 3]
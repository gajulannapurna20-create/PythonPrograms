import importlib.util
from pathlib import Path

program_path = Path(__file__).resolve().parents[1] / "Code" / "16_remove_duplicates.py"

spec = importlib.util.spec_from_file_location("remove_duplicates", program_path)
module = importlib.util.module_from_spec(spec)
spec.loader.exec_module(module)

remove_duplicates = module.remove_duplicates


def test_remove_duplicates():
    assert remove_duplicates([1, 2, 2, 3, 4, 4]) == [1, 2, 3, 4]


def test_remove_duplicates_2():
    assert remove_duplicates([5, 5, 6, 7, 7]) == [5, 6, 7]


def test_no_duplicates():
    assert remove_duplicates([1, 2, 3]) == [1, 2, 3]


def test_all_duplicates():
    assert remove_duplicates([4, 4, 4]) == [4]


def test_empty_list():
    assert remove_duplicates([]) == []
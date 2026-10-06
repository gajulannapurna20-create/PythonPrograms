import importlib.util
from pathlib import Path

program_path = Path(__file__).resolve().parents[1] / "Code" / "17_common_elements.py"

spec = importlib.util.spec_from_file_location("common_elements", program_path)
module = importlib.util.module_from_spec(spec)
spec.loader.exec_module(module)

common_elements = module.common_elements


def test_common_elements():
    assert common_elements([1, 2, 3, 4], [3, 4, 5, 6]) == [3, 4]


def test_common_elements_2():
    assert common_elements([10, 20, 30], [20, 30, 40]) == [20, 30]


def test_no_common_elements():
    assert common_elements([1, 2], [3, 4]) == []


def test_one_common_element():
    assert common_elements([1, 2, 3], [3, 4, 5]) == [3]


def test_duplicate_elements():
    assert common_elements([1, 1, 2, 3], [1, 2]) == [1, 2]
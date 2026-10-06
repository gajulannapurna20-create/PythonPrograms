import importlib.util
from pathlib import Path

program_path = Path(__file__).resolve().parents[1] / "Code" / "02_largest_of_three.py"

spec = importlib.util.spec_from_file_location("largest_of_three", program_path)
module = importlib.util.module_from_spec(spec)
spec.loader.exec_module(module)

largest_of_three = module.largest_of_three


def test_largest_first():
    assert largest_of_three(30, 20, 10) == 30


def test_largest_second():
    assert largest_of_three(10, 40, 20) == 40


def test_largest_third():
    assert largest_of_three(10, 20, 50) == 50


def test_equal_numbers():
    assert largest_of_three(10, 10, 5) == 10


def test_negative_numbers():
     assert largest_of_three(-5, -2, -10) == -2
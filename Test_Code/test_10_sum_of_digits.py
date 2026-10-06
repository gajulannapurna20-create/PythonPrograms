import importlib.util
from pathlib import Path

program_path = Path(__file__).resolve().parents[1] / "Code" / "10_sum_of_digits.py"

spec = importlib.util.spec_from_file_location("sum_of_digits", program_path)
module = importlib.util.module_from_spec(spec)
spec.loader.exec_module(module)

sum_of_digits = module.sum_of_digits


def test_sum_of_digits():
    assert sum_of_digits(12345) == 15


def test_sum_of_digits_2():
    assert sum_of_digits(908) == 17


def test_single_digit():
    assert sum_of_digits(7) == 7


def test_zero():
    assert sum_of_digits(0) == 0


def test_negative_number():
    assert sum_of_digits(-123) == 6
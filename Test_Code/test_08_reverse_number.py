import importlib.util
from pathlib import Path

program_path = Path(__file__).resolve().parents[1] / "Code" / "08_reverse_number.py"

spec = importlib.util.spec_from_file_location("reverse_number", program_path)
module = importlib.util.module_from_spec(spec)
spec.loader.exec_module(module)

reverse_number = module.reverse_number


def test_reverse_number():
    assert reverse_number(12345) == 54321


def test_reverse_number_2():
    assert reverse_number(9080) == 809


def test_single_digit():
    assert reverse_number(7) == 7


def test_zero():
    assert reverse_number(0) == 0


def test_negative_number():
    assert reverse_number(-123) == -321
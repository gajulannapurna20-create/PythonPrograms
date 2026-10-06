import importlib.util
from pathlib import Path

program_path = Path(__file__).resolve().parents[1] / "Code" / "04_factorial.py"

spec = importlib.util.spec_from_file_location("factorial", program_path)
module = importlib.util.module_from_spec(spec)
spec.loader.exec_module(module)

factorial = module.factorial


def test_factorial_zero():
    assert factorial(0) == 1


def test_factorial_one():
    assert factorial(1) == 1


def test_factorial_three():
    assert factorial(3) == 6


def test_factorial_five():
    assert factorial(5) == 120


def test_factorial_four():
    assert factorial(4) == 24
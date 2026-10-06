import importlib.util
from pathlib import Path

program_path = Path(__file__).resolve().parents[1] / "Code" / "05_fibonacci_series.py"

spec = importlib.util.spec_from_file_location("fibonacci_series", program_path)
module = importlib.util.module_from_spec(spec)
spec.loader.exec_module(module)

fibonacci_series = module.fibonacci_series


def test_fibonacci_zero():
    assert fibonacci_series(0) == []


def test_fibonacci_one():
    assert fibonacci_series(1) == [0]


def test_fibonacci_three():
    assert fibonacci_series(3) == [0, 1, 1]


def test_fibonacci_five():
    assert fibonacci_series(5) == [0, 1, 1, 2, 3]


def test_fibonacci_seven():
    assert fibonacci_series(7) == [0, 1, 1, 2, 3, 5, 8]
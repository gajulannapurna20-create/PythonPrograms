import importlib.util
from pathlib import Path

program_path = Path(__file__).resolve().parents[1] / "Code" / "01_even_odd.py"

spec = importlib.util.spec_from_file_location("even_odd", program_path)
module = importlib.util.module_from_spec(spec)
spec.loader.exec_module(module)

Even_Odd = module.Even_Odd


def test_even_number():
    assert Even_Odd(10) == "Even"


def test_odd_number():
    assert Even_Odd(7) == "Odd"


def test_zero():
    assert Even_Odd(0) == "Even"


def test_negative_even():
    assert Even_Odd(-4) == "Even"


def test_negative_odd():
    assert Even_Odd(-5) == "Odd"
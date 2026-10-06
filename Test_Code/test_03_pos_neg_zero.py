import importlib.util
from pathlib import Path

program_path = Path(__file__).resolve().parents[1] / "Code" / "03_pos_neg_zero.py"

spec = importlib.util.spec_from_file_location("pos_neg_zero", program_path)
module = importlib.util.module_from_spec(spec)
spec.loader.exec_module(module)

check_number = module.check_number


def test_positive_number():
    assert check_number(10) == "Positive"


def test_negative_number():
    assert check_number(-5) == "Negative"


def test_zero():
    assert check_number(0) == "Zero"


def test_positive_number_2():
    assert check_number(25) == "Positive"


def test_negative_number_2():
    assert check_number(-15) == "Negative"
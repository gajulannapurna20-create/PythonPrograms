import importlib.util
from pathlib import Path

program_path = Path(__file__).resolve().parents[1] / "Code" / "09_palindrome_number.py"

spec = importlib.util.spec_from_file_location("palindrome_number", program_path)
module = importlib.util.module_from_spec(spec)
spec.loader.exec_module(module)

is_palindrome = module.is_palindrome


def test_palindrome_number():
    assert is_palindrome(121) is True


def test_non_palindrome_number():
    assert is_palindrome(123) is False


def test_palindrome_number_2():
    assert is_palindrome(1221) is True


def test_single_digit():
    assert is_palindrome(7) is True


def test_zero():
    assert is_palindrome(0) is True
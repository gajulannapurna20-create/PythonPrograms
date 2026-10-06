import importlib.util
from pathlib import Path

program_path = Path(__file__).resolve().parents[1] / "Code" / "13_palindrome_string.py"

spec = importlib.util.spec_from_file_location("palindrome_string", program_path)
module = importlib.util.module_from_spec(spec)
spec.loader.exec_module(module)

is_palindrome_string = module.is_palindrome_string


def test_palindrome_madam():
    assert is_palindrome_string("madam") is True


def test_non_palindrome_hello():
    assert is_palindrome_string("hello") is False


def test_palindrome_level():
    assert is_palindrome_string("level") is True


def test_single_character():
    assert is_palindrome_string("a") is True


def test_empty_string():
    assert is_palindrome_string("") is True
import importlib.util
from pathlib import Path

program_path = Path(__file__).resolve().parents[1] / "Code" / "11_vowels_consonants.py"

spec = importlib.util.spec_from_file_location("vowels_consonants", program_path)
module = importlib.util.module_from_spec(spec)
spec.loader.exec_module(module)

count_vowels_consonants = module.count_vowels_consonants


def test_hello_world():
    assert count_vowels_consonants("Hello World") == (3, 7)


def test_python():
    assert count_vowels_consonants("Python") == (1, 5)


def test_all_vowels():
    assert count_vowels_consonants("aeiou") == (5, 0)


def test_all_consonants():
    assert count_vowels_consonants("bcdf") == (0, 4)


def test_empty_string():
    assert count_vowels_consonants("") == (0, 0)
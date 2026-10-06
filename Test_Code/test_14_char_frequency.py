import importlib.util
from pathlib import Path

program_path = Path(__file__).resolve().parents[1] / "Code" / "14_char_frequency.py"

spec = importlib.util.spec_from_file_location("char_frequency", program_path)
module = importlib.util.module_from_spec(spec)
spec.loader.exec_module(module)

character_frequency = module.character_frequency


def test_hello():
    assert character_frequency("hello") == {"h": 1, "e": 1, "l": 2, "o": 1}


def test_apple():
    assert character_frequency("apple") == {"a": 1, "p": 2, "l": 1, "e": 1}


def test_single_character():
    assert character_frequency("a") == {"a": 1}


def test_empty_string():
    assert character_frequency("") == {}


def test_repeated_character():
    assert character_frequency("aaa") == {"a": 3}
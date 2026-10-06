import importlib.util
from pathlib import Path

program_path = Path(__file__).resolve().parents[1] / "Code" / "12_reverse_string.py"

spec = importlib.util.spec_from_file_location("reverse_string", program_path)
module = importlib.util.module_from_spec(spec)
spec.loader.exec_module(module)

reverse_string = module.reverse_string


def test_reverse_hello():
    assert reverse_string("Hello") == "olleH"


def test_reverse_python():
    assert reverse_string("Python") == "nohtyP"


def test_empty_string():
    assert reverse_string("") == ""


def test_single_character():
    assert reverse_string("A") == "A"


def test_reverse_number_string():
    assert reverse_string("12345") == "54321"
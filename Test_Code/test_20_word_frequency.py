import importlib.util
from pathlib import Path

program_path = Path(__file__).resolve().parents[1] / "Code" / "20_word_frequency.py"

spec = importlib.util.spec_from_file_location("word_frequency", program_path)
module = importlib.util.module_from_spec(spec)
spec.loader.exec_module(module)

word_frequency = module.word_frequency


def test_hello_world():
    assert word_frequency("hello world hello") == {"hello": 2, "world": 1}


def test_python():
    assert word_frequency("python is easy python") == {
        "python": 2,
        "is": 1,
        "easy": 1
    }


def test_single_word():
    assert word_frequency("hello") == {"hello": 1}


def test_empty_string():
    assert word_frequency("") == {}


def test_case_insensitive():
    assert word_frequency("Hello hello") == {"hello": 2}
import importlib.util
from pathlib import Path

program_path = Path(__file__).resolve().parents[1] / "Code" / "06_prime_number.py"

spec = importlib.util.spec_from_file_location("prime_number", program_path)
module = importlib.util.module_from_spec(spec)
spec.loader.exec_module(module)

is_prime = module.is_prime


def test_prime_number():
    assert is_prime(7) is True


def test_non_prime_number():
    assert is_prime(10) is False


def test_prime_number_2():
    assert is_prime(13) is True


def test_one_is_not_prime():
    assert is_prime(1) is False


def test_zero_is_not_prime():
    assert is_prime(0) is False
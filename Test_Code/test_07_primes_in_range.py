import importlib.util
from pathlib import Path

program_path = Path(__file__).resolve().parents[1] / "Code" / "07_primes_in_range.py"

spec = importlib.util.spec_from_file_location("primes_in_range", program_path)
module = importlib.util.module_from_spec(spec)
spec.loader.exec_module(module)

primes_in_range = module.primes_in_range


def test_primes_1_to_10():
    assert primes_in_range(1, 10) == [2, 3, 5, 7]


def test_primes_10_to_20():
    assert primes_in_range(10, 20) == [11, 13, 17, 19]


def test_primes_1_to_5():
    assert primes_in_range(1, 5) == [2, 3, 5]


def test_no_primes():
    assert primes_in_range(14, 16) == []


def test_single_prime():
    assert primes_in_range(7, 7) == [7]
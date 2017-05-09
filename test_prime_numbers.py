"""Unit tests for prime_numbers module."""

import unittest
from prime_numbers import prime_numbers


class TestPrimeGenerator(unittest.TestCase):

    def test_five(self):
        """Testing if prime numbers are correctly generated."""

        self.assertEqual(prime_numbers(5), [2, 3, 5])

    def test_prime_numbers(self):
        """Testing if prime numbers are correctly generated."""

        self.assertEqual(prime_numbers(20), [2, 3, 5, 7, 11, 13, 17, 19])

    
    def test_one_hundred(self):
        """Testing if prime numbers are correctly generated."""

        self.assertEqual(prime_numbers(100),
                         [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89,
                          97])

    def test_two_hundred(self):
        """Testing if prime numbers are correctly generated."""

        self.assertEqual(prime_numbers(200),
                         [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89,
                          97, 101, 103, 107, 109, 113,
                          127, 131, 137, 139, 149, 151, 157, 163, 167, 173, 179, 181, 191, 193, 197, 199])

    def test_list_output(self):
        """Testing if zero is correctly determined not to be prime."""

        self.assertEqual(prime_numbers(5), [2, 3, 5])

    def test_zero(self):
        """Testing if zero is correctly determined not to be prime."""

        self.assertEqual(prime_numbers(
            0), "Zero or One cannot be prime numbers.")
    
    def test_one(self):
        """"Testing if one is correctly determined not to be prime."""

        self.assertEqual(prime_numbers(
            1), "Zero or One cannot be prime numbers.")

    def test_two(self):
        """Testing if error returned if integer entered is 2."""

        self.assertEqual(prime_numbers("String"), "Only integers are allowed.")

    def test_invalid_type_string_list(self):
        """Testing if error returned if input not integer."""

        self.assertEqual(prime_numbers([]), "Only integers are allowed.")

    def test_invalid_type_string_set(self):
        """Testing if error returned if input not integer."""

        self.assertEqual(prime_numbers(set()), "Only integers are allowed.")

    def test_only_positive(self):
        """Testing if error returned if negative integers input."""

        self.assertEqual(
            prime_numbers(-1), "Not possible to generate prime numbers for integers less than 2.")


if __name__ == "__main__":
    unittest.main()
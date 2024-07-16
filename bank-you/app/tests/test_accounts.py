import unittest
from app.models.accounts import validate_new_account_number, validate_new_pin_code


class TestValidateAccountNumber(unittest.TestCase):

    def test_result_type_is_bool(self) -> None:
        result = validate_new_account_number(0)
        assertion_error_message = "result should be bool type"

        self.assertIsInstance(result, bool, assertion_error_message)

    def test_int_acceptance(self) -> None:
        result = validate_new_account_number(101)
        expected_output = True
        assertion_error_message = "result should be True"

        self.assertEqual(result, expected_output, assertion_error_message)

    def test_string_type_rejection(self) -> None:
        result = validate_new_account_number("0")
        expected_output = False
        assertion_error_message = "result should be False"

        self.assertEqual(result, expected_output, assertion_error_message)


class TestValidateNewPinCode(unittest.TestCase):

    def test_result_type_is_bool(self):
        result = validate_new_pin_code(0)
        assertion_error_message = "result should be bool type"

        self.assertIsInstance(result, bool, assertion_error_message)

    def test_pin_code_validation(self):
        result = validate_new_pin_code("000000")
        expected_output = True
        assertion_error_message = "result should be True"

        self.assertEqual(result, expected_output, assertion_error_message)


if __name__ == '__main__':
    unittest.main()

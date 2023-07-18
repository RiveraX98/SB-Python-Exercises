from unittest import TestCase
from convert import check_info, convert_currency
from app import app


class currrency_convert_test(TestCase):
    def test_check_info(self):
        self.assertEqual(check_info("USD", "JPY", "500"), "ok")
        self.assertEqual(check_info("USD", "ZZZ", "500"),
                         "Invalid currency code")
        self.assertEqual(check_info("USD", "JPY", "asd"), "Invalid Amount")

    def test_convert_currency(self):
        self.assertEqual(convert_currency("USD", "USD", "1"), 1)

    def test_verify_form_info(self):
        with app.test_client() as client:
            res = client.post(
                "/verify_form", data={"from": "USD", "into": "JPY", "amount": "500"})
            self.assertEqual(res.status_code, 302)
            self.assertEqual(res.location, "/convert")
            res = client.post(
                "/verify_form", data={"from": "USD", "into": "ZZZ", "amount": "500"})
            html = res.get_data(as_text=True)
            self.assertEqual(res.status_code, 200)
            self.assertIn(" <p>Invalid currency code</p>", html)

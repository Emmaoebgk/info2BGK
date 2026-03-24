import unittest
from informatika2.password import LenghtFilter, SpecialCharFilter, AndFilter


class PassTestCase(unittest.TestCase):
    def test_lenght_filter_if_password_is_ok(self):
        lenght = LenghtFilter()
        result= lenght.validate("1234678")
        self.assertEqual([],result)

    def test_lenght_filter_if_password_is_no_ok(self):
        lenght = LenghtFilter(8)
        result = lenght.validate("123")
        self.assertTrue(len(result)> 0)

    def test_special_char_if_not_ok(self):
        special_char_filter = SpecialCharFilter()
        result= special_char_filter.validate("adcdefghij")
        self.assertTrue(len(result) > 0)

    def test_special_char_if_ok(self):
        special_char_filter =SpecialCharFilter()
        result = special_char_filter.validate("adcd.efg*hij")
        self.assertEqual([], result)

    def test_and_if_not_ok(self):
        filters = []
        special_char_filter = SpecialCharFilter()
        filters.append(special_char_filter)
        lenght = LenghtFilter(8)
        filters.append(lenght)
        and_filter = AndFilter(filters)
        result = and_filter.validate("adcdefghij")
        self.assertTrue(len(result) > 0)
        result = and_filter.validate("ab.")
        self.assertTrue(len(result) > 0)

    def test_and_if_ok(self):
        filters = []
        special_char_filter = SpecialCharFilter()
        filters.append(special_char_filter)
        lenght = LenghtFilter(8)
        filters.append(lenght)
        and_filter = AndFilter(filters)
        result = and_filter.validate("adcd.efg,hij")
        self.assertEqual([], result)


if __name__ == '__main__':
    unittest.main()

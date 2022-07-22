import unittest

class UserInputTests(unittest.TestCase):
    #capitalized, 1-7 alpha characters
    def test_symbol(self):
        symbol_input = "NASDAQ"
        self.assertTrue(1 <= len(symbol_input) <= 7)
        self.assertTrue(symbol_input.isalpha())
        self.assertTrue(symbol_input.isupper())
    #1 numeric character, 1 or 2
    def test_chart_type(self):
        chart_type_input = 1
        self.assertTrue(1 <= chart_type_input <= 2)
    #1 numeric character, 1 - 4
    def test_time_series(self):
        time_series_input = 4
        self.assertTrue(1 <= time_series_input <= 4)
    #date type YYYY-MM-DD
    def test_start_date(self):
        start_date_input = "1984-12-30"
        self.assertEqual(len(start_date_input), 10)
        self.assertEqual(start_date_input[4:5], '-')
        self.assertEqual(start_date_input[7:8], '-')
        self.assertTrue(start_date_input[0:4].isnumeric)
        self.assertTrue(start_date_input[5:7].isnumeric)
        self.assertTrue(start_date_input[-2:].isnumeric)
    #date type YYYY-MM-DD
    def test_end_date(self):
        end_date_input = "2020-12-30"
        self.assertEqual(len(end_date_input), 10)
        self.assertEqual(end_date_input[4:5], '-')
        self.assertEqual(end_date_input[7:8], '-')
        self.assertTrue(end_date_input[0:4].isnumeric)
        self.assertTrue(end_date_input[5:7].isnumeric)
        self.assertTrue(end_date_input[-2:].isnumeric)

if __name__ == "__main__":
    unittest.main()
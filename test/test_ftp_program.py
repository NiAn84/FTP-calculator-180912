import unittest

from ftp_program import get_wkg, assemble_date


class TestOkValues(unittest.TestCase):
    def test_get_wkg_307_and_82(self):
        self.assertEqual(get_wkg(307, 82), 3.74)

    def test_get_wkg_253_and_65(self):
        self.assertEqual(get_wkg(253, 65), 3.89)

    def test_get_wkg_403_and_91(self):
        self.assertEqual(get_wkg(403, 91), 4.43)


class TestNotOkValues(unittest.TestCase):

    def test_new_entry_low_ftp(self):
        self.assertRaises(ValueError, get_wkg, 40, 80)

    def test_new_entry_negative_ftp(self):
        self.assertRaises(ValueError, get_wkg, -40, 80)

    def test_new_entry_high_ftp(self):
        self.assertRaises(ValueError, get_wkg, 600, 80)

    def test_new_entry_low_weight(self):
        self.assertRaises(ValueError, get_wkg, 200, 18)

    def test_new_entry_negative_weight(self):
        self.assertRaises(ValueError, get_wkg, 200, -18)

    def test_new_entry_high_weight(self):
        self.assertRaises(ValueError, get_wkg, 200, 203)



    def test_assemble_date_year_too_high(self):
        self.assertRaises(ValueError, assemble_date, 100, 10, 10)

    def test_assemble_date_month_too_high(self):
        self.assertRaises(ValueError, assemble_date, 99, 13, 10)

    def test_assemble_date_day_too_high(self):
        self.assertRaises(ValueError, assemble_date, 99, 10, 32)

    def test_assemble_date_year_negative(self):
        self.assertRaises(ValueError, assemble_date, -100, 10, 10)

    def test_assemble_date_month_negative(self):
        self.assertRaises(ValueError, assemble_date, 99, -13, 10)

    def test_assemble_date_day_negative(self):
        self.assertRaises(ValueError, assemble_date, 99, 10, -4)


if __name__ == '__main__':
    unittest.main()
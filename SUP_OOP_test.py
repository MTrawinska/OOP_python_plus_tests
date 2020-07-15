import unittest
from SUP_OOP import SurfingBoard, SUP

class SUPTest(unittest.TestCase):

    def test_isOn(self):
        self.assertIsNotNone(SurfingBoard.total_weight_incl_gear(8,56,2))
        self.assertIsNotNone(SUP.total_weight_incl_gear(8, 56, 2))

    def test_init_invalid_type(self):
        self.assertRaises(TypeError, SUP, "foo", 0, 1.5)
        self.assertRaises(TypeError, SUP, 1.5, 0, "foo")
        self.assertRaises(ValueError, SUP, 10, 5, 8, 65, "foo")

    def test_string(self):
        with self.assertRaises(TypeError):
            SUP.user_number("bubbaBar")
            SUP.user_weight("bubbaBar")
            SUP.user_number("bubbaBar")

    def test_float(self):
        with self.assertRaises(TypeError):
            SUP.user_number(1.2)
            SUP.user_weight(1.5677)
            SUP.user_number(0.2)

    def test_sup_weight_count(self):
        self.assertRaises(ValueError, SUP, 48, 48, 1, 1,"epoxy")

    def test_user_weight_count(self):
        self.assertRaises(ValueError, SUP, 10, 23, 1, 1,"epoxy")

    def test_gear_weight(self):
        self.assertRaises(ValueError, SUP, 8, 0, 10, 1,"epoxy")

    def test_user_count(self):
        self.assertRaises(ValueError, SUP, 8, 0, 1, 10,"epoxy")

    def test_init_valid(self):
        edge_case = SUP.individual_baby_SUP()
        edge_case = (8, 35, 8, 2, "epoxy")
        second_edge_case = SUP(8, 32, 1, 2, "epoxy")
        self.assertTrue(edge_case)
        self.assertTrue(second_edge_case)

    def test_total_sup_mass(self):
        sup = SUP(7, 35, 1, 3, "epoxy")
        expected_sup_mass = sup.sup_weight + ((sup.user_weight + sup.gear_weight) * sup.user_number)
        self.assertEqual(sup.total_SUP_mass, expected_sup_mass)

if __name__ == '__main__':
    unittest.main()

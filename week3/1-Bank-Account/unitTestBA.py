import unittest
from BankAccount import BankAccount


class BankAcount(unittest.TestCase):

    def setUp(self):
        self.ba = BankAccount("rado", 500, "$")

    def tearDown(self):
        pass

    def tets_create_new_BankAccount_class(self):
        self.assertEqual(self.ba.history(),"Account was created")
        self.assertTrue(isinstance(self.ba, BankAccount))

    def test_create_int_value_from_BankAccount(self):
        self.assertEqual(int(self.ba), 500)
    def test__str__in_BankAccount(self):
        self.assertEqual(str(self.ba),"Bank account for rado with balance of 500$")
    def test_balance(self):
        self.assertEqual(self.ba.balance(),500)
    def test_transfer_to(self):
        maria = BankAccount("Maria",200,"$")
        self.assertEqual(self.ba.transfer_to(maria,"$"),True)
        with self.assertRaises(TypeError) :
            self.ba.transfer_to("maria","$")
    def test_withdraw(self):
        self.assertTrue(self.ba.withdraw(200))
        self.assertFalse(self.ba.withdraw(900))
    def test_deposit(self):
        d = 1000
        self.ba.deposit(500)
        self.assertEqual(self.ba.balance(),1000)


if __name__ == '__main__':
    unittest.main()

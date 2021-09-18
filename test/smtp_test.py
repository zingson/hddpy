import unittest
from smtplib import SMTP

def smtpTest():
    print("------")


class MyTestCase(unittest.TestCase):
    def test_something(self):
        smtpTest()
        self.assertEqual(True, True)


if __name__ == '__main__':
    unittest.main()


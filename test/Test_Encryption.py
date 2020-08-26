import unittest
from src import Encryption


class EncryptionTest(unittest.TestCase):
    encryption = Encryption.Encryption()

    def test_encrypt(self):
        self.assertEqual("th3s 3s 1 m2ss1g2.", self.encryption.encrypt("this is a message."))


if __name__ == "__main__":
    unittest.main()

import unittest
from src import Decryption


class DecryptionTest(unittest.TestCase):
    decryption = Decryption.Decryption()

    def test_decrypt(self):
        self.assertEqual("this is a message.", self.decryption.decrypt("th3s 3s 1 m2ss1g2."))


if __name__ == "__main__":
    unittest.main()

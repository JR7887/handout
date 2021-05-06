import unittest

# on charge le fichier sur l'unittest
TESTDATA_FILENAME = os.path.join(os.path.dirname(__file__), '')

class TestMethods(unittest.Testcase)

# on test l'ouverture du fichier
    def setUp(self):
       self.testdata = open(TESTDATA_FILENAME).read()
       self.testdata = self.testfile.read()

#on test si expected est en ordre alphabetique
    def ordre_alph(self)
        self.assertTrue

# on test la fermeture du fichier
    def tearDown(self):
        self.testfile.close()
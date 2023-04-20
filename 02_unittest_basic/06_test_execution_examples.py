import unittest

#Żeby przetestować tylko poszcególną klasę testową używamy po nazwie pliku, nazwy klasy

#python -m unittest 06_test_execution_examples.TestClass2 -v

#W ten sam sposób możemy wywołać tylko poszczególny test

#python -m unittest 06_test_execution_examples.TestClass1.test_case_1 -v


#Flaga -f pozwala nam uruchomić testy do pierwszego Fail

#python -m unittest 06_test_execution_examples -v -f

class TestClass1(unittest.TestCase):

    def test_case_1(self):
        self.assertEqual('John Smith'.split(), ['John','Smith'])

    def test_case_2(self):
        self.assertTrue('apple'.islower())


class TestClass2(unittest.TestCase):

    def test_case_1(self):
        self.assertEqual('3.9'.split('.'), ['3', '9'])


class TestClass3(unittest.TestCase):

    def test_case_1(self):
        self.assertEqual('#'.join(['gym', 'sport']), 'gym#sport')





import unittest
from find_zero import find_zero


class TestFindZero(unittest.TestCase):
    """
    Тесты для функции find_zero
    """
    def _test_simple(self, s:str, ans):
        """
        Шаблон для простого теста
        """
        self.assertEqual(find_zero(s), ans)

    def test_empty(self):
        """
        Проверка c пустой строкой
        """
        self._test_simple('', -1)

    def test_no_zero(self):
        """
        Проверка со строкой без нулей но с единицами
        :return:
        """
        self._test_simple('111', -1)

    def test_1(self):
        self._test_simple("111111111111111111111111100000000", 25)


if __name__ == '__main__':
    unittest.main(verbosity=2)

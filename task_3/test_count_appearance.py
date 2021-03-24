import unittest
from count_appearance import *


class TestCountAppearance(unittest.TestCase):
    def _test_positive(self, test_setup):
        self.assertEqual(count_appearance(test_setup['data']), test_setup['answer'])

    def test_1(self):
        test_setup = {'data': {'lesson': [1594663200, 1594666800],
                               'pupil': [1594663340, 1594663389, 1594663390, 1594663395, 1594663396, 1594666472],
                               'tutor': [1594663290, 1594663430, 1594663443, 1594666473]},
                      'answer': 3117}
        self._test_positive(test_setup)

    def test_2(self):
        test_setup = {'data': {'lesson': [1594702800, 1594706400],
             'pupil': [1594702789, 1594704500, 1594702807, 1594704542, 1594704512, 1594704513, 1594704564, 1594705150,
                       1594704581, 1594704582, 1594704734, 1594705009, 1594705095, 1594705096, 1594705106, 1594706480,
                       1594705158, 1594705773, 1594705849, 1594706480, 1594706500, 1594706875, 1594706502, 1594706503,
                       1594706524, 1594706524, 1594706579, 1594706641],
             'tutor': [1594700035, 1594700364, 1594702749, 1594705148, 1594705149, 1594706463]},
            'answer': 3577}
        self._test_positive(test_setup)

    def test_3(self):
        test_setup = {'data': {'lesson': [1594692000, 1594695600],
             'pupil': [1594692033, 1594696347],
             'tutor': [1594692017, 1594692066, 1594692068, 1594696341]},
            'answer': 3565}
        self._test_positive(test_setup)

    def test_failure_garbage_data(self):
        """
        Проверка с ошибкой при подаче аргумента не словаря
        """
        self.assertRaises(CountAppearanceWrongData, count_appearance, None)

    def test_failure_wrong_dict(self):
        """
        Проверка с ошибкой при отсутсвии в списке нужных ключей
        """
        data = {'lesson': [11, 14],
                'pupoll': [10,12,13,14]}
        self.assertRaises(CountAppearanceWrongData, count_appearance, data)

    def test_failure_not_list(self):
        """
        Проверка с ошибкой при неправильном типе значения в словаре
        """
        data = {'lesson':1,
                'pupil':2,
                'tutor':3}
        self.assertRaises(CountAppearanceWrongData, count_appearance, data)

    def test_failure_wrong_list_len(self):
        """
        Проверка с ошибкой при неправильном количестве элементов в списках
        """
        data = {'lesson': [1],
                'pupil': [1,2,3,4],
                'tutor': [1,2,3,4]}
        self.assertRaises(CountAppearanceWrongInterval, count_appearance, data)
        data['lesson'] = [1,4]
        data['pupil'] = [1,2,3]
        self.assertRaises(CountAppearanceWrongInterval, count_appearance, data)
        data['pupil'] = [1,2,3,4]
        data['tutor'] = [1,2,3]
        self.assertRaises(CountAppearanceWrongInterval, count_appearance, data)

    def test_failure_wrong_interval(self):
        """
        Проверка с ошибкой, когда начало интервала больше конца интервала
        :return:
        """
        data = {'lesson': [1,2],
                'pupil': [3,1],
                'tutor': [1,2,3,4]}
        self.assertRaises(CountAppearanceWrongInterval, count_appearance, data)


if __name__ == '__main__':
    unittest.main(verbosity=2)

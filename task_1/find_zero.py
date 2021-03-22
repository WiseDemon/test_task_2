# def find_zero(s:str) -> int:
#     """
#     Поиск первого нуля с помощью встроенной функции find
#     :param s:
#     :return:
#     """
#     return s.find('0')

def find_zero(s:str) -> int:
    """
    Поиск первого нуля в строке, первая часть которой состоит из единиц,
    а вторая - из нулей.
    Бинарный поиск с досрочной остановкой.
    Функция не проверяет, действительно ли строка состоит только из нулей и единиц и правильный ли у них порядок,
    но поднимет исключение, если наткнется на неправильный символ.
    Алгоритмическая сложность: O(log n), n - длина строки.
    :param s:
    :return: Позиция первого нуля или -1, если нулей нет.
    :exception FindZeroException: обнаружен неправильный символ
    """
    if not s:
        return -1

    left = 0
    right = len(s) - 1
    while left <= right:
        mid = (right - left) // 2 + left
        if s[mid] == '1':
            left = mid+1
        elif s[mid] == '0':
            # Досрочный выход при нахождении правильной позиции
            if mid == 0 or s[mid-1] == '1':
                return mid
            else:
                right = mid-1
        else:
            raise FindZeroException(f"Неправильный символ '{s[mid]}', строка должна иметь вид '11111000'")
    else:
        return -1


class FindZeroException(Exception):
    """
    Ошибка при поиске первого нуля в функции find_zero
    """
    pass

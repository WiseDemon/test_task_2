def count_appearance(data:dict) -> int:
    """
    Функция полуает на вход спиок с интервалами урока и присутсвия учителя и ученика,
    считает время одновременного присутсвия учителя и ученика на уроке.
    Время указывается в секундах.
    :param data: словарь, содержащий три списка:
        -lesson: интервал проведения урока (список из двух элементов)
        -pupil: интервалы присутвия ученика (список из четного количества элементов,
            каждый четный элемент - время входа на урок, каждый нечетный - время выхода)
        -tutor: интервалы присутсвия учителя (список из четного количества элементов,
            каждый четный элемент - время входа на урок, каждый нечетный - время выхода)
    :return: общее время присутвия ученика и учителя на уроке одновременно
    """
    lesson = data['lesson']
    pupil = data['pupil']
    tutor = data['tutor']
    if not pupil or not tutor or not lesson:
        return 0

    appearance = 0
    p_pos = 0
    t_pos = 0

    new_pupil = pupil[:2]
    # объединение интервалов учеников, если они пересекаются
    while p_pos < len(pupil):
        p_start = pupil[p_pos]
        p_end = pupil[p_pos + 1]
        if p_start < new_pupil[-1] and p_end > new_pupil[-2]:
            new_pupil[-2] = min(p_start, new_pupil[-2])
            new_pupil[-1] = max(p_end, new_pupil[-1])
        else:
            new_pupil.extend([p_start, p_end])
        p_pos += 2
    p_pos = 0

    while p_pos < len(new_pupil) and t_pos < len(tutor):
        p_start = new_pupil[p_pos]
        p_end = new_pupil[p_pos + 1]
        t_start = tutor[t_pos]
        t_end = tutor[t_pos + 1]
        # проверка на пересечение интервалов
        if p_start < t_end and p_end > t_start:
            # добавляем пересечение с учетом интервала урока
            appearance += max(min(p_end, t_end, lesson[1]) -
                              max(p_start, t_start, lesson[0]), 0)

        # сменяем тот интервал, который закончился первым
        if p_end <= t_end:
            p_pos += 2
        if p_end >= t_end:
            t_pos += 2

    return appearance

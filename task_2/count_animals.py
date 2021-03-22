import urllib.request as r
from urllib.parse import quote
import json
from collections import Counter


class WikipediaResponseException(Exception):
    """
    Ошибка в ответе от википедии
    """
    def __init__(self, msg=None, response=None):
        super().__init__(msg)
        self.response = response


# Параметры обращения к апи википедии
endpoint = 'https://ru.wikipedia.org/w/api.php'
parameters = {'format': 'json',
              'list': 'categorymembers',
              'cmtitle': quote('Категория:Животные_по_алфавиту'),
              'cmprop': 'title',
              'cmtype': 'page',
              'cmlimit': '500',
              'cmsort': 'sortkey',
              'cmdir': 'asc'
              }

# Составление запроса
url = endpoint + '?action=query'
for key in parameters:
    url += '&' + key + '=' + parameters[key]

# Параметр-ссылка на продолжение списка
cmcontinue = ''

# Создание словаря с буквами русского алфавита для посдчета
cyrillic_alphabet = [chr(i) for i in range(ord('А'), ord('Я')+1)]
cyrillic_alphabet.insert(6, 'Ё')

counts = {char: 0 for char in cyrillic_alphabet}

repeats = 0
# Чтобы случайно не сделать слишком много запросов
while repeats < 1000:
    repeats += 1
    temp_url = url + '&cmcontinue=' + cmcontinue
    with r.urlopen(temp_url) as response:
        result = json.load(response)
        if 'batchcomplete' not in result:
            raise WikipediaResponseException('Ответ не содержит batchcomplete', result)
        # Достаем имена животных из ответа
        animals = [item['title'] for item in result['query']['categorymembers']]
        # Считаем первые буквы
        cur_counts = Counter(s[0] for s in animals)
        # Добавляем в общий словарь (игнорируем названия не с буквы русского алфавита на всякий случай)
        for key in cur_counts:
            if key.upper() in counts:
                counts[key.upper()] += cur_counts[key]
        if 'continue' in result:
            cmcontinue = result['continue']['cmcontinue']
        else:
            break
else:
    print('Остановка из-за превышения лимита запросов')

for key in counts:
    print(key + ': ', counts[key])

with open('answer.txt', 'w') as f:
    for key in counts:
        print(key + ': ', counts[key], file=f)
